from elasticsearch import Elasticsearch
from common.read_yaml import readYamlHandler


es = None


class ES():
    @staticmethod
    def connectES():
        global es
        esHost = readYamlHandler.read_conf()['elasticsearch']['esAddress']
        esPort = readYamlHandler.read_conf()['elasticsearch']['esPort']
        if es == None:
            es = Elasticsearch(
                hosts="http://"+esHost+":"+str(esPort),
            )
        return es


esHandler = ES.connectES()

if __name__ == "__main__":
    es = ES.connectES()

    # es.indices.create(index="hello")
    # result = es.indices.get(index="hello")
    # for index in result:
    #     print(index)
    # print(result)
    # es.index(index="hello", document=mappings2)
