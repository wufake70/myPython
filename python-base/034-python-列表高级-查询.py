# _*_coding :utf-8 _*_
# @Time :2022/5/8 16:20
# @File : 034-python-列表高级-查询
# @Project : python-base

# 所谓查找就是看指定的元素是否存在
# 方法：in（使用得更多）  和 not in

# in 判断某一个元素是否在某一个列表中，存在就返回 布尔值True
food_list = ['锅包肉', '汆白肉', '东北乱炖']
food = input('请输入您想要吃的菜：')
food = [food]
if food in food_list:
    print('该菜我们有')
else:
    print('该菜我们没有')






























