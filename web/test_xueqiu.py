# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/10 
Desc：
'''
import json

from selenium import webdriver


class Test_Xueqiu(object):

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")

    def test_search(self):
        #css定位方式--- .name name
        self.driver.find_element_by_css_selector('.Header_nav__search_1YZ  input').click()

        self.driver.find_element_by_css_selector('.Header_nav__search_1YZ  input').send_keys("阿里巴巴")
        # self.driver.find_element_by_tag_name("input").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@type='button']").click()
        # self.driver.find_element_by_xpath("//*[@class='follow__control followed']").click()
        # self.driver.find_element_by_xpath("//*[@name='username']").send_keys("1528039518")
        # self.driver.find_element_by_xpath("//*[@name='password']").send_keys("1528039518")

    def test_window(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    #页面加载时间
    def test_execute_script_time(self):
        raw = self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(raw)
        print(json.dumps(json.loads(raw),indent=4))

    def test_execute(self):
        self.driver.execute()

    def teardown_method(self):
        self.driver.quit()
