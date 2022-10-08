# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/7 
Desc：
'''

from pages.basePage import BasePage
# from pages.mainPage import MainPage
from pages.loginPage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        self.findByText("登录雪球").click()
        return LoginPage()
