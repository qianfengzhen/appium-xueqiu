# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/11 
Desc：
'''
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):

    def __init__(self, driver):
        self.driver: WebDriver = driver

