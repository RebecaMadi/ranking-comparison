for query, response in ref_queries.items():
        optimal_ids = [res["doc_id"] for res in response]
        idcg = dcg(optimal_ids, optimal_ids, 3)

        raw = es.search(index="jusbrasil_1kb_p", query={
            "multi_match": {
                "fields": ["title", "body"],
                "query": query
            }
        }, _source=["id"], size=3)["hits"]["hits"]

        aux = list()
        for res in raw:
            aux.append(int(res["_source"]["id"]))

        var_dcg = dcg(aux, optimal_ids, 3)
        kb1_dcgs.append(var_dcg)
        kb1_ndcgs.append(var_dcg / idcg)

    for query, response in ref_queries.items():
        optimal_ids = [res["doc_id"] for res in response]
        idcg = dcg(optimal_ids, optimal_ids, 3)

        raw = es.search(index="jusbrasil_10kb_p", query={
            "multi_match": {
                "fields": ["title", "body"],
                "query": query
            }
        }, _source=["id"], size=3)["hits"]["hits"]

        aux = list()
        for res in raw:
            aux.append(int(res["_source"]["id"]))

        var_dcg = dcg(aux, optimal_ids, 3)
        kb10_dcgs.append(var_dcg)
        kb10_ndcgs.append(var_dcg / idcg)

    for query, response in ref_queries.items():
        optimal_ids = [res["doc_id"] for res in response]
        idcg = dcg(optimal_ids, optimal_ids, 3)

        raw = es.search(index="jusbrasil_100kb_p", query={
            "multi_match": {
                "fields": ["title", "body"],
                "query": query
            }
        }, _source=["id"], size=3)["hits"]["hits"]

        aux = list()
        for res in raw:
            aux.append(int(res["_source"]["id"]))

        var_dcg = dcg(aux, optimal_ids, 3)
        kb100_dcgs.append(var_dcg)
        kb100_ndcgs.append(var_dcg / idcg)

    for query, response in ref_queries.items():
        optimal_ids = [res["doc_id"] for res in response]
        idcg = dcg(optimal_ids, optimal_ids, 3)

        raw = es.search(index="jusbrasil_500kb_p", query={
            "multi_match": {
                "fields": ["title", "body"],
                "query": query
            }
        }, _source=["id"], size=3)["hits"]["hits"]

        aux = list()
        for res in raw:
            aux.append(int(res["_source"]["id"]))

        var_dcg = dcg(aux, optimal_ids, 3)
        kb500_dcgs.append(var_dcg)
        kb500_ndcgs.append(var_dcg / idcg)
    
    for query, response in ref_queries.items():
        optimal_ids = [res["doc_id"] for res in response]
        idcg = dcg(optimal_ids, optimal_ids, 3)

        raw = es.search(index="jusbrasil_1mb_p", query={
            "multi_match": {
                "fields": ["title", "body"],
                "query": query
            }
        }, _source=["id"], size=3)["hits"]["hits"]

        aux = list()
        for res in raw:
            aux.append(int(res["_source"]["id"]))

        var_dcg = dcg(aux, optimal_ids, 3)
        mb1_dcgs.append(var_dcg)
        mb1_ndcgs.append(var_dcg / idcg)


        print(f"NDCG index apenas com docs < 1kb: {mean(kb1_ndcgs)}")
    print(f"DCG index apenas com docs < 1kb: {mean(kb1_dcgs)}")
    print(f"NDCG index apenas com docs < 10kb: {mean(kb10_ndcgs)}")
    print(f"DCG index apenas com docs < 10kb: {mean(kb10_dcgs)}")
    print(f"NDCG index apenas com docs < 100kb: {mean(kb100_ndcgs)}")
    print(f"DCG index apenas com docs < 100kb: {mean(kb100_dcgs)}")
    print(f"NDCG index apenas com docs 100kb < x < 500kb: {mean(kb500_ndcgs)}")
    print(f"DCG index apenas com docs 100kb < x < 500kb: {mean(kb500_dcgs)}")
    print(f"NDCG index apenas com docs < 1mb: {mean(mb1_ndcgs)}")
    print(f"DCG index apenas com docs < 1mb: {mean(mb1_dcgs)}")
