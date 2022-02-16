from fastapi import APIRouter
from common.read_yaml import readYamlHandler
from dao.elasticsearch.elasticsearch_base import ElasticSearchBase

searchRouter = APIRouter()
esIndexName = readYamlHandler.read_conf()['elasticsearch']['esIndexName']
es = ElasticSearchBase()


# 查询经验
@searchRouter.get("/search")
async def GetSearchResult():
    result = es.GetAllDocs(esIndexName)
    return {"data": result, "meta": {}}
