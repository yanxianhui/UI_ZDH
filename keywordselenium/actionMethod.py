# coding=utf-8
from selenium import webdriver
from base.find_element import FindElement
import time
import os
from utils.path import DRIVER_PATH
import random
class ActionMethod:
    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            # self.option = webdriver.ChromeOptions()
            # self.option.add_argument("headless")
            # self.driver = webdriver.Chrome(chrome_options=self.option)
            self.driver = webdriver.Chrome(DRIVER_PATH+"\chromedriver.exe")
            self.driver.maximize_window()
            print("启动谷歌")
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            print("启动火狐")
        else:
            self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 输入元素(随机生成值，患者姓名)
    def element_send_key(self, key):
        element = self.get_element(key)
        num=random.randint(1,100)
        element.send_keys("TV"+str(num))
        print("TV"+str(num))
    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 等待（3s）
    def sleep_time(self):
        time.sleep(3)

    # 等待（1s）
    def sleep_timeone(self):
        time.sleep(1)

    # 等待（2s）
    def sleep_timetwo(self):
        time.sleep(2)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()
        time.sleep(1)
        self.driver.quit()

    # 获取title
    def get_title(self):
        title = self.driver.title
        return title

    # 上传图片（带有参数）
    def Uploadimg(self,value):
        os.system(value)

    # 上传图片（不带参数）
    def Uploadimgs(self):
      os.system("D:\\Ggshang1.exe")


    def Expected(self,key):
        element = self.get_element(key)
        res=element.text
        return  res



