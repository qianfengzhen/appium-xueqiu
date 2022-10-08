# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@qq.com
Version: V1.0.0
Date: 2022/10/8 
Desc：
'''

import yaml

from driver.AndroidClient import AndroidClient


class TestYaml(object):

    def test_yaml(self):
        dict = yaml.safe_load(open("../data/LoginPage.yaml", 'r', encoding="utf-8"))
        print(dict)
        print(dict['loginByPassword'][0])
        for step in dict:
            print(dict[step])


    def test_laodSteps(self):
        po_path = "../data/LoginPage.yaml"
        key = "loginByPassword"
        file = open(po_path, encoding='UTF-8').read()
        po_data = yaml.safe_load(file)
        po_method = po_data[key]
        print(po_method)
        for step in po_method:
            print(step['by'])
            print(step['locator'])
            action = str(step['action']).lower()
            print(action)
            if action == "click":
                print("click")
            elif action == "send_keys":
                print("send_keys(step['text'])")
            else:
                print("unknown commod %s" % step)
