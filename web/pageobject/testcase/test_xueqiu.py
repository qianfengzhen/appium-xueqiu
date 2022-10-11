# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/11 
Desc：
'''
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.pageobject.page.MainPage import MainPage


class TestXueqiu(object):
    def setup(self):
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")
        self.main = MainPage(self.driver)

    def test_search(self):
        self.main.search("alibaba").follow("09988")
        # self.main.search("alibaba")


    def teardown_method(self):
        time.sleep(4)
        self.driver.quit()
