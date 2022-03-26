import re


def judgeSpecChar(input):
    pattern = r'[`\^=;,_!$%\(\)\\.\[\]:<>《》/?~！@#￥……&*（）――|{}【】‘；：”“\'。，、？]'
    result = re.search(pattern=pattern, string=input)
    # print("regex result:", result)
    return result
