from fastapi import APIRouter
from dao.elasticsearch.elasticsearch_base import ElasticSearchBase, expPipelineWhenCreated
from common.read_yaml import readYamlHandler
from services.collectExpsInYaml import CollectExpsInYaml

addRouter = APIRouter()
esIndexName = readYamlHandler.read_conf()['elasticsearch']['esIndexName']
esExpPipelineName = readYamlHandler.read_conf(
)['elasticsearch']['esExpPipelineName']
es = ElasticSearchBase()


@addRouter.post("/dashboard/add")
async def PostNewExperience():
    '''
    在指定的索引里面添加文档
    '''
    # import json
    experiences = CollectExpsInYaml()
    for singleExp in experiences:
        es.InsertNewDoc(index=esIndexName, doc=singleExp,
                        pipeline=esExpPipelineName)

    return {'data': '', 'meta': 200}
