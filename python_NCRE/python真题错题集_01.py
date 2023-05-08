# _*_coding :utf-8 _*_
# @Time :2022/8/5 12:58
# @File : python真题错题集
# @Project : python_NCRE

"""
1.以下关于程序设计语言的描述，错误的选项是：
A Python语言是一种脚本编程语言
B 汇编语言是直接操作计算机硬件的编程语言 ####
C 程序设计语言经历了机器语言、汇编语言、脚本语言三个阶段  # 没有 脚本语言，加上 高级语言
D 编译和解释的区别是一次性翻译程序还是每次执行时都要翻译程序
正确答案： C

----------------------------------------------------
2.不同进制数值 写法
print(0x1e7)        0x开头 表示十六进制 , e表示 14
print(03e7)         0开头 表示十进制，3e7表示 3x10^7
print(0b10)         0b开头 表示二进制
print(0O777)        0o开拓 表示八进制

3.十进制转其他进制 函数
print(bin(3))       二进制
print(oct(9))       八进制
print(hex(17))      十六进制

4.序列类型 索引 切片
string = 'python'
print(string[:len(string))      表示取出所有内容,注意 左闭右开

5.以下选项，不属于程序流程图基本元素的是：
A 循环框
B 连接点
C 判断框
D 起始框
正确答案： A

6.字符串 进行 比较（比较运算符）
'9333' > '95990'     他会先进行 第一位字符的ascii码大小比较，……

7(易错题). 判断下列输出结果（93python22）
w = '93python22'
for x in w:
    if '0'<= x <= '9':
        continue
    else:
        print(x)
        w.replace(x, '')
print(w)
####注意：字符串为 不可变对象，w.replace(x, '')需要变量接收

8(易错题).判断返回值(0)
以下程序的输出结果是：

s = 0
def fun(num): #s 在函数内无定义。。。。。
    try:
        s += num
        return s
    except:
        return 0
    return 5
print(fun(2))
###注意:
    1.函数中 读到 return 关键字直接 返回 该值，停止函数
    2.s 为全局变量，且为不可改变对象，在函数中只能(访问)读取，不能修改，
      或使用 global 声明此变量

9.15.以下关于函数的描述，错误的是：（B）
A 函数是一种功能抽象
B 使用函数的目的只是为了增加代码复用
C 函数名可以是任何有效的Python标识符
D 使用函数后，代码的维护难度降低了

10.函数中的 默认参数 可以不用 关键字传参，可以位置传参

11.判断下列输出的结果（ ['j', 's', 'y', 'z']  ）
ss = list(set("jzzszyj"))
ss.sort()
print(ss)
###注意：set() 将序列类型 转换为 集合类型 ，自动去重，排列无序，

12.内置函数 sorted() 可以将 字符串，列表，元祖，集合 转化为列表 排序，需要标变量接受
    id() 可以查询 变量的内存 地址

13. 变量 赋给 变量，id号不变,
a = [1]
b = a
c = b.copy()
print(id(a),id(b),id(c))        # 2131859662464 2131859662464 2131859632128
#####列表的 copy() 赋给一个变量 ，id号会变
####组合数据类型 修改 任一个变量（相同id号），其余变量（同id号）也会跟着改变
z = []
b = y = z
print(id(b), id(y), id(z))
z.extend([9])               # 增加 列表的值
print(b, y, z)
----------------
kvps = {'name': 1, 'age': 2}
theCopy = kvps
kvps[' name '] = 5              # 修改 字典某个键的值
print(id(kvps), id(theCopy))
sum = kvps[' name '] + theCopy[' name ']
print(sum)


14.将字典转换 为其他类型
ls = tuple({'shandong':200, 'hebei':300, 'beijing':400}.keys())         # 指定了 将键值对的值 转换
ls = tuple({'shandong':200, 'hebei':300, 'beijing':400})            # 默认下，将键值对的的键 转换
print(ls)

15.以下关于文件的描述，错误的是： （C）
A 二进制文件和文本文件的操作步骤都是“打开-操作-关闭”
B open() 打开文件之后，文件的内容并没有在内存中
C open()只能打开一个已经存在的文件 ,         （也可以打开（创建）一个不存在的文件，
D 文件读写之后，要调用close()才能确保文件被保存在磁盘中了

16.判断输出的结果（[12, 34, 56, 78]）
img1 = [12,34,56,78]
img2 = [1,2,3,4,5]
def displ():
    print(img1)
def modi():
    # global img1
    img1 = img2     ### 在函数作用域里面，没有声明 img1 变量，不能（/使用）进行 赋值运算，
                    ### 在函数作用域里面，可以 访问 全局变量(读取该值)
modi()
displ()


17..以下关于turtle库的描述，正确的是：(C)
A 在import turtle之后就可以用circle()语句，来画一个圆圈  # 不能，先设置窗口
B 要用from turtle import turtle来导入所有的库函数      # 应为 from turtle import turtles
C home() 函数设置当前画笔位置到原点，朝向东             #
D seth(x) 是setheading(x)函数的别名，让画笔向前移动x   # 该方法设置角度

18.三木运算
x = 1
y = 4
min = x if  x<y else y
print(min)

19.字典 中 键名的类型 为 字符串、元祖、数字       （列表，字典，集合不能作为键名）

20.python 中的一行 可以写入多行命令，
   可以循环 任一组合数据类型 ，集合 会先转 列表并排序（升序）
for i in {8, 9, 3, 2, 1, }: print(i)

21.下列哪种说法是错误的? (  A )
A.除字典类型外，所有标准对象均可以用于布尔测试        # 字典也 可以做布尔测试 True
B.空字符串的布尔值是False
C.空列表对象的布尔值是False
D.值为0的任何数字对象的布尔值是False

"""


a = [1]
b = a
c = b.copy()
print(id(a),id(b),id(c))
























