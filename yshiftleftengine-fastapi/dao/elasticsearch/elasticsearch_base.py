from attr import fields
from numpy import source
from sqlalchemy import false
from common.es import esHandler
from common.read_yaml import readYamlHandler

experienceIndexMappings = {
    "mappings": {
        # 禁止动态新增字段
        "dynamic": "strict"
    },
    # 具体的字段写在这里面
    "properties": {
        # 作者
        "author": {
            "type": "text",
            # 作者这个字段不建立索引
            "index": false
        },
        # 点击量
        "clicks": {
            "type": "long",
            # 点击量这个字段不建立索引
            "index": false
        },
        # 参考链接
        "reference": {
            "type": "text",
            # 参考链接这个字段不建立索引
            "index": false
        },
        # 添加时间
        "createTime": {
            "type": "date",
            "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis",
            # 添加时间这个字段不建立索引
            "index": false,
        },
        # 修改时间
        "updateTime": {

        }
    }
}


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

        body = {
            "source": {
                "index": "my-index-000001"
            },
            "dest": {
                "index": "my-new-index-000001"
            }
        }
        esHandler.reindex(body=body)


def InitElasticSearch():
    '''
    初始化Elasticsearch数据库
    '''

    esIndexName = readYamlHandler.read_conf()['elasticsearch']['esIndexName']

    # 判断索引存不存在
    if esHandler.indices.exists(index=esIndexName):
        # 存在则不新建
        pass
    else:
        # 不存在则新建
        pass
