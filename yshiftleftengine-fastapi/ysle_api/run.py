from routers import search
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import sys
import os
# 把根目录添加进系统目录
sys.path.append(os.pardir)

from ysle_api.common import ES

from ysle_api.dao import ElasticSearchBase

es = ES.connectES()

app = FastAPI()

# 处理跨域请求
app.add_middleware(
    CORSMiddleware,
    # 允许所有的源进行请求
    allow_origins=["*"],
    allow_credentials=True,
    # 允许所有的请求方法
    allow_methods=["*"],
    # 允许所有的请求头
    allow_headers=["*"],
)

app.include_router(search.searchRouter)


def init():
    pass


def main():
    init()
    uvicorn.run(app="run:app",
                host="0.0.0.0",
                port=80,
                reload=True,
                debug=True)


if __name__ == '__main__':
    main()
