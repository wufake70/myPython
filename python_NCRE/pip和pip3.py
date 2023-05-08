# _*_coding :utf-8 _*_
# @Time :2022/8/2 15:33
# @File : pip和pip3
# @Project : python_NCRE

"""
0、dos上 零时切换 Python版本和pip，set Path=D:\SoftWareSpace\python\python-3.5.3\Scripts\;D:\SoftWareSpace\python\python-3.5.3\;
1、pip是python的包管理工具，pip和pip3版本不同，都位于Scripts\目录下：
2、如果系统中只安装了Python2，那么就只能使用pip。
3、如果系统中只安装了Python3，那么既可以使用pip也可以使用pip3，二者是等价的。
4、如果系统中同时安装了Python2和Python3，则pip默认给Python2用，pip3指定给Python3用。
5、重要：虚拟环境中，若只存在一个python版本，可以认为在用系统中pip和pip3命令都是相同的.


pip 常用工具命令
install     #安装库
download    #下载库（一般不用，安装时会自动下载）
uninstall   #卸载库
freeze  # 以requirements格式导出安装包（如pip freeze > requirements.txt，将库导出到txt文件，导出的具体位置在命令行运行下的文件夹中，下回可以通过pip install -r requirements.txt在新的机器上安装了，要注意文件存放的位置。）
list    #展示所有库及其版本
show    #显示某个安装库的信息，如pip show pygame
search  #搜索名称或摘要包含关键词的库，如pip search pygame将搜索PyPI中名称或摘要包含pygame的所有库，并将其列出
"""






















