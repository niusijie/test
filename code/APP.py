from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
    'platformName':'Android', #被测手机就版本
    'platformVersion':'10', #安佐版本
    'deviceName':'xxx', #设备名，苹果有专有设备名但安卓可以随便写
    'appPackage':'tv.danmaku.bili',  #启动APP Package名称
    'appActivity':'.ui.splash.SplashActivity',  #启动Activity名称
    'unicodeKeyboard': True,  #使用自带入输入法，中文时为True
    'resetKeyboard':True,  #执行完毕是否恢复原来输入
    'noReset':True,  #不重置
    'newCommandTimeOut':6000,
    'automationName':'UiAutomator2'
}

# 与app server 通过http请求连接并发送参数
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# 设置等待时间
driver.implicitly_wait(10)

driver.find_element_by_id('expand_search').click()
