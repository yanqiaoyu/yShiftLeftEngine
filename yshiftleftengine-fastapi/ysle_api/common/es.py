from elasticsearch import Elasticsearch

es_host = "103.44.241.227"

es = None


class ES():
    @staticmethod
    def connectES():
        global es
        if es == None:
            es = Elasticsearch(es_host,
                               sniff_on_start=True,
                               sniff_on_connection_fail=True,
                               sniff_timeout=5)
        return es


if __name__ == "__main__":
    es = ES.connectES()

    # es.indices.create(index="hello")
    result = es.indices.get("*")
    print(result)
