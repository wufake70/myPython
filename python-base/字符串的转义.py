# _*_coding :utf-8 _*_
# @Time :2022/6/2 13:23
# @File : 字符串的转义
# @Project : python-base

"""
字符串的转义：反斜杠\ + 字母
再print（）中才有用
"""
# \t 水平制表符（相当于tab按键）
# \t 当它前面的字符串不满4个时，就会自动补空格键直至满4个
# 当它前面的字符串多于4个时，就用4来整除，
# 余出来的继续用空格键补齐，以达到对其效果
"""
水平制表符就是用来将文字对齐的

k       k   djoienkjtrjuier
iw      eu  hihjntreuikje
jei     ouy hjhntjkj9oie
jwio    e   uyhrtijnert'
kieuj   r   thiopertujio
"""
print('h\tworld')
print('he\tworld')
print('hel\tworld')
print('hell\tworld')
print('hello\tworld')
print('兰\t州交通大学数理学院')
print('兰州\t交通大学数理学院')
print('兰州交\t通大学数理学院')
print('兰州交通\t大学数理学院')
print('兰州交通大\t学数理学院')
print('兰州交通大学\t数理学院')
print('兰州交通大学数\t理学院')

# \n (换行符）
print('兰州交通大学\n数理学院')

















