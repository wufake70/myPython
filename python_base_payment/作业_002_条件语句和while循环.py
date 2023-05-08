import random

print('==========第一题===========')
#1.利用while写出九九乘法表
i = 1

while i < 10:
    m = 1
    while m <= i:
        #使用fomat()函数
        #print()函数中，end='\t' 参数可以使所有print()输出的内容写到一行上 ,并用制表符隔开
        print(f"{m}×{i}={i*m}", end='\t')
        m+=1
    #使用print('')来阻断end='\t'将全部内容输出到一行，只对里面的while有效
    print('')
    i+=1

print('==========第二题===========')
# 2.利用while计算出100以内的奇数的总和
a = 100
js = 1
js_1 = 1
while js < a - 1:
    #使循环变量自增
    js += 2
    #计算奇数和
    js_1 = js_1 + js
print('100以内奇数和为' + str(js_1))
    

'''
#建一个列表用于接收数据
JS = ['1']
while js < a-1:
    #使循环变量自增
    js += 2
    #数字转化为列表，并追加到JS中
    js_1 = [str(js)]    #js = [str(js)]报错？
    JS.extend(js_1)     #JS.append(js_1) 不宜使用？     
    print(js)
'''

print('==========第三题===========')
#3.利用random模块中的randint方法写一个猜数字的小游戏（5次机会，猜中退出，猜大猜小，提示）
#random模块 randint(a, b) 方法可以返回随机整数 N 满足 a <= N <= b。
#print(random.randint(1, 6))

for i in range(1,6):
    aa = random.randint(1, 6)
    #查看随机数
    print(str(aa)) 
    jh = input('请随机一个数(范围1-6):')
    if int(jh) == aa:
        print('恭喜你猜中了！！')
        break
    else:
        print('你还有' + str(5-i) + '机会')

print('==========第四题===========')
#4.用户输入三个整数、判断三个整数是否可以组成一个三角形（任意两条边之和，大于另外一条边）
a = int(input('请输入第一个整数:'))
b = int(input('请输入第二个整数:'))
c = int(input('请输入第三个整数:'))

"""
错误写法：
if a < b + c & b < a + c : 
    if c < a + b:
        print('%s,%s,%s,可以组成一个三角形' % (a, b, c))
    else:
        print('%s,%s,%s, 不 可以组成一个三角形' % (a, b, c))
"""
if a == b and a == c:
    if c == b:
        print('%d,%d,%d,可以组成一个三角形' % (a, b, c))
    else:
        print('%d,%d,%d, 不 可以组成一个三角形' % (a, b, c))
elif a < (b + c) and b < (a + c) and c < (b + a):
    print('%d,%d,%d,可以组成一个三角形' % (a, b, c))
else:
    print('%d,%d,%d, 不 可以组成一个三角形' % (a, b, c))
    










