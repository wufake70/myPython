# _*_coding :utf-8 _*_
# @Time :2022/5/12 13:29
# @File : 白嫖
# @Project : python-base

url = input('请输入下载网址：')
name = input('请命名文件：')
extended_name = input('请输入该文件的拓展名：')
import urllib.request
import urllib.parse
urllib.request.urlretrieve(url, 'file_storage/' + name + '.' + extended_name)
print('下😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️载成功')





















