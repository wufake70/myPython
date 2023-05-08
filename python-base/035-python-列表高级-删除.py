# _*_coding :utf-8 _*_
# @Time :2022/5/9 14:56
# @File : 035-python-列表高级-删除
# @Project : python-base
"""
列表的高级-删除
1.del：根据下标进行删除
2.pop：删除最后一个元素
3.remove：根据元素的值进行删除

注意：del和pop删除最后一个数据时没有任何区别
"""
a_list = [1, 2, 3, 4, 5, 6, 7]
print(a_list)

# del 格式：del 变量名[下标]
del a_list[2]
# 结果为 [1, 2, 4, 5, 6, 7]
print(a_list)

# pop  格式：变量.pop()
a_list.pop()
# 结果为 [1, 2, 4, 5, 6]
print(a_list)


# remove  格式：变量.remove(列表的值) 注意：当元素没有要删除的值的时候，就会报错
a_list.remove(1)
# 结果为 [2, 4, 5, 6]
print(a_list)



























