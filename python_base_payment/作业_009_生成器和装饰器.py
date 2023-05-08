# _*_coding :utf-8 _*_
# @Time :2022/7/6 16:08
# @File : 作业_009_生成器和装饰器
# @Project : python_base_payment

print('==============第一题=============')


# 1.利用装饰器，记录函数的运行次数


def decorator(func):
    # print('nihao')                                    # 装饰器会先执行一遍，但执行一遍
    a = 0

    def num():                                              # 在定义函数时，不会执行里面的 调用函数; 将调用函数 赋给一个变量，该变量即代表了调用函数
        # global a                                      # global 只能再局部 声明全局 ，a = 0 在这里并不是全局变量，而是嵌套函数外部的变量
        nonlocal a                                          # 应使用nonlocal 声明嵌套函数外部函数 的变量，才可在内部函数进行修改
        a += 1
        func()
        # print('我是额外的函数')
        print(f'这是第{a}次调用')

    return num                                      # 将返回的函数体赋给 被装饰函数 nh()


@decorator
def nh():
    print('你好  世界！')


nh()
nh()
nh()

print('=============第二题=============')


# 2.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
# 通过修改以下代码中的BUG，来达到上述要求。

# 代码如下：
# def age(n):
#     if n==1:
#         c = 10
#     else:
#         c = age(n) + 2            陷入无限循环，报超过递归最大限度错误
#     return n
# print(age(5))


def age(n):
    if n == 1:
        c = 10
        # print(c)

        # return c                        # 将第一个人的数据返回
    else:
        c = age(n-1) + 2                    # 递归函数：在函数里面调用函数，不能超过最大递归限度
        # print(c)
        # return c                        # 返回递归函数中最后的数据

    return c


print(age(5))
