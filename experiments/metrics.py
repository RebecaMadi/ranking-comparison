import csv
from math import log
from statistics import mean
from elasticsearch import Elasticsearch

ranking = list()
ranking2 = list()

REF_COLLECTION_PATH = "data/referencia.csv"

def adjust_queries(path):
    with open("data/referencia.csv", mode='w') as output, open(path, mode='r', encoding="utf-8-sig") as file:
        reader = file.readlines()
        for line in reader:
            output.write(line.replace("\"", ""))


def load_ref_queries(path):
    queries = dict()
    with open(path, mode='r', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter="|")
        for row in reader:
            queries[row["query"]] = list()
            items = list(row.values())
            n = len(items)
            for i in range(1, n, 2):
                try:
                    queries[row["query"]].append({ "doc_id": int(items[i]), "doc_title": items[i+1] })
                except ValueError:
                    break
                except TypeError:
                    break
    return queries

def searchEqual(optimals, value):
    for i in range(len(optimals)):
        if value == optimals[i]:
            return 1
    return 0

#DCG para DCG@N
def dcg(queries, optimals, n):
    dcg = 0.0
    for i in range(min(n, len(queries))):
        if searchEqual(optimals, queries[i])==1:
            dcg = dcg + (1.0 / log(i+2, 2))
    return dcg



def main():
    es = Elasticsearch(request_timeout=600, hosts="http://localhost:9200")
    ref_queries = load_ref_queries(REF_COLLECTION_PATH)
    raw_ndcgs, b500_ndcgs= list(), list()
    raw_dcgs, b500_dcgs= list(), list()
    i = 0
    for query, response in ref_queries.items():
        optimal_ids = [res["doc_id"] for res in response]
        idcg = dcg(optimal_ids, optimal_ids, 3)
        raw = es.search(index="jusbrasil_completo", query={
            "multi_match": {
                "fields": ["title", "body"],
                "query": query
            }
        }, _source=["id"], size=3)["hits"]["hits"]

        aux = list()
        for res in raw:
            aux.append(int(res["_source"]["id"]))

        ranking.append(aux)
        i += 1
        var_dcg = dcg(aux, optimal_ids, 3)
        raw_dcgs.append(var_dcg)
        raw_ndcgs.append(var_dcg / idcg)
    i = 0
    diff = 0
    diffr = 0
    for query, response in ref_queries.items():
        optimal_ids = [res["doc_id"] for res in response]
        idcg = dcg(optimal_ids, optimal_ids, 3)

        raw = es.search(index="jusbrasil_15kb", query={
            "multi_match": {
                "fields": ["title", "body"],
                "query": query
            }
        }, _source=["id"], size=3)["hits"]["hits"]

        aux = list()
        for res in raw:
            aux.append(int(res["_source"]["id"]))

        #r = ranking[i]
        #cont = 0
        #print("query: " + query)
        #print(r)
        #print(aux)
        #n = 0
        #dis = 0
        #conc = 0
        #for i in range(len(aux)):
           #for j in range(len(aux)):
            #    n += 1
             #   if (aux[i] < aux[j] and r[i] < r[j]) or (aux[i]> aux[j] and r[i] > r[j]):
              #     conc += 1
               # elif (aux[i] < aux[j] and r[i] > r[j]) or (aux[i] > aux[j] and r[i] < r[j]):
                #   dis += 1
        #print("novo")
        #print(r)
        #print(aux)
        #print(optimal_ids)
        
                #print("e: " + str(e))
                #print("cont: " + str(r[cont]))
                #print("cont v: " + str(cont))  
                #break
            #print("e: " + str(e))
            #cont += 1
                  
        #t = (conc - dis)/((n*(n-1))/2)
        #print("tau: " + str(t))
        #i = i+1
        ranking2.append(aux)
        var_dcg = dcg(aux, optimal_ids, 3)
        b500_dcgs.append(var_dcg)
        b500_ndcgs.append(var_dcg / idcg)

    m2 = 0
    m1 = 0
    for i in range(len(ranking)):
        if ranking[i] != ranking2[i]:
            if raw_ndcgs[i] <= b500_ndcgs[i]:
                m2 += 1
            else:
                m1 += 1
            diff += 1
    
    #with open("data/ranking.txt", "a") as bs:
     #   print(len(ranking))
      #  for size in ranking:
       #      bs.write(str(ranking))
        #     bs.write("\n")

    #No total difere em 455 consultas

    print(diff)
    print(m1)
    print(m2)
    #print(diffr)
    print(f"NDCG - BM25 puro: {mean(raw_ndcgs)}")
    print(f"DCG  - BM25 puro: {mean(raw_dcgs)} ")
    print(f"NDCG index apenas com docs < 15kb: {mean(b500_ndcgs)}")
    print(f"DCG index apenas com docs < 15kb: {mean(b500_dcgs)}")
    
if __name__ == "__main__":
    main()