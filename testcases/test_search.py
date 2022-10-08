# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
import time
import pytest

from pages.App import App
# from pages.mainPage import MainPage


class TestSelected(object):

    # 只执行一次
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    # 每次用例前执行一次
    def setup_method(self):
        # self.mainPage: MainPage = TestSelected.mainPage
        self.searchPage = self.mainPage.gotoSearch()  # 为了配合数据驱动做的演示

    # case:输入的股票是否已添加自选
    def test_is_selected_stock(self):
        self.searchPage.search("阿里巴巴")
        time.sleep(3)
        assert self.searchPage.isInSelected("BABA") == False

    # case:输入的用户是否已被关注
    def test_is_selected_user(self):
        self.searchPage.searchByUser("seveniruby")
        time.sleep(3)
        assert self.searchPage.isFollowed("seveniruby") == False

    @pytest.mark.parametrize("key,code",
                             [("招商银行", "SH600036"), ("平安银行", "SZ000001"), ("pingan", "SH601318"), ("视源股份", "SZ002841")])
    def test_is_selected_stock_hs(self, key, code):
        self.searchPage.search(key)
        assert self.searchPage.isInSelected(code) == False

    def test_add_stock(self):
        key = "招商银行"
        code = "SH600036"
        search_page = self.searchPage.search(key)
        if search_page.isInSelected(code) == True:
            search_page.removeFromSelected(code)

        search_page.addToSelected(code)
        assert search_page.isInSelected(code) == True

    def teardown_method(self):
        self.searchPage.cancel()  # 配合数据驱动的关闭
