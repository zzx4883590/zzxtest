# coding:utf-8
import time
import unittest
import warnings
from appium import webdriver
from common.base import Base
from common.config import road_transport
from page.login import Login
from page.order import SearchOrder
import ddt
from common.datas import datas

testdata = datas()
@ddt.ddt
class SearchReservation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print('* * * Start * * *')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', road_transport())
        self.base = Base(self.driver)
        self.n = SearchOrder(self.driver)
        self.a = Login(self.driver)
        # a = cls.driver.page_source
        # print(a)
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告日志
        self.driver.implicitly_wait(20)

    def tearDown(self):
        print('* * * End * * *')
        # self.driver.quit()
        time.sleep(30)

    # 使用ddt方法
    @ddt.data(*testdata)
    def test01(self, testdata):

        """校验车票价格，取消订单"""
        print(f'出发站:{testdata["start"]}-->到达站：{testdata["end"]}')

        try:
            start = testdata["start"]
            end = testdata["end"]
            self.n.isexit_order()
            self.n.deparstaion(start, end)
            amount, serve = self.n.getsum()
            self.n.now_pay()
            self.n.order_context()
            address = self.n.is_adress()
            phone = self.n.is_phone()
            result = self.n.cancal_order()
            self.assertEqual(amount, serve)
            self.assertTrue(address)
            self.assertTrue(phone)
            self.assertTrue(result)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            # 图片名称可以加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.png' % nowTime)
            raise


if __name__ == '__main__':
    unittest.main()
