# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
import time

from driver.AndroidClient import AndroidClient


class SelectedPage(object):
    def addDefault(self):
        return self

    def gotoMarking(self):
        AndroidClient.driver.find_element_by_xpath("//*[@text='市场']")
        time.sleep(5)
        AndroidClient.driver.find_element_by_xpath("//*[@text='市场']").click()
        return

    def getPriceByName(self, name) -> float:
        price = AndroidClient.driver.find_element_by_xpath("//*[contains(@resource-id,'stockName') and @text='"+name+"']"+
            "/../../../..//*[contains(@resource-id, 'currentPrice')]").text
        return float(price)


