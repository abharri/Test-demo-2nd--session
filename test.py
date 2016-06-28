#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time,urllib,urllib2,re,requests,json,codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8")

browser = webdriver.Firefox()  # Get local session of firefox
browser.get('http://192.168.31.121:3020/portal/login')  # Load page
# assert "Yahoo!" in browser.title
try:
    browser.find_element_by_id('authId').send_keys('htiaf@qq.com')  # Find the query box
    browser.find_element_by_id('password').send_keys('12345678')
    browser.find_element_by_class_name('ant-btn').click()
    time.sleep(3)  # Let the page load, will be added to the API
except NoSuchElementException:
    print 'sorry we can\'t find it'

try:
    # for i in range(0,6):
      product=browser.find_elements_by_class_name('ProductItem')[0]
      actions=ActionChains(browser)
      actions.move_to_element(product).perform()
      time.sleep(3)
      hidden_btn=browser.find_element_by_class_name('HoverProduct-button')
      actions.click(hidden_btn)
      actions.perform()
      browser.find_element_by_id('corporation').send_keys(u'杭州誉存科技有限公司')

      browser.find_element_by_class_name('ant-btn').click()
      time.sleep(3)
      text=browser.find_element_by_class_name('ant-modal-content').text
      # print text
      if(u'公司报告已存在' in text):
          print '查看已存在报告'
          browser.find_element_by_link_text("跳转").click()
          time.sleep(1)
          browser.find_element_by_class_name('fa-line-chart').click()
          time.sleep(3)
          # browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$"+str(j)+".0']").click()
          # time.sleep(3)
          # browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$nav.1.2.0.0.1:$2.0']").click()
          # //获取基本信息
          # data=browser.find_element_by_xpath("//div[@data-reactid='.0.2.0.2.0.$demo5.0.0.$content.$1.0']").text
          infokey=browser.find_elements_by_xpath("//span[@class='Report-info-key']")
          infovalue=browser.find_elements_by_xpath("//span[@class='Report-info-value']")
          for i in range(0,len(infokey)):
                #print infokey[i].text
                #print infovalue[i+1].text

                if '工商注册号' in infokey[i].text:
                    #print infovalue[i-1].text
                    if int(infovalue[i].text) == 330106000363957:
                        print (u"工商注册号 正确:"+str(infovalue[i].text))
                    else:
                        print (u"工商注册号 错误:"+str(infovalue[i].text))

                if '企业名称' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip()== u"杭州誉存科技有限公司":
                        print(u"企业名称 正确:"+str(infovalue[i].text))
                    else:
                        print(u"企业名称 错误:"+str(infovalue[i].text))


                if '法人代表' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text() == u"陈玮":
                        print(u" 正确:"+str(infovalue[i].text))
                    else:
                        print(u"法人姓名 错误:"+str(infovalue[i].text))
                        fail=False

                if '企业（机构）类型' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "私营有限责任公司(自然人控股或私营性质企业控股)":
                        print(u"企业（机构）类型 正确:"+str(infovalue[i].text))
                    else:
                        print(u"企业（机构）类型 错误:"+str(infovalue[i].text))



                if '成立日期' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "2014-10-29":
                        print(u"成立日期 正确:"+str(infovalue[i].text))
                    else:
                        print(u"成立日期 错误:"+str(infovalue[i].text))


                if '经营状态' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "无":
                        print(u"经营期限自 正确:"+str(infovalue[i].text))
                    else:
                        print(u"经营期限自 错误:"+str(infovalue[i].text))


                if '经营期限至' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "无":
                        print(u"经营期限至 正确:"+str(infovalue[i].text))
                    else:
                        print(u"经营期限至 错误:"+str(infovalue[i].text))


                if '登记机关' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "杭州市西湖区工商行政管理局":
                        print(u"登记机关 正确:"+str(infovalue[i].text))
                    else:
                        print(u"登记机关 错误:"+str(infovalue[i].text))


                if '注册地址' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "杭州市西湖区文二西路820号2幢213室":
                        print(u"注册地址 正确:"+str(infovalue[i].text))
                    else:
                        print(u"注册地址 错误:"+str(infovalue[i].text))


                if '最后年检年度' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "无":
                        print(u"最后年检年度 正确:"+str(infovalue[i].text))
                    else:
                        print(u"最后年检年度 错误:"+str(infovalue[i].text))


                if '登记机关' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "杭州市西湖区工商行政管理局":
                        print(u"登记机关 正确:"+str(infovalue[i].text))
                    else:
                        print(u"登记机关 错误:"+str(infovalue[i].text))


                if '经营（业务）范围' in infokey[i].text:
                    #print infovalue[i-1].text
                    if infovalue[i].text.strip() == "一般经营项目：服务：计算机科技、网络科技、电子科技、信息科技、计算机软硬件、网络技术的技术开发、技术咨询、技术服务":
                        print(u"经营（业务）范围 正确:"+str(infovalue[i].text))
                    else:
                        print(u"经营（业务）范围 错误:"+str(infovalue[i].text))




      else:
          print '新创建公司报告'
          time.sleep(2)
          browser.find_elements_by_class_name('ant-btn')[2].click()
except NoSuchElementException:
       print "can't find element"

time.sleep(3)
# browser.close()


