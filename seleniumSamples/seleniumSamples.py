#coding=utf-8
from selenium import webdriver

driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.get('http://www.google.cn')
driver.forward()
driver.back()


driver.maximize_window()
driver.close()
