"""
从配置文件获取相关的app测试配置信息
"""
from appium import webdriver
# from config.config import *
from common.log import logger
import time
from common.base import Base


# 道路客运-壹行天下app 安卓
@logger('开始从配置文件中获取测试相关的配置')
def road_transport():
    desired_caps = {
                    'platformName': 'Android',
                    'platformVersion': '9',
                    'deviceName': '50e7e65f',
                    'noReset': True,
                    'automationName': 'uiautomator2',
                    # 'ANDROID_UIAUTOMATOR':'uiautomator2',
                    'appPackage': 'io.dcloud.H5A6DF4A7',
                    'appActivity': 'io.dcloud.PandoraEntryActivity',
                    'androidDeviceReadyTimeout': 20,
                    'recreateChromeDriverSessions': True,
                    'unicodeKeyboard': True,
                    'sessionOverride': True,
                    'resetKeyboard': True}
    return desired_caps
# #
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', road_transport())
# # contexts=driver.contexts
# # for cotext in contexts:
# #     print (cotext)
# # # driver.switch_to.context("WEBVIEW")
# # a = driver.find_elements_by_xpath("//android.view.View[@index='0']")
# # print(a)
# h =Base(driver)
# h.tap(407, 2241, 0)
# time.sleep(6)
# h.send_keys('xpath', '//android.widget.EditText[@index="1"]', 0, '13269361468')
# h.send_keys('xpath', '//android.widget.EditText[@index="1"]', 1, 'zzx910129')
# h.click_element('xpath', '//android.view.View[@text="登 录"]')
# # h.click_elements('id', 'bottomBar', 2)
# time.sleep(20)

# h.click_element('xpath', '//android.view.View[@text="出发城市"]')
# time.sleep(2)
# h.click_element('xpath', '//*[@text="唐山市"]')
# # time.sleep(2)
# h.click_element('id', 'arrSearchCity')
# time.sleep(2)
# driver.find_element_by_id('arrSearchCity').sendkeys('北京市')
# driver.find_element_by_xpath('//android.view.View[@text="我的"]').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
# driver.find_element_by_name('我的').click()


# class AppiumTest:
#     def __init__(self):
#         desired_caps = {}
#         desired_caps['platformName'] = Testplatform
#         desired_caps['platformVersion'] = TestplatformVersion
#         desired_caps['deviceName'] = Testdevicesname
#         desired_caps['appPackage'] = TestappPackage
#         desired_caps['automationName'] = TestuiAuto
#         desired_caps['appActivity'] = TestappActivity
#         desired_caps['androidDeviceReadyTimeout'] = TestandroidDeviceReadyTimeout
#         desired_caps['unicodeKeyboard'] = TestunicodeKeyboard
#         desired_caps['resetKeyboard'] = TestresetKeyboard
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         self.driver.implicitly_wait(30)
#
#     def get_driver(self):
#         return self.driver