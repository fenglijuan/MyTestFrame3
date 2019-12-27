import requests,json

class HTTP:
    def __init__(self):
        self.session=requests.session()
        self.result=''
        self.jsonres={}
        self.params={}
    def  post(self,url,d=None,j=None,en='utf8'):
        if d is None:
            pass
        else:
            #print(d)
            d=self.__get_param(d)
            d=self.__get_data(d)
        res=self.session.post(url,d,j)
        self.result=res.content.decode(en)
        self.jsonres=json.loads(self.result)
    def  post2(self,url,d=None,j=None,en='utf8'):
        if d==None:
            pass
        else:
            d=self.__get_param2(d)
            d=self.__get_data(d)
        res=self.session.post(url,d,j)
        self.result=res.content.decode(en)
        self.jsonres=json.loads(self.result)

    def addheaders(self,key,value):
        value=self.__get_param(value)
        self.session.headers[key]=value

    def assertequals(self,key,value):
        if str(self.jsonres[key])==str(value):
            print('pass')
        else:print('fail')

    def savejson(self,key,p):
        self.params[p]=self.jsonres[key]

    def __get_data(self,s):
        param={}
        list1=s.split('&')
        for s2 in list1:
            list2=s2.split('=')
            try:
                param[list2[0]]=list2[1]
            except Exception as e:
                print('warning:参数格式不标准')
        return param
    def __get_param2(self,s):
        s=eval(s)
        return s
    #得到关联参数的值
    def __get_param(self,s):
        for key in self.params:
            s=s.replace('{'+key+'}',self.params[key])
        return s


