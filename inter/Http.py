import requests,json,jsonpath
from common.logger import *
from suds.client import Client
from suds.xsd.doctor import Import,ImportDoctor
class HTTP:
    def __init__(self,writer):
        #忽略警告
        requests.packages.urllib3.disable_warnings()
        self.session=requests.session()
        self.session.headers['content-type'] = 'application/x-www-form-urlencoded'
        self.session.headers[
            'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

        self.result=''
        self.jsonres={}
        self.params={}
        self.url=''
        self.writer=writer
    def seturl(self,u):
        '''
        设置请求的url host地址
        :param u:url的host地址
        :return:无
        '''
        if u.startswith('http')or u.startswith('https'):
            self.url=u
            self.writer.write(self.writer.row,7,'pass')
            self.writer.write(self.writer.row, 8, self.url)
        else:
            #print('error:url格式错误')
            logger.error('error:url格式错误')
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, 'url格式错误')
    def  post(self,url,d=None,j=None):
        '''
        发送post请求
        :param url: url路径，可以是单纯的路径+全局的host,也可以是http/https开头的绝对路径
        :param d:标准url data传参
        :param j:传递json字符串的参数
        :return:无
        '''
        if not(url.startswith('http')or url.startswith('https')):
            url=self.url+'/'+url
        if d is None or d=='':
            pass
        else:
            d=self.__get_param(d)
            d=self.__get_data(d)
            #print(self.params)
        res=self.session.post(url,d,j,verify=False)
        self.result=res.content.decode('utf8')
        #print(self.result)
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]
            #print(jsons)
            self.jsonres = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(jsons))
            # self.jsonres=json.loads(self.result)
            # self.writer.write(self.writer.row, 7, 'pass')
            # self.writer.write(self.writer.row, 8, str(self.jsonres))
            #print(self.jsonres)
        except Exception as e:
            self.jsonres={}
            logger.exception(e)
            #不是json格式不代表失败
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(self.result))
    # def  post2(self,url,d=None,j=None,en='utf8'):
    #     if d==None:
    #         pass
    #     else:
    #         d=self.__get_param2(d)
    #         d=self.__get_data(d)
    #     res=self.session.post(url,d,j)
    #     self.result=res.content.decode(en)
    #     self.jsonres=json.loads(self.result)
    #
    def  get(self,url,params=None):
        '''
        发送post请求
        :param url: url路径，可以是单纯的路径+全局的host,也可以是http/https开头的绝对路径
        :param d:标准url data传参
        :param j:传递json字符串的参数
        :return:无
        '''
        if not(url.startswith('http')or url.startswith('https')):
            url=self.url+'/'+url
        else:
            url=url+"?"+params
        #如果https请求，报ssl错误，就添加verify=False参数
        res=self.session.get(url,verify=False)
        self.result=res.content.decode('utf8')
        #print(self.result)
        try:
            jsons=self.result
            jsons=jsons[jsons.find('{'):jsons.rfind('}')+1]
            print(jsons)
            self.jsonres=json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(jsons))
            #print(self.jsonres)
        except Exception as e:
            self.jsonres={}
            logger.error(e)
            # 不是json格式不代表失败
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(self.result))
    def removeheader(self,key):
        '''
        从头里面删除一个键值对
        :param key: 要删除的键
        :return: 无
        '''
        try:
            self.session.headers.pop(key)
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
        except Exception as e:
            logger.error('没有'+key+'这个键的header存在')
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
    def addheader(self,key,value):
        '''
        添加一个键值对，支持关联
        :param key:要添加的键
        :param value:键的值
        :return:无
        '''
        value=self.__get_param(value)
        self.session.headers[key]=value
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, str(self.session.headers))
    def assertequals(self,jpath,value):
        '''
        断言json结果里面，某个键的值和value相等
        :param key:json结果的键
        :param value:预期的值
        :return:无
        '''
        value=self.__get_param(value)
        res=str(self.result)
        try:
            res=str(jsonpath.jsonpath(self.jsonres,jpath)[0])
        except Exception as e:
            pass
        if res==str(value):
            logger.info('pass')
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, res)
        else:
            logger.info('fail')
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8,'实际结果：'+res+';预期结果：'+value)
    def assertequals2(self,key,value,mothedname):
        '''
        断言json结果里面，某个键的值和value相等
        :param key:json结果的键
        :param value:预期的值
        :param mothedname:
        :return:无
        '''
        res=str(self.result)
        try:
            res=str(self.jsonres[key])
        except Exception as e:
            pass
        if res==str(value):
            print(mothedname+':pass')
        else:print(mothedname+':fail')

    def savejson(self,jpath,p):
        '''
        将需要保存数据，保存为参数p的值
        :param key:需要保存的jsond的键
        :param p:保存后，调用参数的参数名字{p}
        :return:无
        '''
        try:
            #self.params[p]=self.jsonres[key]
            self.params[p] =str(jsonpath.jsonpath(self.jsonres,jpath)[0])
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(self.params[p]))
        except Exception as e:
            logger.error("保存参数失败!，没有"+key+"这个键")
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(self.jsonres))



    def __get_data(self,s):
        #默认是标准的url参数
        flg=False
        param={}
        list1=s.split('&')
        for s2 in list1:
            list2=s2.split('=')
            try:
                param[list2[0]]=list2[1]
            except Exception as e:
                flg=True
                logger.error('参数格式不标准')
                logger.exception(e)
        if flg:
            s=s.encode('utf-8')
            return s
        else:
            return param
    def __get_param2(self,s):
        s=eval(s)
        return s
    #得到关联参数的值
    def __get_param(self,s):
        for key in self.params:
            s=s.replace('{'+key+'}',self.params[key])
            #print('s='+s)
        return s

