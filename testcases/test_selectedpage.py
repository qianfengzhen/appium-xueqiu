# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
from pages.MainPage import MainPage


class TestSelected(object):

    def test_price(self):
        main = MainPage()
        assert main.gotoSelected().getPriceByName("瑞士信贷") == 4.49