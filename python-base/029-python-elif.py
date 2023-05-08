# _*_coding :utf-8 _*_
# @Time :2022/5/8 10:35
# @File : 029-python-elif
# @Project : python-base

"""
格式：
if 判断：
    代码块
elif：
    代码块
else
    代码块
"""

# 如果你考了90分以上，优秀
# 如果你考了80分以上，良好
# 如果你考了70分以上，中等
# 如果你考了60分以上，合格
# 否则，不合格

score = input('请输入您的分数：')
score = int(score)
if 100 >= score >= 90:
    print('优秀')
elif 90 > score >= 80:
    print('良好')
elif 80 > score >= 70:
    print('中等')
elif 70 > score >= 60:
    print('及格')
elif 60 > score >= 0:
    print('不及格')
else:
    print('小子，别乱搞！！')





































