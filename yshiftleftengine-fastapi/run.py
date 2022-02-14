from common.read_yaml import readYamlHandler
from dao.elasticsearch.elasticsearch_base import ElasticSearchBase
from routers import search
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import sys
import os
# 把根目录添加进系统目录
sys.path.append(os.pardir)


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


def only4Test():
    '''
    仅用于测试
    '''
    # print("beginning test")
    # from dao.elasticsearch import elasticsearch_base
    # a = ElasticSearchBase()
    # a.DeleteIndex("api")

    from dao.elasticsearch.elasticsearch_base import InitElasticSearch
    InitElasticSearch()

    # a = ElasticSearchBase()
    # a.ReIndex()


def main():
    only4Test()
    # initAPIService()


if __name__ == '__main__':
    main()
