# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/6 
Desc：
'''
import time

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
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text = '%s']/../../..//*[contains(@resource-id, 'follow_btn')]" % key)
        self.find(follow_button).click()
        return self

    def removeFromSelected(self, key):
        followed_button = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text = '%s']/../../..//*[contains(@resource-id, 'followed_btn')]" % key)
        self.find(followed_button).click()
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

    def cancel(self):
        self.findByText("取消").click()

    def searchByUser(self, key):
        locator_user = (By.XPATH, "//*[contains(@resource-id,'title_text') and @text = '用户']")
        self.find(self._locator_edit).send_keys(key)
        self.driver.keyevent(66)
        time.sleep(3)
        self.find(locator_user).click()
        return self

    def isFollowed(self, key):
        follow_button = (By.XPATH, "//*[contains(@resource-id, 'user_name') and @text = '%s']/../..//*[contains(@resource-id, 'follow')]" %key)
        id = self.find(follow_button).get_attribute("resourceId")
        return "followed_btn" in id


