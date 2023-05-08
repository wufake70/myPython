import math

print('===============第一题==============')
#1.利用取整和取余一个三位数中的百位、十位、个位
num = 567
#print(num)
num_1 = num // 100
print(str(num) + '百位是:' + str(num_1))
num_2 = num // 10 % 10
print(str(num) + '十位是:' + str(num_2))
num_3 = num % 10
print(str(num) + '个位是:' + str(num_3))

print('===============第二题==============')
#2.利用字符串拼接多个字符串拼接
a = 'hello'
b = "world"
c = """i am a string
....
"""
d = ' '
#方式一：
print(a + d + d + b + ' ,' + c)
#方式二：
print('%s %s , %s' % (a, b, c))

print('===============第三题==============')
#3.一个长方体，用户提供长宽高，算出他每个面的面积
le = 4
wid = 5
hig = 6

MJ_1 = le * wid
print('他的底面积为' + str(MJ_1))
MJ_2 = le * hig
print('他的侧面积为' + str(MJ_2))
MJ_3 = wid * hig
print('他的另一个侧面积为' + str(MJ_3))

print('===============第四题==============')
#选做题：用户提供半径，算出圆的面积和周长
pi = math.pi
r = 10
#print(pi)
MJ = pi*r**2
print('圆的面积为' + str(MJ))
ZC = 2*pi*r
print('圆的周长为' + str(ZC))







