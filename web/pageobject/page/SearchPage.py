# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/11 
Desc：
'''
from web.pageobject.page.BasePage import BasePage


class SearchPage(BasePage):

    def follow(self, keyword):
        element = self.driver.find_element_by_xpath('//*[contains(text(),"%s")]/../../../..//*[@class="follow__control followed"]' %keyword)
        element.click()