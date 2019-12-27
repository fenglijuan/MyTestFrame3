from inter.Http import HTTP
http=HTTP()
http.post('http://testingedu.com.cn/inter/HTTP/auth')
http.assertequals('status','200')
http.savejson('token','t')
http.addheaders('token','{t}')

# http.post2('http://testingedu.com.cn/inter/HTTP/register',d="{'username': 'Will7','pwd': 'will','nickname': 'Will','describe': 'Will'}")
# http.assertequals('status','200')
# print(http.result)
http.post('http://testingedu.com.cn/inter/HTTP/register',d="username=will6&pwd=will&nickname=will&describe=will")
http.assertequals('status','200')
print(http.result)

http.post('http://testingedu.com.cn/inter/HTTP/login',d='username=will2&password')
http.assertequals('status','200')
print(http.result)

http.savejson('userid','id')
http.post('http://testingedu.com.cn/inter/HTTP/getUserInfo',d='id={id}')
http.assertequals('status','200')
print(http.result)

http.post('http://testingedu.com.cn/inter/HTTP/logout')
http.assertequals('status','200')