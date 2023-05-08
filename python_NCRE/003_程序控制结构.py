# _*_coding :utf-8 _*_
# @Time :2022/7/12 8:41
# @File : 003_程序控制结构
# @Project : python_NCRE

# 一、三种控制结构
# 顺序结构 分支结构 循环结构

# 二、分支结构
# 1.单分支结构:
# 格式：
# if 判断条件:
#   代码块

# 2.二分支结构:
# 格式:
# if ……  else……

# 3.多分枝结构:
# 格式:
# if …… elif …… elif …… else ……

# 三、循环结构
# 遍历（迭代）循环  for循环
# 条件循环          while循环
# for、while循环与 else 搭配时，循环正常结束(没有执行break语句)时，会执行else 代码块

# 四、异常处理
# 1.异常的类型:
# AssertionError    断言语句失败（assert 后的条件为假）
# AttributeError    访问的对象属性不存在
# ImportError    无法导入模块或者对象，主要是路径有误或名称错误
# IndentationError 代码没有正确对齐，主要是缩进错误
# IndexError    下标索引超出序列范围
# IOError        输入/输出异常，主要是无法打开文件
# KeyError    访问字典里不存在的键
# NameError     访问一个未声明的变量
# OverflowError    数值运算超出最大限制
# SyntaxError    python语法错误，无法解释执行的符号
# TabError    Tab和空格混用
# TypeError    不同类型数据之间的无效操作（传入对象类型与要求的不符合）
# ValueError    传入无效的值，即使值的类型是正确的
# ZeroDivisionError    除法运算中除数0 或者 取模运算中模数为0
# 一旦程序发生异常，表明该程序在执行时出现了非正常的情况，无法再执行下去。默认情况下，程序会终止退出。

# 2.处理格式:
# try:
#     可能报错的代码
# except 报错的类型 as fp:
#     print（fp）     打印报错信息 或者 直接 pass 继续程序

for i in range(3):
    print(i,end=',')
else:
    print('结束')










































