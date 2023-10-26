from elasticsearch import Elasticsearch
import csv
import sys

body_sizes = []

def main():
    csv.field_size_limit(int(sys.maxsize / 4))
    es = Elasticsearch(request_timeout=600, hosts="http://localhost:9200")

    if not es.indices.exists(index="jusbrasil_15kb"):
        es.indices.create(index="jusbrasil_15kb", mappings= {
            "properties": {
                'id' : { "type": "text" },
                'body' : {"type": "text"},
                #'body_size' : { "type": "unsigned_long" },
                'title' : {"type": "text"},
                'date' : {"type": "text"},
                'court': {"type": "text"},
                'click_context': {"type": "text"},
                'copy_context': {"type": "text"},
                'expanded_copy_context': {"type": "text"},
                #"_size": {"enabled": {"type": "boolean"}, "store": {"type": "boolean"}},
            }
        })
        
    with open("data/bq-results-20230919-175133-1695146081962.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
                 body = str(row["body"])
                 size = len(body)
                 body_sizes.append(size)
                 new_body = ""
                 if size <= 15360:
                    new_body = body
                 else:
                    new_body = body[0:15360]
                         
                 res = es.index(
                    index='jusbrasil_15kb',
                    document= {
                        'id' : row["id"],
                        'body' : new_body,
                        'title' : row["title"],
                        'date' : row["date"],
                        'court': row["court"],
                        'click_context': row["click_context"],
                        'copy_context': row["copy_context"],
                        'expanded_copy_context': row["expanded_copy_context"]
                    }
                 )
                 if(res["result"]!="created"): print(res)
    
    with open("data/bs_babs.txt", "a") as bs:
        print(len(body_sizes))
        for size in body_sizes:
             bs.write(str(size))
             bs.write("\n")
         

if __name__ == "__main__":
    main()