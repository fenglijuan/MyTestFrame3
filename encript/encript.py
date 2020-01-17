import os
from common import logger
#result=os.popen('ipconfig').read()
# cmd='java -jar decript.jar 0 123456'
# result=os.popen(cmd).read()
# print(result)

def dencript(t,s):
    '''

    :param t: 0表示加密，其他字符串表示解密
    :param s:需要加密或解密的字符串
    :return:加密或解密后的字符串
    '''
    cmd = 'java -jar decript.jar '+str(t)+' '+ str(s)
    try:
        result = str(os.popen(cmd).read())
    except Exception as e:
        result=''
        logger.exception(e)
    return result
