# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/6 
Desc：
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        #todo:处理各类弹窗
       return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find(By.XPATH, "//*[@text='%s']" %text)
