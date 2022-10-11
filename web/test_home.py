# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/10 
Desc：
'''
from selenium import webdriver

class TestHome(object):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com/")

    def test_mtsc2022(self):
        self.driver.find_element_by_partial_link_text("MTSC").click()
        self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
        # self.driver.find_element_by_css_selector()

        # self.driver.find_element_by_partial_link_text().click()


    def test_cookie(self):
        print(self.driver.get_cookies())
        self.driver.add_cookie([{"name": "a", "value": "b"}])
        print(self.driver.get_cookies())