class SOAP:

    def __init__(self,writer):
        #定义wadl描述文档的地址
        self.wsdl=''
        self.client=None
        self.result=''
        self.jsonres={}
        self.writer = writer
        self.headers={}
        self.params={}


    #设置wsdl路径，并解析webservice服务
    def setwsdl(self,url):
        self.wsdl = url
        self.client=Client(url,doctor=self.doctor)
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, self.wsdl)
        self.doctor=None
    def adddoctor(self,s,x,n):
        imp = Import(s, location=x)
        imp.filter.add(n)
        self.doctor = ImportDoctor(imp)
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def callmethod(self,m,l=None):
        if l==None or l=='':
            try:
                self.result = self.client.service.__getattr__(m)()
            except Exception as e:
                #logger.exception(e)
                self.result=e.__str__()
                print(self.result)
        else:
            l=l.split('、')
            for i in range(len(l)):
                l[i]=self.__get_param(l[i])
            try:
                self.result=self.client.service.__getattr__(m)(*l)
            except Exception as e:
                logger.exception(e)
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]
            #print(jsons)
            self.jsonres = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(jsons))
            # self.jsonres=json.loads(self.result)
            # self.writer.write(self.writer.row, 7, 'pass')
            # self.writer.write(self.writer.row, 8, str(self.jsonres))
            # print(self.jsonres)
        except Exception as e:
            self.jsonres = {}
            logger.exception(e)
            # 不是json格式不代表失败
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(self.result))
    def addheader(self,key,value):
        value=self.__get_param(value)
        self.headers[key]=value
        self.client = Client(self.wsdl,headers=self.headers)
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, str(self.result))
    def removeheader(self,key,value):
        self.headers.pop(key)
        self.client = Client(self.wsdl,headers=self.headers)
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, str(self.result))
    def savejson(self,jpath,p):
        '''
        将需要保存数据，保存为参数p的值
        :param key:需要保存的jsond的键
        :param p:保存后，调用参数的参数名字{p}
        :return:无
        '''
        try:
            #self.params[p]=self.jsonres[key]
            self.params[p] =str(jsonpath.jsonpath(self.jsonres,jpath)[0])
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, str(self.params[p]))
        except Exception as e:
            logger.error("保存参数失败!，没有"+key+"这个键")
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
    def assertequals(self,jpath,value):
        '''
        断言json结果里面，某个键的值和value相等
        :param key:json结果的键
        :param value:预期的值
        :return:无
        '''
        value=self.__get_param(value)
        res=str(self.result)
        try:
            res=str(jsonpath.jsonpath(self.jsonres,jpath)[0])
        except Exception as e:
            pass
        if res==str(value):
            logger.info('pass')
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, res)
        else:
            logger.info('fail')
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8,'实际结果：'+res+';预期结果：'+value)

    def __get_param(self, s):
        #按规则获取关联的参数
        #遍历已经保存的参数，并将传入字符串里面，满足{key}所有字符串用key的值来替代
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])
            # print('s='+s)
        return s