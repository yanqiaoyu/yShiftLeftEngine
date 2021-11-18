from fastapi import APIRouter

searchRouter = APIRouter()


@searchRouter.get("/search")
async def GetSearchResult():
    return {"message": "Hello World"}
