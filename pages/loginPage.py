# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/8 
Desc：
'''
from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from pages.profilePage import ProfilePage


class LoginPage(BasePage):
    _close_locator = (By.ID, "iv_action_back")  # 取消按钮
    _login_user = (By.ID, "login_account")  # 已注册账号
    _login_password = (By.ID, "login_password")  # 已注册账号密码
    _login_button = (By.ID, "button_next")  # 登录按钮
    _login_without_password = (By.ID, "login_without_password")  # 验证码快捷登录 界面文本
    _login_outside = (By.ID, "login_outside")  # 海外手机登录 界面文本
    _register_phone_number = (By.ID, "register_phone_number")  # 手机号
    _register_code = (By.ID, "register_code")  # 验证码
    _login_more = (By.ID, "login_more")  # 邮箱手机号密码登录 界面文本
    _weixin_login = (By.ID, "weixin_login")  # 微信登录
    _sina_login = (By.ID, "sina_login")  # 微博登录
    _tencent_login = (By.ID, "tencent_login")  # QQ登录
    _error_msg = (By.ID, "md_content")  # 验证码已过期 或者 用户名或密码错误  弹窗内容
    _md_buttonDefaultPositive = (By.ID, "md_buttonDefaultPositive")  # 确定 弹窗内容

    def loginByWx(self):
        return self

    def loginByMSG(self, photo, code):
        return self

    def loginByPassword(self, account, password):
        self.find(self._login_user).send_keys(account)
        self.find(self._login_password).send_keys(password)
        self.find(self._login_button).click()
        return self

    def loginSuccessByPassword(self, account, password):
        return self

    def loginByWeibo(self):
        return self

    def loginByQQ(self):
        return self

    def back(self):
        # todo:
        # 显示等待的逻辑：等待2秒,直到某个元素出现
        #WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_all_elements_located(self._close_locator))
        self.find(self._close_locator).click()
        return ProfilePage()

    def getErrorMsg(self):
        msg = self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg