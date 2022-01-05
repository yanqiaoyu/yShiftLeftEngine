from routers import search
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import sys
import os
# 把根目录添加进系统目录
sys.path.append(os.pardir)

from common.read_yaml import readYamlHandler

app = FastAPI()
'''
https://fastapi.tiangolo.com/zh/tutorial/cors/
来自官网的处理跨域请求的方法
'''
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


# 初始化api服务
def initAPIService():
    bindAddress = readYamlHandler.read_conf()['apiService']['bindAddress']
    bindPort = readYamlHandler.read_conf()['apiService']['bindPort']
    uvicorn.run(app="run:app",
                host=bindAddress,
                port=bindPort,
                reload=True,
                debug=True)


def main():
    initAPIService()


if __name__ == '__main__':
    main()
