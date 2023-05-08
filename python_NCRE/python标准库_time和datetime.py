# _*_coding :utf-8 _*_
# @Time :2022/7/12 18:20
# @File : python标准库_time
# @Project : python_NCRE

import time
import datetime

# 1.获取当前的时间戳，单位秒
print(time.time())

# 获取当前本地时间 并以易读方式显示
print(time.ctime())

# 获取当前世界标准时间（比北京时间晚8个小时） 返回为计算机可处理的时间格式
print(time.gmtime())    # time.struct_time

# 获取当前当地标准时间 同样返回计算机可处理的时间格式
print(time.localtime()) # time.struct_time

# 2.时间格式化 将时间以合理得方式展示出来
"""
格式化控制符
%Y      年份
%m      月份
%d      日期
%H      小时(24)
%l      小时(12)
%M      分钟
%S      秒

%B      月份名称
%b      月份名称缩写

%A      星期
%a      星期缩写

格式: strftime(tpl, ts)
tpl 表示格式化模板
ts 表示计算机内部时间类型变量 即 ts=time.gmtime()
"""

ts = time.gmtime()
print('当前的世界时间:', time.strftime('%Y-%m(%b)-%d, %a, %H, %p, %M', ts))
ts_2 = time.localtime()
print('当前的当地时间:', time.strftime('%Y-%m(%b)-%d, %a, %H, %p, %M', ts_2))


# datetime库 以类的方式 提供多种日期和时间表达式。
# 该书只介绍datetime.datetime类 日期和时间表示类 功能覆盖 date类和time类

# 使用 datetime.datetime.now() 获取当前的日期和时间 （生成对象）
print(datetime.datetime.now())

# 使用 该类中 datetime.utcnow() 获取当前的 世界标准 日期和时间 （生成对象）
print(datetime.datetime.utcnow())

# 调用datetime()函数直接创建一个datetime对象 效果同上 （生成对象）
print(datetime.datetime(2016, 9, 16, 22, 33, 32, 7))  # hour minute second 可默认为零

# 用someday 来接收 生成的 对象
someday = datetime.datetime.now()
print(someday.year)         # 获取 对象的年属性
print(someday.month)        # 获取 对象的月属性
print(someday.day)          # 获取 对象的日期属性
print(someday.hour)         # 获取 对象的 小时 属性
print(someday.minute)       # 获取 对象的 分钟属性
print(someday.second)       # 获取 对象的 秒 属性

# 时间格式化控制符同上















