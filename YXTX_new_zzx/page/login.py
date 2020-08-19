# coding:utf-8
from common.config import road_transport
from appium import webdriver
from common.base import Base
import time


class Login(Base):

    def skip_login(self):

        for i in range(4):
            self.swip_left()
            # 点击立即体验
            self.click_element('xpath', '//*[@resource-id="close"]')
            time.sleep(3)

    def login(self, usname, pwd):
        # 输入用户名，密码，点击登陆
        self.clear_ele("xpath", "//*[@resource-id='username']")
        self.clear_ele("xpath", "//*[@resource-id='password']")
        self.send_key("xpath", "//*[@resource-id='username']", usname)
        self.send_key("xpath", "//*[@resource-id='password']", pwd)
        self.click_element("xpath", "//*[@resource-id='login']")
        time.sleep(2)

    def trips(self):
        """点击行程"""
        b = self.driver.current_context
        print(b)
        a = self.driver.page_source
        print(a)
        # self.click_element("xpath", "//android.view.View[@text=' 行程']")
        xc = '//*[@resource-id="bottomBar"]/android.view.View[2]'     # 定位行程
        self.driver.find_element_by_xpath(xc).click()

    def order(self):
        """点击订单进入登录页面"""
        a = self.driver.page_source
        print(a)
        b = self.driver.current_context
        print(b)
        self.click_element("xpath", "//android.view.View[@text=' 订单']")
        # self.tap(674, 2245, 0)

    def logout(self):
        """退出登录"""
        # self.tap(948, 2248, 0)
        self.click_element('xpath', '//*[@resource-id="head"]')
        self.click_element('xpath', '//*[@resource-id="loginOut"]')

    def allows(self):
        """允许权限"""
        self.always_allow(self.driver, number=5)   # 调用允许方法
        # result = self.driver.page_source
        # print(result)
        time.sleep(2)

if __name__ == '__main__':
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', road_transport())
    h = Login(driver)     # 将class进行实例化
    h.order()
    h.login('13269361468', 'zzx910129')   # 调用test_login函数

