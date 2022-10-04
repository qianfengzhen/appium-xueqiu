# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
from driver.AndroidClient import AndroidClient


class SelectedPage(object):
    def addDefault(self):
        return self

    def getPriceByName(self, name) -> float:
        price = AndroidClient.driver.find_element_by_xpath("//*[contains(@resource-id,'stockName') and @text='"+name+"']"+
            "/../../../..//*[contains(@resource-id, 'currentPrice')]").text
        return float(price)

