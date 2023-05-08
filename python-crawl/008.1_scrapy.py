# _*_coding :utf-8 _*_
# @Time :2022/10/13 21:01
# @File : 008.1_scrapy
# @Project : python-crawl

"""

1.  scrapy 基操
    创建一个项目                              scrapy startproject projectname
    新建爬虫文件(进入 项目中的spider 文件中)   scrapy genspider tb www.taobao.com(不需要协议)

    在 spider目录下
    scrapy list                             爬虫文件列表
    scrapy crawl tb                         运行 tb 爬虫文件
    scrapy crawl pdd                        运行 pdd 爬虫文件
    scrapy shell url(相关地址)              代码调试



2.  scrapy 五大组件
    Scrapy Engine                 Scrapy 引擎
    Spiders                       爬虫文件 (返回响应的数据 进行解析)
    item Pipline(管道)            解析后的 数据(存储....) 处理
    Scheduler                     计划程序
    Downloader


3.  response 的 属性和方法 （使用 for循环 迭代 dir(response) 即可） (过于繁琐)
    body                body 标签
    cb_kwargs
    certificate
    copy
    css                 css选择器(返回 特定的 selector 对象)
    encoding
    flags
    follow
    follow_all
    headers             请求头
    ip_address          IP地址
    json                JSON数据
    meta                元数据
    replace
    request
    selector            scrapy特定的选择器对象 (get方法获取对应的数据、)
    status              响应码
    text                全部文本 (使用xpath 或 bs4 进行数据提取 比较方便)
    url
    urljoin
    xpath               xpath 选择器 (返回 特定的 selector 对象)

"""





















