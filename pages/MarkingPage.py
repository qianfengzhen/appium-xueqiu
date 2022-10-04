# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/5 
Desc：
'''
from driver.AndroidClient import AndroidClient
from pages.MainPage import MainPage


class MarkingPage:

    def getszdata(self, name):
        change_price = AndroidClient.driver.\
            find_element_by_xpath("//*[contains(@resource-id, 'index_name') and @text='"+name+"')]"
            +"/..//*[contains(@resource-id, 'index_price')]").text
        return change_price
