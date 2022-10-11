# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/11 
Desc：
'''
from web.pageobject.page.BasePage import BasePage
from web.pageobject.page.SearchPage import SearchPage


class MainPage(BasePage):

    def search(self, keyword):
        self.driver.find_element_by_css_selector('.Header_nav__search_1YZ  input').send_keys(keyword)
        self.driver.find_element_by_xpath("//*[@type='button']").click()
        return SearchPage(self.driver)

