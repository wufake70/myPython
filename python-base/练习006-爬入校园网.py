# _*_coding :utf-8 _*_
# @Time :2022/5/20 14:41
# @File : 练习006-爬入校园网
# @Project : python-base

from selenium import webdriver

url = 'http://webvpn.lzjtu.edu.cn/http/77726476706e69737468656265737421e8e240922c35265c64029db9d6502720222896/xs_main.aspx?xh=20211103104'
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
browser.get(url)
