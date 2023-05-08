# _*_coding :utf-8 _*_
# @Time :2022/6/22 21:19
# @File : 作业_003
# @Project : python_base_payment

print('============第一题===========')
# 1.用for循环打印出一个4*4的方阵
for n in range(0, 4):
    for i in range(0, 4):
        print('python', end=' ')
    print('')

print('===========第二题===========')
# 2.一个列表有重复元素，编写程序，移除重复元素（只能使用我们学过的内容来实现，
# 提示for循环迭代列表时，列表改变会影响迭代）
ls = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 'hello', 'world', '世界', '你好', 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 'hello', 'world', '世界', '你好', 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 'hello', 'world', '世界', '你好', 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 'hello', 'world', '世界', '你好']
print(ls)

# 列表count（）方法，统计某个元素出现的次数
# print(ls.count('你好'))
# 创建新列表接收新元素
ls_1 = []
# 创建一个删除函数


def rm():
    # 列表总元素
    b_1 = len(ls)
    for a in range(0, b_1):
        # 判断元素是否重复
        if ls.count(ls[a]) == 1:
            # 将不重复的元素装入列表
            ls_1.append(ls[a])
        # 判断原列表中重复的元素是否已存在新列表里面
        elif ls[a] not in ls_1:
            ls_1.append(ls[a])

# 调用删除函数


rm()
print(ls_1)

'''
def rm():
    a = input('请输入重复的元素：')
    a = int(a)
    b = ls.count(a)
    for c in range(1, b):
        ls.remove(a)


for i in range(0, 5):
     rm()
print(ls)
'''

print('============第三题=============')
# 3.判断100-1000之间水仙花数，并且保存在列表中（水仙花数 等于各位数 的数立方之和）
# 接收水仙花数
SX = []
for i in range(100, 1000):
    a_1 = i // 100  # 取出百位
    # print(a_1)
    a_2 = i // 10 % 10  # 取出十位
    # print(a_2)
    a_3 = i % 10  # 取出个位
    # print(a_3)
    if i == (a_1 ** 3 + a_2 ** 3 + a_3 ** 3):
        # 装入集合
        SX.extend([i])

print('水仙花数的集合', end=',')
print(SX)
print('')

print('===========第四题===========')
# 4.利用for循环去迭代一个列表的同时输出下标职位奇数的元素
# 创建一个列表
a = []
for i in range(1, 100):
    a.extend([i])
print(a)

for i in range(0, 99):
    if (i % 2) == 1:
        print(a[i])
