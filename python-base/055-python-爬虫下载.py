# _*_coding :utf-8 _*_
# @Time :2022/5/10 12:13
# @File : 055-python-爬虫下载
# @Project : python-base

# 导入urllib.request
import urllib.request

# 下载网页
# 格式：urllib.request.urlretrieve（网址，'路径和文件名‘）
# url_page = 'http://www.google.com'
# urllib.request.urlretrieve(url_page, 'file_storage/google.htm')

# 下载图片
# 注意：文件的拓展名
# url_picture = 'https://img1.baidu.com/it/u=350945439,796966266&fm=253&fmt=auto&app=120&f=JPEG?w=700&h=394'
# urllib.request.urlretrieve(url_picture, 'file_storage/p_UI.JPEG')


# 下载音乐
#
#

# 下载视频
url_video = 'https://www.youtube.com/s/search/audio/failure.mp3'
urllib.request.urlretrieve(url_video, 'file_storage/p_好看视频.mp4')































