from fastapi import APIRouter, Body
from common.read_yaml import readYamlHandler
from dao.elasticsearch.elasticsearch_base import ElasticSearchBase

searchRouter = APIRouter()
esIndexName = readYamlHandler.read_conf()['elasticsearch']['esIndexName']
es = ElasticSearchBase()


@searchRouter.get("/dashboard/search")
async def GetSearchResult(searchInput: str):
    '''
    在标题和背景中,搜素关键字
    '''
    # print("SearchInput: ", searchInput)

    body = {
        "explain": True,
        "query": {
            "multi_match": {
                "query": searchInput,
                "fields": ["title", "background"]
            }
        }
    }
    result = es.GetDocsBySearchInput(index=esIndexName, body=body)
    print(result)
    return {"data": result, "meta": {}}
