# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/10/6 
Desc：
'''
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from driver.Client import AndroidClient
import re


class BasePage(object):
    element_black = [(By.XPATH, "ddd")]  # 黑名单标记

    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        # todo:处理各类弹窗
        return self.driver.find_element(*kv)

    def finds(self, by, value):
        element: WebElement
        # 加上重试机制

        for i in range(3):
            try:
                element = self.driver.find_element(by, value)
                return element
            except:
                # 找到页面的最顶层的元素进行点击
                # 动态变化位置的元素
                # self.driver.page_source
                # get_maxdepth_element.click()

                # 黑名单
                ##//*[@text='弹窗']/..///*[@text = '确认']
                for e in BasePage.element_black:
                    elements = self.driver.find_element(*e)
                    if (elements.__sizeof__() > 0):
                        elements[0].click()

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" % text))

    def laodSteps(self, po_path, key, **kwargs):
        file = open(po_path, encoding='UTF-8').read()
        po_data = yaml.safe_load(file)
        po_method = po_data[key]
        po_elements = dict()
        if po_data.keys().__contains__("elements"):
            po_elements = po_data['elements']
        # po_elements从外部文件读取  =yaml.safe_load(file)

        for step in po_method:
            step: dict
            if step.keys().__contains__("element"):
                element_platform = po_elements[step['element']][AndroidClient.platform]
            else:
                element_platform = {"by": step['by'], "locator": step['locator']}
            element = self.driver.find_element(by=element_platform['by'], value=element_platform['locator'])
            action = str(step['action']).lower()

            # todo:定位失败，多数是弹框，try catch后进入一个弹框处理
            if action == "click":
                element.click()
            elif action == "send_keys":
                text = str(step['text'])
                for k, v in kwargs.items():
                    text = text.replace("$%s" % k, v)
                    print(text)
                element.send_keys(text)
            else:
                print("unknown commod %s" % step)
