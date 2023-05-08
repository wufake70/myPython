# _*_coding :utf-8 _*_
# @Time :2022/6/23 14:37
# @File : 作业_004_字符串和散列类型
# @Project : python_base_payment
from pprint import pprint
import random

print('===========第一题===========')
# 1.利用数据类型的特点，找出两个列表中相同的数据，并打印出来
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'j', 'i', 'o', 'g', 'n', ]
lst_2 = [3, 4, 5, 6, 'g', 'j', 'n', 'j', 'k']

print('两个列表相同的数据是：')
for i in range(0, len(lst_2)):
    # 判断lst_2 是否存在 lst_1中
    if lst_2[i] in lst_1:
        print(lst_2[i], end=',')
print('')

print('===========第二题===========')
# 2.统计一串字符中，每个字母a-z的出现次数，忽略大小写，利用字典保存
str_1 = 'hello world, i am python; HELLO WORLD, I AM PYTHON，a'

# 全部转小写
str_2 = str_1.lower()
# 字幕对照表
str_3 = 'abcdefghijklmnopqrstuvwxyz'
# print(str_2.find('h', 1))
# print(str_3[0])  字符串序列类型
# print('a' in str_1)  判断字符串是否存在
# 创建一个新字典
dict_1 = {}
for i in range(0, 25):
    # 判断对照字幕是否存在str_2
    if str_3[i] in str_2:
        # print(str_3[i])  # 标记
        # 出现的起始位置
        i_1 = str_2.find(str_3[i], 0)
        # 创建一个变量记录次数
        i_2 = 1
        # 使用while循环测试出现几次
        while i_1 <= len(str_2):
            i_1 += 1
            i_1 = str_2.find(str_3[i], i_1)
            # 判断是否出现一次以上
            if i_1 != -1:
                print('', end='')
            else:
                dict_1.update({str_3[i]: i_2})
                # 终止while循环
                break
            i_2 += 1
    # 不存在的字母次数为零
    else:
        dict_1.update({str_3[i]: 0})

# 使用pprint打印该集合
pprint(dict_1)

print('============第三题============')
# 3.判断用户输入的是不是一个手机号。
# 手机号规则：11位数，纯数字

for i in range(0, 10000):
    a = input('请输入您的手机号：')
    a_1 = len(a)
    if a.isdigit() and a_1 == 11:
        print('感谢配合！！')
        break
    else:
        print('请重试')
        continue

print('===========第四题============')
# 4.利用26个字母和10个数字，随机生成3组6位数的验证码，且验证码不能相同
# range() 函数，有几个注意点：
# （1）它表示的是左闭右开区间；
# （2）它接收的参数必须是整数，可以是负数，但不能是浮点数等其它类型；
# （3）它是不可变的序列类型，可以进行判断元素、查找元素、切片等操作，但不能修改元素；
# （4）它是可迭代对象，却不迭代器。

# chr()函数： 通过ascll码找到对应字符

# random模块,choice()方法会随机返回序列中一个元素

# 创建一个列表用于储存随机字符
lst = []

# 创建一个函数形参
code_1 = ''


# 创建一个函数
def code(code_1):
    for n in range(6):
        c_1 = str(random.randint(0, 9))  # 获取随机数字,并转为字符串 方便存储
        c_2 = chr(random.randint(65, 90))  # 获取随机小写字母
        c_3 = chr(random.randint(97, 122))  # 获取随机大写字母
        # 将上列随机字符装入列表
        lst.extend([c_2, c_3, c_1])  # extend()方法多个元素增加，要用中括号 []
        # print(lst)
        # 再从该列表 随机选出验证码的第一位,第二位、、、、、
        # 并且使用‘+ ’进行拼串
        code_1 += random.choice(lst)
    print('验证码为，' + code_1)


# 调用函数
code(code_1)
