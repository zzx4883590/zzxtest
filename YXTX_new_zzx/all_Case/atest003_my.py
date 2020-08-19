# coding:utf-8
import time
import unittest
import warnings
from appium import webdriver
from common.base import Base
from common.config import road_transport
from page.my import My
from page.login import Login


class MyOperaTion(unittest.TestCase):
    """测试我的页面操作"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', road_transport())
        cls.base = Base(cls.driver)
        cls.h = My(cls.driver)
        cls.a = Login(cls.driver)
        b = cls.driver.page_source
        print(b)
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告日志
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print('* * * Start * * *')

    def tearDown(self):
        print('* * * End * * *')

    def test01(self):  # 账号设置
        """测试点击账号设置"""
        try:
            self.h.mine()
            self.h.settings()
            result = self.base.is_element_exist('账号设置')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    # def test02(self):  # 我的收藏
    #     """测试点击我的收藏"""
    #     try:
    #         self.h.collect()
    #         result = self.base.is_element_exist('我的收藏')
    #         self.assertTrue(result)
    #
    #     except Exception as msg:
    #         print('测试Fail,异常原因:', msg)
    #         now_time = time.strftime("%Y%m%d.%H.%M.%S")
    #         self.base.get_screenshot_as_file('%s.png' % now_time)
    #         raise
    #     finally:
    #         self.driver.back()

    def test02(self):  # 常用乘客
        """测试点击常用乘客管理"""
        try:
            self.h.passenger()
            result = self.base.find_toast('修改成功')
            self.assertTrue(result)
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    def test03(self):  # 优惠券
        """测试点击优惠券"""
        try:
            self.h.coupon()
            result = self.base.is_element_exist('优惠券')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    def test04(self):  # 帮助中心
        """测试点击帮助中心"""
        try:
            self.h.help()
            result = self.base.is_element_exist('帮助中心')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    def test05(self):  # 意见反馈
        """测试点击意见反馈"""
        try:
            self.h.feedback()
            result = self.base.is_element_exist('意见反馈')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    def test06(self):  # 关于我们
        """测试点击关于我们"""
        try:
            self.h.aboutus()
            result = self.base.is_element_exist('关于我们')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    def test07(self):
        """个人信息-修改头像"""
        try:
            self.h.settings()   # 进入设置
            self.h.information()   # 进入个人信息
            self.h.headsculpture()    # 修改头像
            result = self.base.is_element_exist('个人信息')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test08(self):
        """个人信息-修改用户名"""
        try:
            self.h.usename()    # 修改用户名
            result = self.base.is_element_exist('测试用户名')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test09(self):
        """个人信息-修改姓名"""
        try:
            self.h.name()    # 修改姓名
            result = self.base.is_element_exist('测试姓名')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test10(self):
        """个人信息-修改性别"""
        try:
            self.h.sex()    # 修改性别
            result = self.base.is_element_exist('男')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test11(self):
        """个人信息-修改出生日期"""
        try:
            self.h.birthday()    # 修改出生日期
            result = self.base.is_element_exist('个人信息')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test12(self):
        """个人信息-修改证件类型"""
        try:
            # self.h.settings()   # 进入我的
            # self.h.information()   # 进入个人信息
            self.h.documenttype()    # 修改证件类型
            result = self.base.is_element_exist('身份证')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise

    def test13(self):
        """个人信息-修改证件号码"""
        try:
            self.h.certificate()    # 修改证件号
            result = self.base.is_element_exist('个人信息')
            self.assertTrue(result)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()

    def test14(self):
        """安全中心-修改相同密码"""
        try:
            # self.h.settings()   # 进入我的
            self.h.safecenter()    # 安全中心
            result = self.base.find_toast('新旧密码一样')
            self.assertTrue(result)
            time.sleep(2)
            self.driver.back()
            time.sleep(2)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.base.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.back()
            time.sleep(2)

    def test15(self):
        """退出登录"""
        try:
            self.driver.back()
            self.a.logout()
            # self.driver.find_element_by_id('com.klgz.smartcampus:id/iv_leader_sel').click()
            time.sleep(2)
            self.assertTrue(self.base.is_element_exist('登录或注册'))
            print('退出成功')
            time.sleep(2)

        except Exception as msg:
            print('测试Fail,异常原因:', msg)
            now_time = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.png' % now_time)
            raise
        finally:
            self.driver.quit()
