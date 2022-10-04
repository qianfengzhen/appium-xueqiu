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
from pages.MarkingPage import MarkingPage
from pages.SelectedPage import SelectedPage


class MainPage(object):
    #完成driver初始化
    #完成页面点击
    #完成页面选择

    def __init__(self):
        AndroidClient.restart_app()

    #点击行情后跳转到行情自选页面
    def gotoSelected(self):
        #调用全局变量driver查找 元素
        AndroidClient.driver.find_element_by_xpath('//*[@text="行情"]')
        time.sleep(5)
        AndroidClient.driver.find_element_by_xpath('//*[@text="行情"]').click()
        return SelectedPage()

    def gotoMarking(self):
        #调用全局变量driver查找 元素
        AndroidClient.driver.find_element_by_xpath('//*[@text="行情"]')
        time.sleep(5)
        AndroidClient.driver.find_element_by_xpath('//*[@text="行情"]').click()
        time.sleep(3)
        AndroidClient.driver.find_element_by_xpath('//*[@text="市场"]').click()
        return MarkingPage()
