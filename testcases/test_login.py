# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/8 
Desc：
'''
from pages.App import App
import pytest


class TestLogin(object):

    @classmethod
    def setup_class(cls):
        cls.profilePage = App.main().gotoProfile()

    def setup_method(self):
        self.loginPage = self.profilePage.gotoLogin()

    @pytest.mark.parametrize("user, pw, msg",
                             {("139295092340", "11111111", "手机号码"), ("13929509234", "11111111", "用户名")})
    def test_login_password(self, user, pw, msg):
        self.loginPage.loginByPassword(user, pw)
        assert msg in self.loginPage.getErrorMsg()

    def teardown_method(self):
        self.loginPage.back()
