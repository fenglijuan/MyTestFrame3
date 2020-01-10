from inter.Http import HTTP
import inspect,json,jsonpath
from common import config
# http=HTTP()
# http.post('http://testingedu.com.cn/inter/HTTP/auth')
# http.assertequals('status','200')
# http.savejson('token','t')
# http.addheaders('token','{t}')
#
# # http.post2('http://testingedu.com.cn/inter/HTTP/register',d="{'username': 'Will7','pwd': 'will','nickname': 'Will','describe': 'Will'}")
# # http.assertequals('status','200')
# # print(http.result)
# http.post('http://testingedu.com.cn/inter/HTTP/register',d="username=will6&pwd=will&nickname=will&describe=will")
# http.assertequals('status','200')
# print(http.result)
#
# http.post('http://testingedu.com.cn/inter/HTTP/login',d='username=will2&password')
# http.assertequals('status','200')
# print(http.result)
#
# http.savejson('userid','id')
# http.post('http://testingedu.com.cn/inter/HTTP/getUserInfo',d='id={id}')
# http.assertequals('status','200')
# print(http.result)
#
# http.post('http://testingedu.com.cn/inter/HTTP/logout')
# http.assertequals('status','200')

# http=HTTP()
# func = getattr(http, 'post')
# func('http://testingedu.com.cn/inter/HTTP/auth')
# args=inspect.getfullargspec(func).__str__()
# print(args)
# print(func.__doc__)
# args=args[args.find('args=')+5:args.rfind(', varargs=')]
# print(args)
# args=eval(args)
# args.remove('self')
# print(args)
# print(len(args))
# config.get_config('../lib/conf.properties')
# print(config.config)

s='{"status":"0","t":"1578276241940","set_cache_time":"","data":[{"location":"澳大利亚","titlecont":"IP地址查询","origip":"1.2.3.4","origipquery":"1.2.3.4","showlamp":"1","showLikeShare":1,"shareImage":1,"ExtendedLocation":"","OriginQuery":"1.2.3.4","tplt":"ip","resourceid":"6006","fetchkey":"1.2.3.4","appinfo":"","role_id":0,"disp_type":0}]}'
jsons=json.loads(s)
res=jsonpath.jsonpath(jsons,'$.data.[0].location')[0]
print(res)