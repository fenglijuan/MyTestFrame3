#-*- coding:UTF-8 -*-
from appium import webdriver
from common import logger
import traceback,os,time,threading

class APP:

    def __init__(self,writer):
        self.driver=None
        self.t=20
        self.writer=writer
        self.port='4723'

    def runappium(self,path='',port='',t=''):
        '''
        启动appium服务
        :param path:appium的安装路径
        :param port:服务的启动端口
        :param t:等待时间
        :return:
        '''
        try:
            if path=='':
                cmd='node D:\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            else:
                cmd = 'node '+path+'\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            if port=='':
                cmd += ' -p 4723'
            else:
                self.port = port
                cmd+=' -p '+port
            if t=='':
                t=5
            else:
                t=int(t)
            #启动appium服务
            def run(cmd):
                print(cmd)
                try:
                    os.popen(cmd).read()
                except Exception  as e:
                    pass
            th=threading.Thread(target=run,args=(cmd,))
            th.start()
            time.sleep(t)
            self.writer.write(self.writer.row, 7, 'pass')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    def runapp(self,conf,t='20'):
        '''
        连接appuim服务器，并根据conf配置，启动待测试app
        :param conf:app的启动配置，为标准json字符串
        :param t:
        :return:
        '''
        try:
            conf=eval(conf)
            if t=='':
                t=20
            else:
                t=int(t)
            self.t=t
            self.driver = webdriver.Remote('http://localhost:'+self.port+'/wd/hub', conf)
            self.driver.implicitly_wait(t)
            self.writer.write(self.writer.row,7,'pass')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row,7,'fail')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def _findele(self,path):
        try:
            ele=None
            if path.startswith('/'):
                ele=self.driver.find_element_by_xpath(path)
            # elif path.find('id/')>=0
            else:
                try:
                    self.driver.implicitly_wait(5)
                    ele=self.driver.find_element_by_accessibility_id(path)
                except Exception as e:
                    self.driver.implicitly_wait(self.t)
                    ele=self.driver.find_element_by_id(path)
            self.writer.write(self.writer.row, 7, 'pass')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
        return ele

    def click(self,path):
            ele=self._findele(path)
            if ele is None:
                logger.error('no such element:'+path)
                self.writer.write(self.writer.row, 7, 'fail')
            else:
                try:
                    ele.click()
                    self.writer.write(self.writer.row, 7, 'pass')
                except Exception as e:
                    self.writer.write(self.writer.row, 7, 'fail')
                    self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    def clear(self,path):
            ele=self._findele(path)
            if ele is None:
                logger.error('no such element:'+path)
            else:
                try:
                    ele.clear()
                    self.writer.write(self.writer.row, 7, 'pass')
                except Exception as e:
                    self.writer.write(self.writer.row, 7, 'fail')
                    self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    def input(self,path,text):
        ele=self._findele(path)
        if ele is None:
            logger.error('no such element:'+path)
        else:
            try:
                ele.send_keys(text)
                self.writer.write(self.writer.row, 7, 'pass')
            except Exception as e:
                self.writer.write(self.writer.row, 7, 'fail')
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
    def closeappuim(self):
        try:
            os.popen('taskkill /F /IM node.exe')
            self.writer.write(self.writer.row, 7, 'pass')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def quit(self):
        try:
            self.driver.quit()
            self.writer.write(self.writer.row, 7, 'pass')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'fail')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
