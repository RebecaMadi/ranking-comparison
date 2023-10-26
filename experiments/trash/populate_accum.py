from elasticsearch import Elasticsearch
import csv
import sys

body_sizes = []

def main():
    csv.field_size_limit(int(sys.maxsize / 4))
    es = Elasticsearch(request_timeout=600, hosts="http://localhost:9200")

    if not es.indices.exists(index="jusbrasil_500b"):
        es.indices.create(index="jusbrasil_500b", mappings= {
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
    if not es.indices.exists(index="jusbrasil_1kb"):
        es.indices.create(index="jusbrasil_1kb", mappings= {
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
    
    if not es.indices.exists(index="jusbrasil_10kb"):
        es.indices.create(index="jusbrasil_10kb", mappings= {
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
    
    if not es.indices.exists(index="jusbrasil_100kb"):
        es.indices.create(index="jusbrasil_100kb", mappings= {
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
    
    if not es.indices.exists(index="jusbrasil_500kb"):
        es.indices.create(index="jusbrasil_500kb", mappings= {
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
        
    if not es.indices.exists(index="jusbrasil_1mb"):
        es.indices.create(index="jusbrasil_1mb", mappings= {
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
        c500 = 0
        c1kb = 0
        c10kb = 0
        c100kb = 0
        c500kb = 0
        c1mb = 0
        for row in reader:
            size = sys.getsizeof(str(row["body"]))
            if size <= 1024000:
                c1mb += 1
                es.index(
                    index='jusbrasil_1mb',
                    document= {
                        'id' : row["id"],
                        'body' : row["body"],
                        'title' : row["title"],
                        'date' : row["date"],
                        'court': row["court"],
                        'click_context': row["click_context"],
                        'copy_context': row["copy_context"],
                        'expanded_copy_context': row["expanded_copy_context"]
                    }
                )
                if size <= 512000:
                    c500kb += 1
                    es.index(
                        index='jusbrasil_500kb',
                        document= {
                            'id' : row["id"],
                            'body' : row["body"],
                            'title' : row["title"],
                            'date' : row["date"],
                            'court': row["court"],
                            'click_context': row["click_context"],
                            'copy_context': row["copy_context"],
                            'expanded_copy_context': row["expanded_copy_context"]
                        }
                    )
                    if size <= 102400:
                        c100kb += 1
                        es.index(
                            index='jusbrasil_100kb',
                            document= {
                                'id' : row["id"],
                                'body' : row["body"],
                                'title' : row["title"],
                                'date' : row["date"],
                                'court': row["court"],
                                'click_context': row["click_context"],
                                'copy_context': row["copy_context"],
                                'expanded_copy_context': row["expanded_copy_context"]
                            }
                        )
                        if size <= 10240:
                            c10kb += 1
                            es.index(
                                index='jusbrasil_10kb',
                                document= {
                                    'id' : row["id"],
                                    'body' : row["body"],
                                    'title' : row["title"],
                                    'date' : row["date"],
                                    'court': row["court"],
                                    'click_context': row["click_context"],
                                    'copy_context': row["copy_context"],
                                    'expanded_copy_context': row["expanded_copy_context"]
                                }
                            )
                            if size <=1024:
                                c1kb += 1
                                es.index(
                                    index='jusbrasil_1kb',
                                    document= {
                                        'id' : row["id"],
                                        'body' : row["body"],
                                        'title' : row["title"],
                                        'date' : row["date"],
                                        'court': row["court"],
                                        'click_context': row["click_context"],
                                        'copy_context': row["copy_context"],
                                        'expanded_copy_context': row["expanded_copy_context"]
                                    }
                                )
                                if size <= 500:
                                    c500 += 1
                                    es.index(
                                        index='jusbrasil_500b',
                                        document= {
                                            'id' : row["id"],
                                            'body' : row["body"],
                                            'title' : row["title"],
                                            'date' : row["date"],
                                            'court': row["court"],
                                            'click_context': row["click_context"],
                                            'copy_context': row["copy_context"],
                                            'expanded_copy_context': row["expanded_copy_context"]
                                        }
                                    )
            else:
                print(row)
                print(size)       

        print("final:")
        print(c500)
        print(c1kb)
        print(c10kb)
        print(c100kb)
        print(c500kb)
        print(c1mb)
        print(c500 + c1kb + c10kb + c100kb + c500kb + c1mb)
        

if __name__ == "__main__":
    main()