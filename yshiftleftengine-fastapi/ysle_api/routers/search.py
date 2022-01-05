from fastapi import APIRouter

import dao

searchRouter = APIRouter()


# 查询经验
@searchRouter.get("/search")
async def GetSearchResult():
    dao.ElasticSearchBase.GetAllIndices()
    dao.ElasticSearchBase.GetAllDocs('api')
    return {"message": "Hello World"}
