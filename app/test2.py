import os,threading
def run():
    res=os.popen('node D:\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js -p 4724').read()
th=threading.Thread(target=run,args=())
th.start()
print(11111)