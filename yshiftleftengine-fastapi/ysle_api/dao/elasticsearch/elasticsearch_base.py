from common.es import esHandler


class ElasticSearchBase:
    def GetAllIndices():
        '''
        查询所有索引,排除了.开头的内部索引
        '''
        result = []
        for index in esHandler.indices.get('*'):
            if index[0] == '.':
                pass
            else:
                result.append(index)
        return result

    def GetAllDocs(indexName):
        '''
        查询特定索引下面所有的文档
        '''
        return esHandler.search(index=indexName)

    def InsertNewDoc(index, doc):
        return esHandler.index(index=index, document=doc)