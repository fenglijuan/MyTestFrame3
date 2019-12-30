import requests,json,traceback

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
            d=self.__get_param(d)
            d=self.__get_data(d)
            print(self.params)
        res=self.session.post(url,d,j,verify=False)
        self.result=res.content.decode(en)
        #print(self.result)
        try:
            self.jsonres=json.loads(self.result)
            #print(self.jsonres)
        except Exception as e:
            self.jsonres={}
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
    def addheaders(self,key,value):
        value=self.__get_param(value)
        self.session.headers[key]=value

    def assertequals(self,key,value,mothedname):

        res=str(self.result)
        try:
            res=str(self.jsonres[key])
        except Exception as e:
            pass
        if res==str(value):
            print(mothedname+':pass')
        else:print(mothedname+':fail')

    def savejson(self,key,p):
        try:
            self.params[p]=self.jsonres[key]
        except Exception as e:
            print("warning:保存参数失败!，没有"+key+"这个键")
            print(traceback.format_exc())



    def __get_data(self,s):
        param={}
        list1=s.split('&')
        for s2 in list1:
            list2=s2.split('=')
            try:
                param[list2[0]]=list2[1]
            except Exception as e:
                print('warning:参数格式不标准')
                print(traceback.format_exc())
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


