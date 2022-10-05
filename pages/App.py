# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/6 
Desc：
'''
from driver.AndroidClient import AndroidClient
from pages.MainPage import MainPage


class App(object):
    @classmethod
    def main(self):
        AndroidClient.restart_app()
        return MainPage()