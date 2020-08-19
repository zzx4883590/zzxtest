# coding:utf-8
from common.base import Base
import time
import logging


# 搜索预订
class SearchOrder(Base):

    # 进入首页后判断是否存在待支付订单
    def isexit_order(self):
        self.driver.implicitly_wait(20)
        try:
            # 点击X关闭弹窗
            click_x = self.driver.find_element_by_xpath(
                "//*[@text='汽车票订单']/../../*[@class='android.view.ViewGroup'][4]")
        except:
            # 不存在时就跳过
            print("不存在'待支付的订单'")
        else:
            print('存在待支付订单——>取消')
            click_x.click()
            # 点击首页的订单按钮
            self.click_element("xpath", "//*[@text='订单']/../../*[@class='android.view.ViewGroup'][3]")
            SearchOrder.order_context(self)
            SearchOrder.cancal_order(self)

            self.click_element("xpath", "//*[@text='再买一单']")

    def deparstaion(self, start, end):
        # 点击出发站
        self.click_element('xpath', "//*[@text='出发城市']/..//*[@class='android.widget.TextView'][2]")
        # 清空输入框
        time.sleep(2)
        self.clear_ele('xpath', '//android.view.ViewGroup[1]/android.widget.EditText')
        time.sleep(2)
        # 输入出发站
        self.send_key('xpath', '//android.widget.EditText[@text="出发站(如北京/beijing/bj)"]', start)
        # 点击第一个选项
        time.sleep(2)
        self.click_element('xpath',
                           '//android.view.ViewGroup[3]/android.widget.ScrollView/android.view.ViewGroup/android.view'
                           '.ViewGroup/android.view.ViewGroup[1]')
        time.sleep(2)
        # 输入到达站
        self.send_key('xpath', '//android.widget.EditText[@text="到达站(如北京/beijing/bj)"]', end)
        # 点击第一个选项
        time.sleep(2)
        self.click_element('xpath',
                           '//android.view.ViewGroup[3]/android.widget.ScrollView/android.view.ViewGroup/android.view'
                           '.ViewGroup/android.view.ViewGroup[1]')
        # 点击汽车票查询
        self.click_element('xpath', '//android.widget.TextView[@text="汽车票查询"]')
        time.sleep(2)
        # 点击明天
        self.click_element('xpath', '//android.widget.TextView[@text="明天"]')
        time.sleep(2)
        # 点击第一趟车
        self.driver.find_element_by_xpath(
            "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup["
            "1]/android.view.ViewGroup/android.view.ViewGroup").click()
        time.sleep(3)

    def getsum(self):
        # 获取票价金额
        a = self.driver.find_element('xpath', '//android.view.ViewGroup[2]/android.widget.TextView[2]').text
        price = a.split("￥")[1]
        # 获取总金额
        c = self.driver.find_element('xpath',
                                     '//android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup/android.widget.TextView[2]').text
        totalamout = c.split("￥")[1]
        # 获取服务费
        try:
            # 如果存在服务费就返回 票价金额+服务费、总金额的值
            b = self.driver.find_element('xpath', '//android.view.ViewGroup[5]/android.widget.TextView[2]').text
            serve = b.split('￥')[1].split('x')[0]
            amount_serve = int(price) + int(serve)
            print('票价为：', price)
            print('服务费为：', serve)
            print('显示总额为：', totalamout)
            print('计算总额为：', amount_serve)
            return amount_serve, int(totalamout)
        except:
            # 如果不存在服务费就返回 票价金额、总金额的值
            print('票价为：', price)
            print('总金额为：', totalamout)
            return int(price), int(totalamout)

    # 立即支付
    def now_pay(self):
        # 点击立即支付#
        self.click_element("xpath", "//*[@text='立即支付']")
        try:
            # 存在不需要按钮时就点击(是否存在保险)
            no_need = self.driver.find_element_by_xpath("//*[@text='不需要']")
            print("该站存在保险")
        except:
            # 不存在时就跳过
            print("该站不存在保险")
        else:
            no_need.click()
            time.sleep(2)
        finally:
            time.sleep(5)
            self.driver.back()

    # 查看订单信息内容
    def order_context(self):
        # 点击订单
        self.click_element("xpath", "//*[@text='立即支付']/../../..")
        # 点击乘客信息的收起按钮
        self.click_element("xpath", "//*[@text='乘客信息']/..//*[contains(@text,'共')]")
        # 点击订单信息的收起按钮
        self.click_element("xpath", "//*[@text='订单信息']/..//*[contains(@text,'总额')]")

    # 判断发车地址
    def is_adress(self):
        try:
            # 如果存在发车地址就执行else
            self.driver.find_element("xpath", "//*[@text='发车地址 :']")
        except:
            # 不存在发车地址返回True
            print("该站点不存在发车地址")
            return True
        else:
            try:
                # 如果存在发车地址就点击地址进入导航页面
                self.click_element("xpath", "//*[@text='发车地址 :']/..//*[@class='android.view.ViewGroup'][1]")
                self.driver.find_element("xpath", "//*[@text='开始导航']")
                time.sleep(2)
                self.driver.back()
                print("地址正常，点击发车地址进入导航页面")
                return True
            except:
                print("存在发车地址，但信息为空")
                return False

    # 判断联系电话
    def is_phone(self):
        try:
            # 如果存在联系电话就返回电话号码
            phone = self.driver.find_element_by_xpath("//*[@text='发车地址 :']/.."
                                                      "//*[@class='android.widget.TextView'][3]").text
            print('联系电话:', phone)
            return self.is_number(phone)
        except:
            # 不存在联系电话
            print('不存在联系电话')
            return True

    # 取消订单
    def cancal_order(self):
        # 点击取消
        self.click_element("xpath", "//*[@text='取消订单']")
        # 点击确定
        self.click_element('xpath', "//*[@resource-id='android:id/button1']")
        # 返回toast
        return self.find_toast("订单取消")
