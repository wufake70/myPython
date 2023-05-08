# _*_coding :utf-8 _*_
# @Time :2022/5/8 12:12
# @File : 031-python-字符串高级
# @Project : python-base

# 字符串的高级，字符串的方法（爬虫中常用的）
""" 字符串高级
1.获取长度：len（）
2.查找内容：find（），查找指定的内容在字符串中是否存在，存在返回第一次位置
3.判断：startswith，endswish；判断字符串是不是以谁开头/结尾
4.计算出现的次数：count（）；可以统计某些字符出现的次数
5.替换内容：replace（）；替换字符串中指定的内容，如果指定次数count，则替换不会超过count次
6.切割字符串：split（）；把指定的内容从字符串中切割出来
7.转大写/转小写：upper（）/lower（）
8.去空格处理：strip（）；注意：它只能取出字符串头和尾的空格
9.拼接处理：join（）；
10.检索字符串的位置：index() 或 find（） （一般使用他）;
注意：字符串，列表，元组（不可修改）都属于序列类型, 与其对应的是 散列类型： 字典 、集合（{}中只有值，没有键）

注意： 这些方法中区别是有无返回值，有返回值的可以直接print（）打印，无返回值不能直接打印，必须要变量接收
"""

# len()的使用区别于其他方法
a = 'china'
print('a变量中共有' + str(len(a)) + '字符串')

# 返回a变量中h第一次出现的位置
# 结果为1
print(a.find('h'))

# 判断字符串是否以谁开头
# 结果为False
print(a.startswith('s'))
# 结果为True
print(a.endswith('a'))


# 统计某些字符出现的次数
# 结果为1
print(a.count('c'))

# 替换指定字符串的内容
# 结果为chinese
print(str(a.replace('a', 'ese')))

# 切割字符串 注意：split() 默认切割空格
b = '9,9,99,9,99,9,98,8,,88,8'
# 输出结果为['9', '9', '99', '9', '99', '9', '98', '8', '', '88', '8']
print(b.split(','))

# 转大写/转小写
# 结果为CHINA
print(a.upper())
c = "HJJHRHUIRJ"
# 结果为hjjhrhuirj
print(c.lower())


# 去空格处理 strip（两端）
d = '    y r    '
# 共有11个字符串

print(len(d))
# 去空格后共有；注意：它只能取出字符串头和尾的空格
# 结果为3
print(len(d.strip()))


# 拼接处理 语法： '字符串'.join('字符串')
# 结果为hchinaechinalchinalchinao
print(a.join('hello'))
eg_1 = "hello world, I am python,python is good, you are worth to have it."
a = 'it is'.join(eg_1.split('I am'))  # 先进行字符串切割，在原先地方进行添加
print(a)

# 字符串索引, 语法： 变量.index（'要查找的字符串', 查找的开始位置）
# 要想查找全部的字符串位置需要遍历
# index（）方法，找不到字符串会报错，但是find（）方法不会，它会返回 -1
# 注意：程序一旦报错就会直接终止当前运行
a = eg_1.index('h', 2)
print(a)























