#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest, time
from selenium import webdriver

def login(self):
    driver = self.driver

    try:
        username = "admin"
        password = "admin"

        driver.find_element_by_id("id_username").send_keys(username)
        driver.find_element_by_id("id_password").send_keys(password)
        driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/div/button").click()

    except:
        # 截屏
        driver.get_screenshot_as_file("/Users/liutao/virproject_selenium/testsuit/pic/login_error.png")
