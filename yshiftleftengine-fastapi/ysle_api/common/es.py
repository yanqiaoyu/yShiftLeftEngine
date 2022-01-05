from elasticsearch import Elasticsearch
from common.read_yaml import readYamlHandler

es = None

mappings = {
    'tags': ['上传', '文件上传', 'base64', '加密', '正则校验'],
    'title':
    '一次由正则校验引起的文件上传异常',
    'background':
    '某一个项目存在文件上传的功能，在实际的测试过程中，虽然测试了文件名是中文的情况，但是发布后仍然出现了上传中文文件导致文件无法上传的情况',
    'rootCause':
    '文件上传时，后端程序首先会根据文件名做一次base64加密，然后生成一个新的文件，这个文件之后会作为创建一个任务的输入。在这个任务创建的时候，会针对这个加密过后的文件名做一次正则校验，问题就出在这里：base64加密的时候，可能会生成带有/，+，=等特殊符号的字符串，而出问题的正则校验没有对这种特殊符号的情况进行判断，从而导致了这种情况出现。',
    'testSuggestion':
    '如果待测的功能中含有正则校验，且这个正则校验的输入来源于客户，那么可以考虑输入一些正则校验无法覆盖全面的字符串.此案例中，我们可以上传 “欢迎使用本工具.txt”，进行上传的测试，因为这样base64加密过后，会产生一段“5qyi6L+O5L2/55So5pys5bel5YW3”这样的字符串'
}


class ES():
    @staticmethod
    def connectES():
        global es
        esHost = readYamlHandler.read_conf()['elasticsearch']['esAddress']
        esPort = readYamlHandler.read_conf()['elasticsearch']['esPort']
        if es == None:
            es = Elasticsearch(
                hosts=esHost,
                port=esPort,
            )
        return es


esHandler = ES.connectES()

if __name__ == "__main__":
    es = ES.connectES()

    # es.indices.create(index="hello")
    # result = es.indices.get(index="hello")
    # for index in result:
    #     print(index)
    # print(result)
    es.index(index="hello", document=mappings)
