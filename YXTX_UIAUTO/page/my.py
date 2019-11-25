# coding:utf-8
from appium import webdriver
from common.base import Base
import time


class My(Base):  # 我的
    def mine(self):
        """我的"""
        self.click_element("xpath", "//android.view.View[@text=' 我的']")

    def travels(self):
        """点击行程"""
        self.click_element("xpath", "//android.view.View[@text=' 行程']")

    def settings(self):
        """账号设置"""
        self.click_element("xpath", "//*[@resource-id='loginOrRegister']")

    def collect(self):
        """我的收藏点击"""
        self.click_element('xpath', '//android.view.View[@text="我的收藏"]')

    def passenger(self):
        """常用乘客管理"""
        self.click_element('xpath', '//android.view.View[@text="常用乘客管理"]')
        self.click_element("xpath", "//*[@resource-id='addPassenger']")  # 添加乘客
        self.send_key("xpath", "//*[@resource-id='passName']", "测试乘客")
        self.send_key("xpath", "//*[@resource-id='passIDNum']", "450311197509085264")
        self.send_key("xpath", "//*[@resource-id='passPhone']", "13269361468")
        self.click_element("xpath", "//*[@resource-id='save']")  # 保存
        time.sleep(2)
        self.click_element("xpath", "//android.view.View[@text='测试乘客']")   # 删除乘客
        self.click_element("xpath", "//android.view.View[@text='删除']")
        self.click_element("xpath", "//android.widget.Button[@text='确认']")
        time.sleep(2)
        self.click_element("xpath", "//android.view.View[@text='武大']")   # 修改乘客信息
        self.click_element("xpath", "//android.view.View[@text='保存']")

    def coupon(self):
        """优惠券点击"""
        self.click_element('xpath', '//android.view.View[@text="优惠券"]')

    def help(self):
        """帮助中心"""
        self.click_element('xpath', '//android.view.View[@text="帮助中心"]')
        time.sleep(2)

    def feedback(self):
        """意见反馈"""
        self.click_element('xpath', '//android.view.View[@text="意见反馈"]')
        self.send_key("xpath", "//android.widget.EditText[@index='0']", "测试反馈1234567")
        self.click_element("xpath", "//android.view.View[@text='提 交']")

    def aboutus(self):
        """关于我们"""
        self.click_element('xpath', '//android.view.View[@text="关于我们"]')
        time.sleep(2)

    def information(self):
        """个人信息"""
        self.click_element('xpath', '//android.view.View[@text="个人信息"]')
        time.sleep(2)

    def headsculpture(self):
        """更改头像"""
        self.click_element("xpath", "//*[@resource-id='headimg']")
        self.click_element("xpath", "//android.view.View[@index='0']")
        self.click_element("xpath", "//*[@resource-id='confirm']")   # 确定

    def usename(self):
        """修改用户名"""
        self.click_element("xpath", "//*[@resource-id='loginNameValue']")
        self.send_key("xpath", "//android.widget.EditText[@index='0']", "测试用户名")
        self.click_element("xpath", "//*[@resource-id='confirm']")   # 确定

    def name(self):
        """修改姓名"""
        self.click_element("xpath", "//*[@resource-id='userNameValue']")
        time.sleep(2)
        self.send_key("xpath", "//android.widget.EditText[@index='0']", "测试姓名")
        time.sleep(2)
        self.click_element("xpath", "//*[@resource-id='confirm']")   # 确定
        time.sleep(1)

    def sex(self):
        """修改性别"""
        self.click_element("xpath", "//*[@resource-id='userGenderValue']")   # 选择性别
        self.click_element('xpath', '//android.widget.TextView[@text="男"]')
        time.sleep(2)

    def birthday(self):
        """修改出生日期"""
        self.click_element("xpath", "//*[@resource-id='userBirthdayValue']")
        time.sleep(2)
        self.click_elements("xpath", "//android.view.View[@index='1']", 0)
        self.click_element("xpath", "//android.widget.Button[@text='确定']")
        time.sleep(2)

    def documenttype(self):
        """证件类型选择"""
        self.click_element("xpath", "//*[@resource-id='idTypeValue']")
        time.sleep(2)
        self.click_element("xpath", "//android.widget.TextView[@text='身份证']")

    def certificate(self):
        """修改证件号"""
        self.click_element("xpath", "//*[@resource-id='idNoValue']")
        time.sleep(2)
        self.send_key("xpath", "//android.widget.EditText[@index='0']", "450311197509088609")
        time.sleep(2)
        self.click_element("xpath", "//android.view.View[@text='确定']")

    def  newpassenger(self):
        """新增乘客"""
        self.click_element("xpath", "//*[@resource-id='addPassenger']")  # 添加乘客
        self.send_key("xpath", "//*[@resource-id='passName']", "测试乘客")
        self.send_key("xpath", "//*[@resource-id='passIDNum']", "450311197509085264")
        self.send_key("xpath", "//*[@resource-id='passPhone']", "13269361468")
        self.click_element("xpath", "//android.view.View[@text='保存']")

    def delpassenger(self):
        """删除乘客"""
        self.click_element("xpath", "//android.view.View[@text='测试乘客']")
        self.click_element("xpath", "//android.view.View[@text='删除']")
        self.click_element("xpath", "//android.widget.Button[@text='确认']")
        time.sleep(2)

    def modifypasssenger(self):
        """修改乘客信息"""
        self.click_element("xpath", "//android.view.View[@text='武大']")
        self.click_element("xpath", "//android.view.View[@text='保存']")
        time.sleep(2)

    def safecenter(self):
        """安全中心-修改密码"""
        self.click_elements("xpath", "//android.view.View[@text='安全中心']", 0)   # 进入安全中心
        self.click_element("xpath", "//android.view.View[@text='修改密码']")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@resource-id='psw']").send_keys("zzx910129")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@resource-id='newPsw']").send_keys("zzx910129")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@resource-id='confirmPsw']").send_keys("zzx910129")
        time.sleep(2)
        self.click_element("xpath", "//android.view.View[@text='确认']")

