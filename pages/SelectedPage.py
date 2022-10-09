# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/4 
Desc：
'''
from selenium.webdriver.common.by import By

from driver.Client import AndroidClient
from pages.BasePage import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def getPriceByName(self, name) -> float:
        # price = self.driver.find_element_by_xpath("//*[contains(@resource-id,'stockName') and @text='"+name+"']"+
        #     "/../../../..//*[contains(@resource-id, 'currentPrice')]").text
        priceLocator=(By.XPATH,"//*[contains(@resource-id,'stockName') and @text='%s']/../../../..//*[contains(@resource-id, 'currentPrice')]" %name)
        price = self.find(priceLocator).text
        return float(price)


