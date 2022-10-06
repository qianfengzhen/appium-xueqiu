# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/3 
Desc：
'''

from appium.webdriver.webdriver import WebDriver
from appium import webdriver


class AndroidClient(object):
    driver: WebDriver  #偷懒，保存为当前类变量 ；实际应该有一个全局变量保存

    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {
            "platformName": "Android",
            "platformVersion": "7.1",
            "deviceName": "meitu",
            "appActivity": ".view.WelcomeActivityAlias",
            "appPackage": "com.xueqiu.android",
            "autoGrantPermissions": "true",  #解决第一次启动弹窗权限的问题
            "noReset": "true"
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {
            "platformName": "Android",
            "platformVersion": "7.1",
            "deviceName": "meitu",
            "appActivity": ".view.WelcomeActivityAlias",
            "appPackage": "com.xueqiu.android",
            # "unicodeKeyboard": "true",
            # "resetKeyboard": "true",
            "noReset": "true"
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

