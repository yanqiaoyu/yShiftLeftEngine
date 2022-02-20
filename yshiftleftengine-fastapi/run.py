from common.read_yaml import readYamlHandler
from routers import search, add
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import sys
import os
from dao.elasticsearch.elasticsearch_base import InitElasticSearch
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
app.include_router(add.addRouter)


# 初始化api服务
def initAPIService():
    bindAddress = readYamlHandler.read_conf()['apiService']['bindAddress']
    bindPort = readYamlHandler.read_conf()['apiService']['bindPort']
    uvicorn.run(app="run:app",
                host=bindAddress,
                port=bindPort,
                reload=True,
                debug=True)


# 初始化es数据库服务
def initElasticSearchServices():
    InitElasticSearch()


def only4Test():
    '''
    仅用于测试
    '''
    # print("beginning test")
    # from dao.elasticsearch import elasticsearch_base
    # a = ElasticSearchBase()
    # a.DeleteIndex("api")
    from dao.elasticsearch.elasticsearch_base import ElasticSearchBase
    a = ElasticSearchBase()
    # a.ReIndex("hello", "experience")
    body = {
        'doc': {
            'title': '2022-02-16',
            'createTime': '2022-02-16'
        }
    }
    a.UpdateDocs(index="experience", id="SCCgcn0BLMCW-yuGV_5H", body=body)


def main():
    # only4Test()
    initElasticSearchServices()
    initAPIService()


if __name__ == '__main__':
    main()
