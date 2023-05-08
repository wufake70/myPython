# _*_coding :utf-8 _*_
# @Time :2022/5/8 11:07
# @File : 030-python-for循环
# @Project : python-base

# 爬虫中（大部分使用for循环）
"""
应用场景：
1.range（5）
2.range（1, 6）
3.range（1, 0.3）
4.循环字符串
5.循环一个列表的所有数据（爬虫中使用对多）、也称为遍历
"""
s = "I'm chinese"
# 打印字符串中第一个字符，索引为1，用s[0]
print(s[0])

# for循环遍历
"""
格式：
for 变量 in 要遍历的数据:
    代码块（方法体）
"""
# 遍历字符串
for i in s:
# 此时的 i 就是字符串类型
    print('我是' + '字符串' + i)

# range（5）
# range方法的结果是， 一个可以遍历的对象
# range（5）的范围是：0-4 左闭右开区间[0,5)
for i in range(5):
    print(i)

# range(1,8);range(起始值， 结束值），遵循有闭右开
for i in range(1, 8):
    print(i)

# range(1, 10, 3),range(起始值，结束值，步长）
# 控制台输出1，4，7，10
for i in range(1, 11, 3):
    print(i)

# 循环一个列表
a_list = ['周杰伦', '林俊杰', '陶杰']

# 遍历列表中的元素
for i in a_list:
    print(type(i))
    print('我是列表中的元素：' + i)


# 遍历列表中的下标
# 用 len() 来判断列表中元素的个数
print('a_list列表中一共有' + str(len(a_list)) + '个元素')
for i in range(len(a_list)):
    print(i)























