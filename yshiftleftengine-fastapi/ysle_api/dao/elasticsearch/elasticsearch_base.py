from common.es import esHandler


class ElasticSearchBase:
    # 查询所有索引
    def GetAllIndices():
        for index in esHandler.indices.get('*'):
            if index[0] == '.':
                pass
            else:
                print(index)

    # 查询特定索引下面所有的内容
    def GetAllDocs(indexName):
        result = esHandler.search(index=indexName,
                                  doc_type="doc",
                                  body={
                                      'size': 10000,
                                      'query': {
                                          'match_all': {}
                                      }
                                  })
        print(result)
