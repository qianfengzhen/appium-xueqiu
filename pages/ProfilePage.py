# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/7 
Desc：
'''

from pages.BasePage import BasePage
from pages.loginPage import LoginPage

class ProfilePage(BasePage):
    def gotoLogin(self):
        self.laodSteps("../data/ProfilePage.yaml", "gotoLogin")
        return LoginPage()
