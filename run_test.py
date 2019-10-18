#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import unittest
# from search_suit import test_isbn
import HTMLTestRunner

test_path = "/Users/liutao/virproject_selenium/testsuit/test_case"

def createsuite():
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(test_path, pattern = "*.py", top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

all_tests_name = createsuite()

now = time.strftime("%Y%m%M%H%M%S",time.localtime(time.time()))
testunit = unittest.TestSuite()

# 将测试用例加入测试套件中
# testunit.addTest(unittest.makeSuite(test_isbn.Login))
file_name = "/Users/liutao/virproject_selenium/testsuit/report/" + now + "_result.html"
f = file(file_name, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = u'图书管理系统测试报告',
    description = u'用例执行情况：'
)


# 执行测试用例套件
# runner = unittest.TextTestRunner()
runner.run(all_tests_name)


