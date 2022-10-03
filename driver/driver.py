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


class Client(object):
    driver: WebDriver

    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {
            "platformName": "Android",
            "platformVersion": "7.1",
            "deviceName": "meitu",
            "appActivity": "com.hotbitmapgg.bilibili.module.common.LoginActivity t6057",
            "appPackage": "com.hotbitmapgg.ohmybilibili",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true",
            "noReset": "true"
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        pass

