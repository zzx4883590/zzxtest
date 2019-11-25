# coding:utf-8
import time
import unittest
import warnings
from appium import webdriver
from common.base import Base
from common.disapp import road_transport
from page.login import Login
from page.search import Search


class SearchReservation(unittest.TestCase):
    """搜索预定测试"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', road_transport())
        cls.base = Base(cls.driver)
        cls.n = Search(cls.driver)
        cls.a = Login(cls.driver)
        # a = cls.driver.page_source
        # print(a)
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告日志
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print('* * * Start * * *')

    def tearDown(self):
        print('* * * End * * *')

    def test01(self):
        """输入客运站查询"""
        try:
            self.n.passenger()
            result = self.base.is_element_exist('开始导航')
            self.assertTrue(result)
            time.sleep(2)
            self.driver.back()

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    def test02(self):
        """输入出发站到达站"""
        try:
            self.n.deparstaion()
            result = self.base.is_element_exist('查询')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test03(self):
        """查询/更改日期"""
        try:
            self.n.search()
            result = self.base.is_element_exist('订单填写')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test04(self):
        """生成订单"""
        try:
            self.n.schedule()
            result = self.base.is_element_exist('查询')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test05(self):
        """取消订单"""
        try:
            self.a.order()
            self.n.cancel()
            result = self.base.is_element_exist('我的订单')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test06(self):
        """订单详情"""
        try:
            self.n.details()
            result = self.base.is_element_exist('再次购买')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.quit()

    # def test07(self):
    #     """点击行程"""
    #     try:
    #         self.base.tap(404, 2234, 0)
    #         time.sleep(9)
    #         self.a.trips()
    #         result = self.base.find_toast('没有查询到用户的行程信息')
    #         self.assertTrue(result)
    #
    #     except Exception as msg:
    #         print('测试Fail,异常原因:', msg)
    #         now_time = time.strftime("%Y%m%d.%H.%M.%S")
    #         self.base.get_screenshot_as_file('%s.png' % now_time)
    #         raise
    #     finally:
    #         self.driver.quit()
