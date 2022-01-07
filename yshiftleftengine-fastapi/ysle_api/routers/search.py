from fastapi import APIRouter

import dao

searchRouter = APIRouter()


# 查询经验
@searchRouter.get("/search")
async def GetSearchResult():
    # dao.ElasticSearchBase.InsertNewDoc(index='hello', doc=mappings2)
    result = dao.ElasticSearchBase.GetAllDocs('hello')
    return {"data": result, "meta": {}}