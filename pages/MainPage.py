# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
import time

from selenium.webdriver.common.by import By

from driver.AndroidClient import AndroidClient
from pages.BasePage import BasePage
from pages.MarkingPage import MarkingPage
from pages.SearchPage import SearchPage
from pages.SelectedPage import SelectedPage


class MainPage(BasePage):
    #完成driver初始化
    #完成页面点击
    #完成页面选择

    #点击行情后跳转到行情自选页面
    def gotoSelected(self):
        #调用全局变量driver查找 元素
        hangqing = "行情"
        self.findByText(hangqing)
        self.driver.implicitly_wait(10)
        self.findByText(hangqing).click()
        return SelectedPage()

    def gotoMarking(self):
        #调用全局变量driver查找 元素
        text = "行情"
        self.findByText(text)
        self.driver.implicitly_wait(10)
        self.findByText(text).click()
        self.driver.implicitly_wait(5)
        text_two = "市场"
        self.findByText(text_two)
        self.driver.implicitly_wait(10)
        self.findByText(text_two).click()
        return MarkingPage()

    def gotoSearch(self):
        search_button = (By.ID, "com.xueqiu.android:id/tv_search")
        self.find(search_button).click()
        return SearchPage()

