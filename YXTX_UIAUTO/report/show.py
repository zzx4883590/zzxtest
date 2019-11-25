# coding=utf-8

from appium import webdriver

desired_caps = {

                'platformName': 'Android',
                'deviceName': '50e7e65f',
                'platformVersion': '9',
                # apk包名
                'appPackage': 'io.dcloud.H5A6DF4A7',
                # apk的launcherActivity
                'appActivity': 'io.dcloud.PandoraEntryActivity'

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)