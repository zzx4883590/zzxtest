# coding:utf-8
import time
import unittest
import warnings
from appium import webdriver
from common.base import Base
from common.disapp import road_transport
from page.login import Login


class Loginyxtx(unittest.TestCase):
    """登录页面测试"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', road_transport())
        cls.base = Base(cls.driver)
        cls.a = Login(cls.driver)
        # cls.a.allows()   # 允许权限
        # cls.a.skip_login()  # 跳过滚动页
        # a = cls.driver.page_source
        # print(a)
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告日志

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print('* * * Start * * *')

    def tearDown(self):
        print('* * * End * * *')

    def test01(self):
        """输入错误手机号，密码abc"""
        try:
            self.a.order()
            self.a.login('132693614', 'abc')
            result = self.a.find_toast('输入的登录名格式有误，请重新输入')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test02(self):
        """输入正确手机号，错误密码"""
        try:
            self.a.login('13269361468', 'a123456')
            result = self.a.find_toast('用户密码不匹配，请确认你的用户信息正确无误')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test03(self):
        """登录成功测试"""
        try:
            self.a.login('13269361468', 'zzx910129')
            # a = self.driver.page_source
            # print(a)
            time.sleep(3)
            self.assertTrue(self.base.is_element_exist('我的订单'))
            print('登录成功')

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.png' % now_time)
            raise
        # finally:
        #     self.driver.quit()

    def test04(self):
        """点击行程"""
        try:
            self.a.trips()
            time.sleep(2)
            # a = self.driver.page_source
            # print(a)
            result = self.base.find_toast('没有查询到用户的行程信息')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.quit()
