# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/6 
Desc：
'''
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    _locator_edit = (By.CLASS_NAME, "android.widget.EditText")

    # return self 是为了链式调用，可供其他使用
    def search(self, key):
        self.find(self._locator_edit).send_keys(key)
        self.driver.keyevent(66)
        return self

    def addToSelected(self, key):
        self.find(key).click()
        return self

    def isInSelected(self, key):
        # 先定位元素
        # 获取属性
        # 判断是否在获取的属性中
        follow_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and @text = '%s']/../../..//*[contains(@resource-id, 'follow')]" % key)
        id = self.find(follow_button).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id
