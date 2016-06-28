#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,urllib,urllib2,re,requests,json,codecs
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



def file(data):
    changedata=data.encode('utf')
    file=open('C:\data.txt','a')
    file.write(changedata)
    file.close()
    newfile = open('C:\data.txt')
    line=newfile.readline()
    while line:
        print line
        line=newfile.readline()
    newfile.close()

def sendMail(to_list,sub,content):
    '''Sending mail for attention'''
    mail_host="smtp.163.com"  #设置服务器
    mail_user="emma_tang123"    #用户名
    mail_pass="abc123"   #口令
    mail_postfix="163.com"  #发件箱的后缀
    me="yucun"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False



def login(browser,username,password):

    try:
        browser.find_element_by_id('authId').send_keys(username)  # Find the query box
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_class_name('ant-btn').click()
        time.sleep(3)  # Let the page load, will be added to the API
        browser.find_element_by_xpath("//button[@data-reactid='.4.$dialog.0.1.0.2.1']").click()
        time.sleep(3)
        # browser.find_elements_by_class_name('ant-btn')[1].click()
        time.sleep(3)
    except NoSuchElementException:
        print 'sorry we can\'t find it'



def searchandfill(browser,productitem,company):
    try:
    # for i in range(0,6):
      product=browser.find_elements_by_class_name('ProductItem')[productitem]
      actions=ActionChains(browser)
      actions.move_to_element(product).perform()
      time.sleep(3)
      hidden_btn=browser.find_element_by_class_name('HoverProduct-button')
      actions.click(hidden_btn)
      actions.perform()
      browser.find_element_by_id('corporation').send_keys(company)

      browser.find_element_by_class_name('ant-btn').click()
      time.sleep(3)


    except NoSuchElementException:
       print "can't find element"
