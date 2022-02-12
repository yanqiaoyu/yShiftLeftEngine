from numpy import source
from common.es import esHandler, esHelpers
from elasticsearch import helpers


class ElasticSearchBase:
    def GetAllIndices(self):
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

    def GetAllDocs(self, indexName):
        '''
        查询特定索引下面所有的文档
        '''
        return esHandler.search(index=indexName)

    def InsertNewDoc(self, index, doc):
        '''
        在指定的索引里面插入新的文档
        '''
        return esHandler.index(index=index, document=doc)

    def DeleteIndex(self, index):
        '''
        删除特定的索引
        '''
        esHandler.indices.delete(index=index)

    def ReIndex(self):
        '''
        迁移文档
        '''
        # esHelpers.reindex(client=esHandler,
        #                 source_index="hello", target_index="experience", target_client=esHandler)
        body = {
            "source": {
                "index": "my-index-000001"
            },
            "dest": {
                "index": "my-new-index-000001"
            }
        }
        esHandler.reindex(body=body)
