# _*_coding :utf-8 _*_
# @Time :2022/6/28 9:19
# @File : 08_列表推导式
# @Project : python_base_payment


# [表达式 for 变量 in 序列]
# 让变量去序列中取值，每取一个值就创建列表中的一个元素，元素的值就是表达式的值
# for 变量 in 序列：
#     产生元素
list1 = [1 for x in range(4)]
print(list1)        # [1, 1, 1, 1]

list2 = [x for x in range(4)]
print(list2)        # [0, 1, 2, 3]

list3 = [2*x for x in range(4)]
print(list3)        # [0, 2, 4, 6]

list4 = [len(x) for x in ["abc", "hello", "world"]]
print(list4)        # [3, 5, 5]

# [表达式 for 变量 in 序列 if 条件语句]
# 让变量去序列中取值，每取一个值就判断条件语句是否为True，如果为True就创建一个列表元素，元素的值是表达式的值
# for 变量 in 序列：
#     if 条件语句：
#         产生元素
list6 =[x for x in range(6) if x & 1 == 0]
print(list6)        # [0, 2, 4]

list7 = [x**2 for x in range(10) if x % 2]
print(list7)    # [1, 9, 25, 49, 81]

# [表达式 for 变量1 in 序列1 for 变量2 in 序列2]
# for 变量1 in 序列1：
#     for 变量2 in 序列2：
#         产生一个列表元素（值是表达式的结果）
list8 = [x*y for x in range(4) for y in range(3)]
print(list8)        # [0, 0, 0, 0, 1, 2, 0, 2, 4, 0, 3, 6]

# [表达式 for 变量1 in 序列1 for 变量2 in 序列2 if 条件语句]
# for 变量1 in 序列1：
#     for 变量2 in 序列2：
#         if 条件语句：
#             产生一个列表元素（值是表达式的结果）
list9 = [x+y for x in range(3) if x % 2 for y in range(3)]
print(list9)        # [1, 2, 3]

























