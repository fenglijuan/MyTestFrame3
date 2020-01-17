from web.webautotool import Broswer
import time
#启动浏览器
driver=Broswer()
driver.openbroswer()
driver.geturl('http://www.testingedu.com.cn:8000/')

#登录页面
def login(driver):
    driver.click('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
    driver.input('//*[@id="username"]','13800138006')
    driver.input('//*[@id="password"]', '123456')
    driver.input('//*[@id="verify_code"]','11111')
    driver.click('//*[@id="loginform"]/div/div[6]/a')
    time.sleep(10)
    driver.gettext('/html/body/div[1]/div/div/div/div[2]/a[2]')
    if driver.text=='安全退出':
        print('pass')
    else:
        print('fail')

#个人中心
def userinfo(driver):
    driver.click('/html/body/div[3]/div/div[2]/div[1]/div/ul[4]/li[2]/a')
    driver.click('//*[@id="preview"]')
    #driver.input('//*[@id="rt_rt_1dugu4bbasuh7et1lnp1uch1int1"]/label','')
    driver.intoiframe('//*[@id="layui-layer-iframe1"]')
    driver.input('//*[@id="filePicker"]/div[2]/input','C:\\Users\\test\Desktop\\flj私人文件夹\\临时头像.PNG')
    driver.outiframe()
    driver.click('//*[@id="layui-layer1"]/span[1]/a[3]')
    driver.click('/html/body/div[1]/div/div/ul/li[5]/a')
    driver.switchwindow(1)
    driver.gettitle()
    print(driver.title)
    driver.closewindow()
    driver.switchwindow(0)

def search(driver):
    driver.input('//*[@id="q"]','手机')
    driver.click('//*[@id="sourch_form"]/a')
    driver.moveto('/html/body/div[4]/div/div[2]/div[2]/ul/li[10]/div/div[2]/div/ul/li[3]/a/img')
    driver.click('/html/body/div[4]/div/div[2]/div[2]/ul/li[10]/div/div[5]/div[2]/a')
    time.sleep(3)
    driver.click('//*[@id="layui-layer1"]/span/a')
    driver.excutejs('window.scrollBy(0,800)')
    driver.excutejs('return window.HTMLTitleElement.name')
    print(driver.jsres)

def cart(driver):
    driver.click('//*[@id="hd-my-cart"]/a/div/span')
    driver.click('/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]/a')

def order(driver):
    time.sleep(3)
    driver.click('/html/body/div[14]/div/button')
    time.sleep(3)
login(driver)
#userinfo(driver)
search(driver)
cart(driver)
order(driver)

time.sleep(3)
driver.quite()
