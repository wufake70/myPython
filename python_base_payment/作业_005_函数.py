# _*_coding :utf-8 _*_
# @Time :2022/6/24 10:21
# @File : 作业_005
# @Project : python_base_payment

# li = [2, 9, 5, 6, 10000, '8', 'u', 'p', 'niaho']
# li = [98, 76, 51, 234]
import pprint

li = [46, 45, 44, 72, 34, 45, 66, 78, 45, '188', '10000', 185]
li.sort(key=lambda x: str(x))
print(li)

print('=============第一题=============')
# 1.一个列表四个元组组成，每个元祖都是四个数字组成，
# 现在要求对这个列表排序，排序规则是按照每个元祖的第二个元素排序
# 提示：列表的自定义规则排序

li = [(54, 378, 157, 5), (894, '078', 7, 84), (48, '076', 5, 37), (657, '008', 6, 6)]

# 匿名函数参数 x 等价于 列表的元素（即元祖）
# x[1] 通过索引来获取元祖的第二个元素，
# str(x[1])转化为字符进行比较
li.sort(key=lambda x: str(x[1]))
print('排序的结果为')
print(li)

print('============第二题============')
# 2.构造isPrime()函数，参数是正整数，
# 如果整数是质数（只能够被1和自己整除的数），
# 质数返回True，否则返回False

def isPrime(a):
    if a != 2:  # 特殊值 2
        # 使用for循环 将a 除 2~~(a-1) 的结果进行判断
        for i in range(2, a - 1):
            # 对结果取余,判断是否等于0
            if a % i == 0:
                print('%s 不是质数' % str(a))
                # break只能结束循环，使用return结束函数
                print(i)
                return
        # for循环运行结束，、、、
        print('%s 是质数' % str(a))
    else:
        print('%s 是质数' % str(a))


a = input('请输入整数:')
a = int(a)
isPrime(a)

print('===========第三题===========')


# 3.定义一个函数，输入字符串，如果字符串是顺序则返回'UP'，
# 如果字符串是倒叙的则返回'DOWN'，如果是乱序的则返回'False'.
# 提示：临时排序使用sorted函数，不改变原列表

def pd(a):
    ls_1 = []
    for i in range(0, len(a)):
        ls_1.append(a[i])
    # print(ls_1)
    # 使用sorted函数，创建一个新的列表用于对照判断
    ls_2 = sorted(ls_1, key=lambda x: x)
    # ls_2.reverse()
    # print(ls_2)
    # 进入判断,先判断是顺序？
    for i in range(0, len(a)):
        if ls_1[i] == ls_2[i]:
            print('', end='')
        else:
            # 判断是倒叙？
            # ls_3 = ls_2.reverse()  报错写法
            # print(ls_3)
            for i_1 in range(0, len(a)):
                if ls_1[(len(a) - i_1 - 1)] == ls_2[i_1]:
                    print('', end='')
                else:
                    # 是乱序
                    # print('False')
                    # 设置返回值并结束函数
                    return 'False'
            # print('DOWN')
            # 设置返回值并结束函数
            return 'DOWN'
    # print('UP')
    # 使用return关键字设置返回值
    return 'UP'


a = input('请输入一串字符:')
print('结果为：')
print(pd(a))

print('===========第四题=============')
# 4.构造Max()函数，参数为一个包含多个数值类型的元祖，
# 从其中获取返回出最大值

# 新创建一个元祖
a = (73, 4, 58, 45, 78, 48, 9, 4, 56, 45)


def Max(a):
    # 将元祖中的数据传入到新列表中
    ls_1 = []
    for i in range(0, len(a)):
        ls_1.extend([a[i]])
        # 使用列表的sort()进行排序
        ls_1.sort()
    # 返回列表中最大值
    return ls_1[len(a)-1]


print('元祖中的最大值为' + str(Max(a)))



