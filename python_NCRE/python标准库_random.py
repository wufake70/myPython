# _*_coding :utf-8 _*_
# @Time :2022/7/13 0:12
# @File : python标准库_random
# @Project : python_NCRE

import random

# random库 九个常用的函数
# 1.seed() 随机种子 只要种子相同 每次启动程序，该程序输出的随机数 都相同
# random.seed(0)
print(random.randint(0, 9))
print(random.randint(0, 9))

# 2.random.random() 生成一个[0.0, 1.0)范围内的 随机小数
print(random.random())

# 3.randint() 生成一个给定 [2,90]范围内的整数
print(random.randint(2, 90)) 

# 8.shuffle(seq) 将序列类型 元素打乱原顺序 在返回      (shuffle 洗牌,打乱顺序
print(''.join([chr(i) for i in range(65, 91)]))
upper = [chr(i) for i in range(65, 91)]
random.shuffle(upper)           # 对她 print无效 只返回None; 也不支持字符串
print(''.join(upper))           # 拼接乱序结果

# 6.choice(seq) 从序列类型中， 返回一个随机元素
print(chr(random.choice([i for i in range(65, 91)] + [i for i in range(97, 122)])))

# 7.sample(seq, k) 从pop类型中随机选取k个元素 一列表示形式返回
print(random.sample([chr(i) for i in range(65, 91)], 8))        # 伪随机数和真随机数

# 5.uniform(a, b) 生成一个[a, b]之间的随机小数
print(random.uniform(8, 9))






































