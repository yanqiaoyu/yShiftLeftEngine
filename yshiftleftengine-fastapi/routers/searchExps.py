from fastapi import APIRouter
from common.read_yaml import readYamlHandler
from dao.elasticsearch.elasticsearch_base import ElasticSearchBase

searchRouter = APIRouter()
esIndexName = readYamlHandler.read_conf()['elasticsearch']['esIndexName']
es = ElasticSearchBase()


@searchRouter.get("/dashboard/search")
async def GetSearchResult(searchInput: str = None):
    '''
    在标题和背景中,搜素关键字
    '''
    if searchInput:
        body = {
            "explain": True,
            "query": {
                "multi_match": {
                    "query": searchInput,
                    "fields": ["title", "background"]
                }
            },
            "sort": {
                "createTime": {
                    "order": "desc"
                },

                "_id": {
                    "order": "desc"
                }
            }
        }
        result = es.GetDocsBySearchInput(index=esIndexName, body=body)
        print(result)
        return {"data": result, "meta": {}}
    else:
        '''
        或者全部展示
        '''
        body = {
            "explain": True,
            "query": {
                "match_all": {}
            },
            "sort": {
                "createTime": {
                    "order": "desc"
                },

                "_id": {
                    "order": "desc"
                }
            }
        }
        result = es.GetAllDocs(indexName=esIndexName, body=body)
        return {"data": result, "meta": {}}
