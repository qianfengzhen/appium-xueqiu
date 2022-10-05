# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
from pages.App import App
from pages.BasePage import BasePage
from pages.MainPage import MainPage

class TestSelected(object):

    def test_price(self):
        print(App.main().gotoSelected().getPriceByName("瑞士信贷"))
        assert App.main().gotoSelected().getPriceByName("瑞士信贷") >= 4.0


    def test_price_marking(self):
        assert App.main().gotoMarking().getszdata("深证成指") >= 10000