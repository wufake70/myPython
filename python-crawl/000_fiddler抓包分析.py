# _*_coding :utf-8 _*_
# @Time :2022/12/17 20:15
# @File : 000_fiddler抓包分析
# @Project : python-crawl


"""
一、发送(执行)目标请求包
    ①使用查找功能(也可crtl+F)搜索到 目标请求包(html、js、json 文件)
    ②按住并拖动到 composer（组合器）面板上，点击执行 即可 重新发送
    ③观察 process 可知 该求情是由 fiddler 发起的。

二、使用过滤器
    ①点击 filter(过滤器)，来到过滤器面板
    ②勾选 use filter （即 使用过滤器）
    ③在 hosts 字段上 选择 “show only the following Hosts”(只展示下列主机)，
      并在 编辑框 填上 对应的域名。（注意： 使用英文分号结尾）
    ④通过 请求头中 的参数 过滤
      勾选 "只显示当前网址包含" 并在编辑框中 填入对应参数。



"""





















