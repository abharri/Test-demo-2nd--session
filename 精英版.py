#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import urllib,urllib2,re,requests,json,codecs,time
import fileoperation


browser = webdriver.Firefox()  # Get local session of firefox
browser.get('http://192.168.31.121:3020/portal/login')  # Load page
fileoperation.login(browser,'htiaf@qq.com','12345678')
time.sleep(3)

try:
      company=u'北京奇虎360科技有限公司'
      fileoperation.searchandfill(browser,1,company)
      text=browser.find_element_by_class_name('ant-modal-content').text

      # print text
      if(u'公司报告已存在' in text):
          print '查看已存在报告'
          browser.find_element_by_link_text("跳转").click()
          browser.implicitly_wait(2)
          browser.find_element_by_class_name('fa-line-chart').click()
          browser.implicitly_wait(10)
          browser.find_elements_by_xpath("//a[@data-reactid='.0.2.0.0.0.0.0.1.2.0.0']")[0].click()
          browser.implicitly_wait(30)
          browser.find_elements_by_class_name('ant-btn')[1].click()
          browser.implicitly_wait(60)


          for i in range(1,4):
            j=i
            browser.implicitly_wait(60)
            browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
            browser.implicitly_wait(60)
            # browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$2.0']").click()
             # //获取基本信息
            data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$"+str(j)+".0']").text
            if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                  print '基本信息模块出现问题'
                  continue
            else:
                  fileoperation.file(data)
            browser.implicitly_wait(60)

         #huo获取风险信息
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.1']").click()
          for i in range(1,4):
              j=i
              browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()

              data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.+"+str(j)+".0']").text
              if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                  print '风险信息模块出现问题'
                  continue
              else:
                  fileoperation.file(data)
          browser.implicitly_wait(60)

        #获取关联信息
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.2']").click()
          for i in range(1,6):
              j=i
              browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
              data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$"+str(j)+".0']").text
              if(u'出现异常了，请联系管理员...' in data or data==""):

                  print '关联信息出现问题'
                  continue
              else:
                 fileoperation.file(data)
          browser.implicitly_wait(60)

         #获取资产公示信息
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.3']").click()
          for i in range(1,4):
              j=i
              browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
              data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$"+str(j)+".0']").text
              if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                  print '资产公示信息出现问题'
                  continue
              else:
                  fileoperation.file(data)
              browser.implicitly_wait(60)

          #获深度洞察示信息
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.4']").click()
          data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0']").text
          if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                print '深度洞察信息出现问题'

          else:
                  fileoperation.file(data)
          browser.implicitly_wait(60)


      #获取互联网大数据信息
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.5']").click()
          for i in range(1,4):
              j=i
              browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
              data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$"+str(j)+".0']").text
              if(u'出现异常了，请联系管理员...' in data or data.strip()==''):

                  print '互联网大数据出现问题'
                  continue
              else:
                  fileoperation.file(data)
              browser.implicitly_wait(60)


           #获取行业信息
          browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.0.0.$demo4.0.6']").click()
          data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content']").text
          if(u'出现异常了，请联系管理员...' in data or data.strip()==''):
                  print '行业信息出现问题'

          else:
                  fileoperation.file(data)
          browser.implicitly_wait(60)


      else:
          print '新创建公司报告'
          time.sleep(2)
          browser.find_elements_by_class_name('ant-btn')[2].click()
except NoSuchElementException:
       print "can't find element"

time.sleep(30)
browser.close()


