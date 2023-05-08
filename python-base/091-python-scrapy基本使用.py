# _*_coding :utf-8 _*_
# @Time :2022/5/24 20:52
# @File : 091-python-scrapy基本使用
# @Project : python-base

"""
现在已有两套python


一，scrapy 的基本操作
  1.创建爬虫的项目
  语法： scrapy startproject 项目的名字
  注意：项目的名字不允许使用数字开头，也不能包含中文

  2.创建爬虫文件
  要在spiders文件中去创建爬虫文件
  cd 项目的名字\项目的名字\spiders
  例如：cd scrapy_baidu_091\scrapy_baidu_091\spiers

  创建爬虫文件
  语法：scrapy genspider 爬虫文件名 要爬取的网页
  eg: scrapy genspider baidu www.baidu.com
  注意：一般情况下不需要添加协议头，因为start_urls的值就是根据allowed_domains来修改的

  3.运行爬虫代码
  语法：scrapy crawl 爬虫的名字(注意，要在终端中运行）
  eg:
  scrapy crawl baidu


二，scrapy（文件）项目的结构
项目的名字
    项目的名字
        spiders文件夹（存储爬虫文件的）
            init
            自定义的爬虫文件 （核心文件） 非常重要
        init（初始化时的文件）
        item（定义数据结构的地方，爬取的数据都包含那些）
        middleware  中间件  代理
        pipelines   （用来处理下载的数据）
        setting  （配置文件 robots协议，ua定义）

三，response的属性和方法
    response.text            获取的响应的字符串
    response.body            获取的是二进制数据
    response.xpath           可以直接用xpath的方法来解析response中的内容
    response.extract()       提取seletor对象的data属性值
    response.extract_first() 提取的seletor列表的第一个数据

四、scrapy shell 调试
    直接直接再电脑终端键入  scrapy shell 目标url
    即可进行调试

"""





























