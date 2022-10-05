# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
import time

from selenium.webdriver.common.by import By

from driver.AndroidClient import AndroidClient
from pages.BasePage import BasePage
from pages.MarkingPage import MarkingPage
from pages.SelectedPage import SelectedPage


class MainPage(BasePage):
    #完成driver初始化
    #完成页面点击
    #完成页面选择

    #点击行情后跳转到行情自选页面
    def gotoSelected(self):
        #调用全局变量driver查找 元素
        hangqing = (By.XPATH, "//*[@text='行情']")
        self.find(hangqing)
        self.driver.implicitly_wait(10)
        self.find(hangqing).click()
        return SelectedPage()

    def gotoMarking(self):
        #调用全局变量driver查找 元素
        self.driver.find_element_by_xpath('//*[@text="行情"]')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@text="行情"]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@text="市场"]')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@text="市场"]').click()
        return MarkingPage()
