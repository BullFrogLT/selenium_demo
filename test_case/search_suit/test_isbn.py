#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from common_lib import login
import HTMLTestRunner
import unittest, time
from selenium import webdriver


class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        base_url = "http://127.0.0.1:9000/login/"
        self.driver.get(base_url)
        login.login(self)

    def test_search(self):
        '''
            校验查询书名'1984'的关键词是否正确
        '''
        driver = self.driver
        # driver.get(self.base_url)

        # login.login(self)

        # 搜索书名 “19” 关键词
        print "start test_search: search 1984"
        driver.find_element_by_id("id_keyword").send_keys("1984")
        driver.find_element_by_xpath("/html/body/div/form/div/div[4]/span/button").click()
        self.assertTrue(u"乔治·奥威尔" in driver.page_source, "王小波创作数据未找到")
        # time.sleep(5)

    def test_createuser_search(self):
        '''
            选定作者进行搜索，搜索关键词 “王小波”
        '''
        print "start createuser_search: search 王小波"
        driver = self.driver
        # driver.get(self.base_url)

        # login.login(self)
        #搜索作者 “王小波”
        driver.find_element_by_id("id_search_by_2").click()
        driver.find_element_by_id("id_keyword").send_keys(u"王小波")
        driver.find_element_by_xpath("/html/body/div/form/div/div[4]/span/button").click()
        self.assertTrue(u"王小波" in driver.page_source, "王小波创作数据未找到")


    def tearDown(self):
        print "aaa"
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Search("test_search"))
    testunit.addTest(Search("test_createuser_search"))

    runner = unittest.TextTestRunner()

    file_name = "/Users/liutao/virproject_selenium/testsuit/report/result.html"
    f = file(file_name, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream = f,
        title = u'图书管理系统测试报告',
        description = u'用例执行情况：'
    )

    runner.run(testunit)
    # unittest.main()
