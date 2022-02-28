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
                "type": "nested",
                "properties": {
                    "linkName": {
                        "type": "text",
                        # 不建立索引
                        "index": False
                    },
                    "linkURL": {
                        "type": "text",
                        # 不建立索引
                        "index": False
                    },
                },

            },
            # 添加时间
            "createTime": {
                "type": "date",
                # "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis",
                # 添加时间这个字段不建立索引
                "index": False,
            },
            # 修改时间
            "updateTime": {
                "type": "date",
                # "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis",
                # 修改时间这个字段不建立索引
                "index": False,
                # 修改时间这个字段不进行聚合排序以及脚本操作
                "doc_values": False
            },
            # tags
            "tags": {
                "type": "text",
                "analyzer": "ik_max_word",
            },
            # 问题背景
            "background": {
                "type": "text",
                # 问题背景不需要聚合排序
                "doc_values": False,
                "analyzer": "ik_max_word",
                # 检索的分词没必要细粒度，提升效率
                "search_analyzer": "whitespace",
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
                "search_analyzer": "whitespace",
                # 对 标题 不需要聚合、排序
                "doc_values": False,
                # 提升该字段的权重
                "boost": 5
            }
        }
    },
}

expPipelineWhenCreated = {
    "description": "my exp pipeline when created",
    "processors": [
        {
            "script": {
                "lang": "painless",
                "source": """DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssX"); df.setTimeZone(TimeZone.getTimeZone("Asia/Shanghai")); Date date = new Date(); ctx.createTime = df.format(date);"""
            }
        },
        {
            "script": {
                "lang": "painless",
                "source": """DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssX"); df.setTimeZone(TimeZone.getTimeZone("Asia/Shanghai")); Date date = new Date(); ctx.updateTime = df.format(date);"""
            }
        },
        {
            "set": {
                "field": "clicks",
                "value": 0
            }
        }
    ]
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

    def GetAllDocs(self, indexName, body=None):
        '''
        查询特定索引下面所有的文档
        '''
        return esHandler.search(index=indexName, size=10000, body=body)

    def GetDocsBySearchInput(self, index, body):
        '''
        根据查询名词
        '''
        return esHandler.search(index=index, size=10000, body=body)

    def InsertNewDoc(self, index, doc, pipeline=None):
        '''
        在指定的索引里面插入新的文档
        '''
        return esHandler.index(index=index, document=doc, pipeline=pipeline)

    def DeleteIndex(self, index):
        '''
        删除特定的索引
        '''
        esHandler.indices.delete(index=index)

    def ReIndex(self, sourceIndex, destIndex):
        '''
        迁移文档,需要保证source和dest都存在
        '''

        body = {
            "source": {
                "index": sourceIndex
            },
            "dest": {
                "index": destIndex
            }
        }
        esHandler.reindex(body=body)

    def UpdateDocs(self, index, id, body):
        '''
        更新文档:你需要指定 index id 和 body
        '''
        result = esHandler.update(index=index, id=id, body=body)
        print(result['result'])


def InitElasticSearch():
    '''
    初始化Elasticsearch数据库
    1. 新建索引 需要ES中存在IK分词器的插件,否则建索引报错
    2. 新建pipeline 
    '''

    esIndexName = readYamlHandler.read_conf()['elasticsearch']['esIndexName']
    esExpPipelineName = readYamlHandler.read_conf(
    )['elasticsearch']['esExpPipelineName']

    # 判断索引存不存在
    if esHandler.indices.exists(index=esIndexName):
        # 存在则不新建
        pass
    else:
        # 不存在则新建
        esHandler.indices.create(
            index=esIndexName, body=experienceIndexMappings)

    esHandler.ingest.put_pipeline(
        id=esExpPipelineName, body=expPipelineWhenCreated)
