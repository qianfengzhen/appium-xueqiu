# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''

from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from pages.markingPage import MarkingPage
from pages.profilePage import ProfilePage
from pages.searchPage import SearchPage
from pages.selectedPage import SelectedPage


class MainPage(BasePage):
    # 完成driver初始化
    # 完成页面点击
    # 完成页面选择

    # 行情-自选-页面
    def gotoSelected(self):
        # 调用全局变量driver查找 元素
        hangqing = "行情"
        self.findByText(hangqing)
        self.driver.implicitly_wait(10)
        self.findByText(hangqing).click()
        return SelectedPage()

    # 行情-市场-页面
    def gotoMarking(self):
        # 调用全局变量driver查找 元素
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

    # 首页-搜索框与搜索页面
    def gotoSearch(self):
        search_button = (By.ID, "com.xueqiu.android:id/tv_search")
        self.find(search_button).click()
        return SearchPage()

    # 我的-页面
    def gotoProfile(self):
        profile_button = (By.XPATH, "//*[contains(@resource-id,'tab_name') and @text='我的']")
        self.find(profile_button).click()
        return ProfilePage()
