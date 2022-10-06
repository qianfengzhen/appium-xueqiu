# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
import time

from pages.App import App
from pages.BasePage import BasePage
from pages.MainPage import MainPage

class TestSelected(object):

    #case:测试自选股票的价格
    def test_price(self):
        print(App.main().gotoSelected().getPriceByName("瑞士信贷"))
        assert App.main().gotoSelected().getPriceByName("瑞士信贷") >= 4.0

    #case:测试深证成指的最新价格 fail
    def test_price_marking(self):
        #todo:待调试
        assert App.main().gotoMarking().getszdata("深证成指") >= 10000

    #case:输入的股票是否已添加自选
    def test_is_selected_stock(self):
        searchPage = App.main().gotoSearch().search("阿里巴巴")
        time.sleep(3)
        assert searchPage.isInSelected("BABA") == False
        # assert searchPage.isInSelected("01688") == False

    #case:输入的用户是否已被关注
    def test_is_selected_user(self):
        searchPage = App.main().gotoSearch().searchByUser("seveniruby")
        time.sleep(3)
        assert searchPage.isFollowed("seveniruby") == False
