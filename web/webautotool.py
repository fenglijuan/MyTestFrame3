from selenium.webdriver import *
import os,traceback
import time
from selenium.webdriver.common.action_chains import ActionChains
class  Broswer:
    def __init__(self,writer):
        self.writer=writer
        #保存打开的浏览器
        self.driver=None
        self.text=''
        self.title=''
        self.jsres=''
    #定义打开浏览器的函数
    def openbroswer(self,type='chrome',dir=None):
        if type=='chrome' or type=='':
            if dir==None or dir=='':
                dir='web/lib/chromedriver.exe'
            option=ChromeOptions()
            option.add_argument('disable-infobars')
            userdir=os.environ['USERPROFILE']+'\\AppData\\Local\\Google\\Chrome\\User Data'
            option.add_argument('--user-data-dir='+userdir)
            self.driver=Chrome(executable_path=dir,options=option)
            self.writer.write(self.writer.row,7,'pass')
            self.writer.write(self.writer.row, 8, '')
        elif type=='ie':
            if dir==None:
                dir='lib/IEDriverServer.exe'
            self.driver=Ie(executable_path=dir)
            self.writer.write(self.writer.row,7,'pass')
            self.writer.write(self.writer.row, 8, '')
        elif type=='firefox':
            if dir==None:
                dir='lib/geckodriver.exe'
            self.driver=Firefox(executable_path=dir)
            self.writer.write(self.writer.row,7,'pass')
            self.writer.write(self.writer.row, 8, '')
        else:
            print('该种浏览器没有实现')
            self.writer.write(self.writer.row,7,'fail')
            self.writer.write(self.writer.row, 8, '该种浏览器没有实现')

    def geturl(self,url):
        try:
            self.driver.get(url)
            self.writer.write(self.writer.row, 7, 'pass')
            self.writer.write(self.writer.row, 8, url)
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
    def click(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def input(self,xpath,value):
        self.driver.find_element_by_xpath(xpath).send_keys(str(value))
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def intoiframe(self, xpath):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def outiframe(self):
        self.driver.switch_to.default_content()
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def quite(self):
        self.driver.quit()
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def sleep(self,t=3):
        time.sleep(int(t))
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def gettext(self,xpath):
        self.text=self.driver.find_element_by_xpath(xpath).text
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def gettitle(self):
        self.title=self.driver.title
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def switchwindow(self,idx=0):
        print(self.driver.window_handles)
        h=self.driver.window_handles
        self.driver.switch_to.window(h[int(idx)])
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def closewindow(self):
        self.driver.close()
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def moveto(self,xapth):
        actions=ActionChains(self.driver)
        ele=self.driver.find_element_by_xpath(xapth)
        actions.move_to_element(ele).perform()
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def excutejs(self,js):
        self.jsres=self.driver.execute_script(js)
        self.writer.write(self.writer.row, 7, 'pass')
        self.writer.write(self.writer.row, 8, '')

    def assertequals(self,p,value):
        try:
            p=p.replace('{text}',self.text)
            p = p.replace('{jsres}', self.jsres)
            p = p.replace('{title}', self.title)
            if str(p)==str(value):
                self.writer.write(self.writer.row, 7, 'pass')
                self.writer.write(self.writer.row, 8, '')
            else:
                self.writer.write(self.writer.row, 7, 'fail')
                self.writer.write(self.writer.row, 8, str(p))
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))





