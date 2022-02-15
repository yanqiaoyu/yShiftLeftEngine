from attr import fields
from numpy import source
from sqlalchemy import false, true
from common.es import esHandler
from common.read_yaml import readYamlHandler

experienceIndexMappings = {
    "mappings": {
        # 禁止动态新增字段
        "dynamic": "strict",

        # 具体的字段写在这里面
        "properties": {
            # 作者
            "author": {
                "type": "text",
                # 作者这个字段不建立索引
                "index": False
            },
            # 点击量
            "clicks": {
                "type": "long",
                # 点击量这个字段不建立索引
                "index": False
            },
            # 参考链接
            "reference": {
                "type": "text",
                # 参考链接这个字段不建立索引
                "index": False
            },
            # 添加时间
            "createTime": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis",
                # 添加时间这个字段不建立索引
                "index": False,
            },
            # 修改时间
            "updateTime": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis",
                # 修改时间这个字段不建立索引
                "index": False,
                # 修改时间这个字段不进行聚合排序以及脚本操作
                "doc_values": False
            },
            # tags
            "tags": {
                "type": "keyword",
                # 需要聚合，且数据量较大，但唯一值较少
                "eager_global_ordinals": True,
            },
            # 问题背景
            "background": {
                "type": "text",
                # 问题背景不需要聚合排序
                "doc_values": False,
                # 内容为大字段，单独存储，用于查询返回
                "store": True
            },
            # 问题根因
            "rootCause": {
                "type": "text",
                # 问题根因不需要聚合排序
                "doc_values": False,
                # 内容为大字段，单独存储，用于查询返回
                "store": True
            },
            # 测试建议
            "testSuggestion": {
                "type": "text",
                # 测试建议不需要聚合排序
                "doc_values": False,
                # 内容为大字段，单独存储，用于查询返回
                "store": True
            },
            # 标题
            "title": {
                "type": "text",
                "analyzer": "ik_max_word",
                # 检索的分词没必要细粒度，提升效率
                "search_analyzer": "ik_smart",
                # 对 标题 不需要聚合、排序
                "doc_values": False,
                # 提升该字段的权重
                "boost": 5
            }
        }
    },
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
        esHandler.indices.create(
            index=esIndexName, body=experienceIndexMappings)
