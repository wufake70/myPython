# _*_coding :utf-8 _*_
# @Time :2022/5/29 8:55
# @File : 测试001
# @Project : python_base_payment

# print()函数中，end=',' 参数可以使所有print()输出的内容写到一行上 ,并用逗号隔开
# for i in range(1, 10):
#     print(str(i), end=',')
#
#     print(str(i), end=',')
#     print(end='-')

# 判断是否能够组成三角形
# a = int(input('请输入第一个整数:'))
# b = int(input('请输入第二个整数:'))
# c = int(input('请输入第三个整数:'))
#
# if a == b and a == c:
#     if c == b:
#         print('%d,%d,%d,可以组成一个三角形' % (a, b, c))
#     else:
#         print('%d,%d,%d, 不 可以组成一个三角形' % (a, b, c))
# elif a < (b + c) and b < (a + c) and c < (b + a):
#     print('%d,%d,%d,可以组成一个三角形' % (a, b, c))
# else:
#     print('%d,%d,%d, 不 可以组成一个三角形' % (a, b, c))

# 将数字存入列表中
lst = []
lst_1 = []
for i in range(1, 100):
    # print(type(i))
    lst.append(i)  # lst_1 = lst.append(i) 此写法不对，因为列表的等于号 是复制另外一个列表将其粘贴给他
    lst.extend([i])  # lst.extend(i)会报错，整型不支持迭代

print(lst)
lst_1 = lst
lst_1.remove(1)  # 删除指定元素第一个
lst_1.clear()   # 一键清除
print(lst_1)

ls = [1, 1, 1, 1, 1, 1, 1, ]
a = ls.count(1)
ls.remove(1)
print(a)
