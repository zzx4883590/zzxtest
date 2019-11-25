# coding:utf-8
from appium import webdriver
from common.base import Base
import time


class Search(Base):  # 搜索预定
    def passenger(self):
        """客运站查询"""
        # self.click_element("xpath", "//android.view.View[@text=' 预订']")  # 进入预定页面
        # self.tap(822, 593)
        self.click_element('xpath', '//*[@resource-id="search-tab-station-btn"]')
        time.sleep(2)
        self.send_key('xpath', '//android.widget.EditText[@index="1"]', '唐山')
        self.click_element('xpath', '//android.view.View[@text="查询"]')
        self.click_element('xpath', '//android.view.View[@text="唐山东站"]')
        time.sleep(3)

    def deparstaion(self):
        """出发站/到达站选择"""
        # self.click_element('xpath', '//*[@text="汽车票"]')
        self.click_element('xpath', '//*[@resource-id="search-tab-coach-btn"]')
        self.click_element('xpath', '//android.view.View[@text="出发城市"]')
        time.sleep(2)
        self.click_element('xpath', '//*[@text="北京市"]')
        time.sleep(2)
        # self.click_element('xpath', '//android.view.View[@text="A"]')
        # time.sleep(2)
        self.click_element('xpath', '//android.view.View[@text="安国市"]')
        # self.send_key('id', 'arrSearchCity', '北京市')
        time.sleep(2)

    def search(self):
        """查询/日期后一天"""
        self.click_element('xpath', '//android.view.View[@text="查询"]')
        time.sleep(2)
        self.click_element('xpath', '//android.view.View[@text="后一天"]')
        time.sleep(2)
        # self.click_element('xpath', '//*[@resource-id="ticket-result-content"]')
        self.click_element("xpath", "//android.view.View[@text='￥0.1']")
        time.sleep(2)
        # self.click_element('xpath', '//*[@resource-id="ticket-result-content"]')
        self.click_element("xpath", "//android.view.View[@text='￥0.1']")
        time.sleep(2)
        # self.click_element('xpath', '//*[@resource-id="ticket-result-content"]')
        self.click_element("xpath", "//android.view.View[@text='￥0.1']")
        time.sleep(2)

    def schedule(self):
        """订单填写"""
        self.click_element('xpath', '//*[@resource-id="selectPassBtn"]')
        time.sleep(2)
        # a = self.driver.page_source  # 打印页面元素
        # print(a)
        # self.tap(945, 1549, 0)  # 选择乘客
        # time.sleep(2)
        self.click_element("xpath", "//*[@resource-id='showCouponPrice']")  # 选择乘客
        # self.tap(966, 1342, 0)   # 选择确定
        self.click_element('xpath', '//*[@resource-id="confirmPass"]')  # 选择确定
        self.click_element('xpath', '//*[@resource-id="booking"]')  # 选择预定
        self.click_element('xpath', '//android.view.View[@text="确认支付"]')  # 选择支付
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        self.click_element('id', 'android:id/button1')  # 确定离开
        # self.tap(667, 2227, 0)
        time.sleep(3)

    def cancel(self):
        """取消订单"""
        time.sleep(2)
        # print(self.driver.page_source)  # 打印当前页面元素
        # b = self.driver.current_context
        # print(b)
        # time.sleep(2)
        # self.click_element("xpath", "//android.view.View[@text=' 订单']")
        self.click_element('xpath', '//android.view.View[@text="取消订单"]')
        self.click_element('xpath', '//*[@text="确定"]')
        time.sleep(2)

    def details(self):
        """订单详情"""
        self.click_element("xpath", "//android.view.View[@text='订单作废']")
        time.sleep(2)

        # # a = self.driver.page_source
        # # print(a)
        # # b = self.driver.current_context
        # # print(b)
        # self.click_element("xpath", "//android.view.View[@text=' 行程']")

