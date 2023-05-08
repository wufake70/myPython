# _*_coding :utf-8 _*_
# @Time :2022/7/10 17:38
# @File : 字符串类型及操作
# @Project : python_NCRE

# 1、获取星期几字符串（书上源码）
weekStr = '星期一星期二星期三星期四星期五星期六星期七'
weekId = eval(input('请输入星期数字（1-7）:'))
pos = (weekId - 1)*3
print(weekStr[pos:pos+3])               # 索引取片段


# 2、字符串处理方法之 center （根据字符串的宽度将字符串居中处理）
print('python'.center(30, '='))

# 3、字符串处理方法之 join （在可迭代对象中除最后一个元素外，每个元素增加一个新字符
# 注意: join方法中，传入的参数必须是字符串类型，组合数据类型中 元素也必须是 字符串；
print(','.join('python'))               # 结果为 p,y,t,h,o,n

# 4、replace(old, new)：将字符串中的 old 子串替换为 new 子串,不支持正则,注意: 字符串是不改变对象，需要将其保存在变量里 a=a.replace(x,y)。
# 5、lower()：将字符串中的所有字母转换为小写。
# 6、upper()：将字符串中的所有字母转换为大写。
# 7、title(): 将字符串中每个单词(空格为分界线)的首字母大写。
# 8、strip()：删除字符串中开头和结尾的空白字符(包括空格,\n,\t,)，可以传入指定字符串。
# 9、count()：统计指定字符的出现次数
# 10、split(sep)：将字符串以 sep 分隔符分割成多个子字符串，返回一个列表，默认以空格 分割。
# 11、字符串中括号 [] 用法
#       "12345678"[-0]  第一个字符
#       "12345678"[-1]  最后一个字符
#       "12345678"[:]   全部字符
#       "12345678"[1:]  第二个到最后
#       "12345678"[:-1] 右边取不到，第一个 到 倒数第二个
#       "12345678"[0:1] 右边取不到，返回 第一个字符
#       "12345678"[0:7:1]   第一个到第六个，步长为1
#       "12345678"[::-1]    反转字符串
#       '12345678'[4::-1]   "54321"
"""
capitalize(): 将字符串的首字母大写。
startswith(substring)：判断字符串是否以 substring 开头。
endswith(substring)：判断字符串是否以 substring 结尾。
join(iterable)：将可迭代对象中的元素连接成一个字符串，可指定连接符。
splitlines()：将字符串以行为单位分割成多个子字符串，返回一个列表。
isdigit()：判断字符串是否只包含数字字符。
isalpha()：判断字符串是否只包含字母字符。
islower()：判断字符串中的字母是否全部为小写字母。
isupper()：判断字符串中的字母是否全部为大写字母。
"""

# 8、字符串的格式化 format（）方法 , {} 占位符（俗称槽）
    # '{{'.format()     输出 '{' ,{{ 类似转义字符，转义 花括号

    # # 旧版本 使用基本格式
    # print('{1}:计算机{0}的cpu占用率为{2}%'.format('2018-10-10', 'c', 10))

    # # format方法的格式控制 （槽内部对格式化的配置方式）  共六种
    # # 格式： {<参数序号>:<格式控制标记>}     ':' 引导符号
    # # 前三种可归为一类 （操作字符串类型）1.填充 （以一种字符进行填充） 2. 对齐方法 （< 向左对齐；^ 居中对齐；> 向右对齐） 3.宽度 （填充的宽度）
    # print('hello world{0:=<30}i am python'.format('python'))         # hello world python========================i am python  (向左对齐)将增加字符串放在左边
    # print('hello world{:=>30}i am python'.format('python'))          # hello world========================python i am python

    # # 新版 format 格式控制的写法
    # a = 'python'
    # print(f'hello world{a:=>30}i am python')
    # print(f'hello world{"python":=^20}i am python')

    # # 后三种可归为一类 (操作数值类型），
    
    # # 类型可以放在 格式的后面，
    # print("{0:\"^30x}".format(int(s))) 以英文双引号未填充字符，内容居中，30个宽度，数值用 小写十六进制表示

    # # <, 逗号> 数字的千位分隔符， <. 精度> 只针对于 科学计数法、小数、百分数 ，<类型> 表示将什么数据类型放入槽中
    # # 类型: 1.整数类型 有 b（二进制）o（八进制） d（十进制） x/X（小写/大写十六进制）
    # # 浮点数类型有 e/E（小/大写 以科学计数法表示）, f（以浮点数表示） %（以百分号表示）

    # print(f'{7558578458:b}, {65:c}, {7558578458:d}, {7558578458:o}, {7558578458:x}, {7558578458:X}')
    # # 结果为：111000010100001101100000100011010, A（Unicode id号 65 的字符为 A）, 7558578458, 70241540432, 1c286c11a, 1C286C11A
    # print(f'{8888:.1e}, {8888:.2E}, {8888:.3f}, {8888:.4%}')
    # # 结果为 8.9e+03, 8.89E+03, 8888.000(.3f 保留三位小数 ), 888800.0000%





























