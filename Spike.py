#-*- coding: UTF-8 -*-
import os
from selenium import webdriver
import datetime
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('/home/gaoxing/下载/chromecj.com/chromecj.com-Auto-Refresh_v1.2.1.crx')
driver = webdriver.Chrome(chrome_options=chrome_options)
def login(): 
     # 打开淘宝登录页，并进行扫码登录 
     driver.get("https://www.taobao.com")
     time.sleep(1) 
     if driver.find_element_by_link_text("亲，请登录"): 
         driver.find_element_by_link_text("亲，请登录").click() 
         print("请在15秒内完成扫码") 
         time.sleep(15)
         #进入购物车界面
         driver.get("https://cart.taobao.com/cart.htm") 
     time.sleep(5)
     #点击全选按钮
     if driver.find_element_by_id("J_SelectAll1"):
      driver.find_element_by_id("J_SelectAll1").click()
     time.sleep(5)
     #点击结算
     if driver.find_element_by_id("J_Go"):
      driver.find_element_by_id("J_Go").click();
     now = datetime.datetime.now()
     #输出登陆成功以及当前时间
     print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
     #将预设时间与当前时间比较
def buy_on_time(buytime):
 while True:
    now = datetime.datetime.now()
    if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
        #每1秒点击一次提交订单按钮
        while True:
            try:
             driver.find_element_by_link_text('提交订单').click()
            except:
             time.sleep(1)
    time.sleep(0.1)
login()
buy_on_time('2018-11-11 00:19:00')
