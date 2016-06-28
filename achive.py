#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import fileoperation

browser = webdriver.Firefox()  # Get local session of firefox
browser.get('http://192.168.31.121:3020/portal/login')  # Load page
fileoperation.login(browser,'htiaf@qq.com','12345678')
time.sleep(3)

# browser.find_element_by_xpath("//button[@data-reactid='.4.$dialog.0.1.0.2.1']").click()
# time.sleep(3)
# browser.find_elements_by_class_name('ant-btn')[1].click()
# time.sleep(3)
company=u'重庆富盛阀门制造股份有限公司'
fileoperation.searchandfill(browser,0,company)
text=browser.find_element_by_class_name('ant-modal-content').text
try:
      # print text
      if(u'公司报告已存在' in text):
          print '查看已存在报告'
          browser.find_element_by_link_text("跳转").click()
          time.sleep(1)
          browser.find_element_by_class_name('fa-line-chart').click()
          time.sleep(3)


          for i in range(1,4):
              j=i
              browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
              time.sleep(3)
              # browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$2.0']").click()

              # //获取基本信息
              data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$"+str(j)+".0']").text
              if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                  print '基本信息模块出现问题'
                  continue
              else:
                  fileoperation.file(data)
          time.sleep(2)


          #huo获取互联网大数据信息
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.1']").click()
          for i in range(1,3):
              j=i
              browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
              data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$"+str(j)+".0']").text
              if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                 print '互联网大数据模块出现问题'
                 continue
              else:
                 fileoperation.file(data)
          time.sleep(2)


        #获取风险信息、
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.2']").click()
          for i in range(1,4):
              j=i
              browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
              data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$"+str(j)+".0']").text
              if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                  print '风险信息模块出现问题'
                  continue
              else:
                  fileoperation.file(data)

      else:
          print '新创建公司报告'
          time.sleep(2)
          browser.find_elements_by_class_name('ant-btn')[2].click()
except NoSuchElementException:
       print "can't find element"

time.sleep(30)
browser.close()


