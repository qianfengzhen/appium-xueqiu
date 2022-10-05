# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/6 
Desc：
'''
from selenium.webdriver.remote.webelement import WebElement

from driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
       return self.driver.find_element(*kv)
