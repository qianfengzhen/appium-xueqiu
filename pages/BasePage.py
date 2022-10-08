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

from driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        # todo:处理各类弹窗
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" % text))

    def laodSteps(self, po_path, key, **kwargs):
        file = open(po_path, encoding='UTF-8').read()
        po_data = yaml.safe_load(file)
        po_method = po_data[key]
        for step in po_method:
            element = self.driver.find_element(by=step['by'], value=step['locator'])
            action = str(step['action']).lower()

            #todo:定位失败，多数是弹框，try catch后进入一个弹框处理
            if action == "click":
                element.click()
            elif action == "send_keys":
                text = str(step['text'])
                for k, v in kwargs.items():
                    text = text.replace("$%s" %k, v)
                    print(text)
                element.send_keys(text)
            else:
                print("unknown commod %s" % step)
