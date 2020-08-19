# coding:utf-8
"""
从配置文件获取相关的app测试配置信息
"""
from common.log import logger
from appium import webdriver


# 道路客运-壹行天下app 安卓
@logger('开始从配置文件中获取测试相关的配置')
def road_transport():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '10',
        'deviceName': '38e3fd24',
        'noReset': True,
        'automationName': 'uiautomator2',
        # 'ANDROID_UIAUTOMATOR':'uiautomator2',
        'appPackage': 'io.dcloud.H5A6DF4A7',  # 测试环境
        'appActivity': 'io.dcloud.H5A6DF4A7.MainActivity',  # 生产环境
        # 'appActivity': 'io.dcloud.PandoraEntry',
        # 'chromeOptions': {'androidProcess': 'com.tencent.mm/.plugin.appbrand.ui.AppBrandUI2'},
        'androidDeviceReadyTimeout': 20,
        'settings[waitForIdleTimeout]': 10,
        'recreateChromeDriverSessions': True,
        'unicodeKeyboard': True,
        'sessionOverride': True,
        'resetKeyboard': True}
    return desired_caps


# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', road_transport())
