# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["deviceName"] = "62b614de"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = ".activity.SplashActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)
#登录界面
el7 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el7.send_keys("871080118")
el8 = driver.find_element_by_accessibility_id("密码 安全")
el8.send_keys("1111aaaa")
el9 = driver.find_element_by_accessibility_id("登 录")
el9.click()
#设置界面
el10 = driver.find_element_by_id("com.tencent.mobileqq:id/ws")
el10.click()
el11 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout")
el11.click()
el12 = driver.find_element_by_id("com.tencent.mobileqq:id/iqb")
el12.click()
el13 = driver.find_element_by_id("com.tencent.mobileqq:id/account_switch")
el13.click()
el14 = driver.find_element_by_accessibility_id("退出当前帐号按钮")
el14.click()
el15 = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
el15.click()

driver.quit()