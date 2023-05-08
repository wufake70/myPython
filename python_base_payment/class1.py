##变量：用来保存数据的容器
##变量名的命名规则：
##不能用数字开头、不能使用关键字和内置函数名
##变量名最后做到见名知意
##pig = 15
##pig = 21
##print(pig)
##print(1,end='')
####end参数表示结尾输出 默认为\n  \n表示换行
##print(2)
##False = 10
##import keyword
##print(keyword.kwlist)
##编辑模式中，需要使用变量保存结果或者内容之后，
##才可以使用print输出出来
##输入：用来接收用户输入的值
##s = input('请输入你的密码')

##int 整型
##a = -123
#type可以查看数据类型
##float 浮点型(小数)
##b = 1.2234432432
#bool 布尔型
#True:1或者存在或者不为空值
#False:0或者为空值或者不存在
##c = True,False
##print(type(c))

#运算
#a = 6
##a -= 4 #a = a+4
# a = 2

# /  除法
# // 整除  除法取整数
# %  取余   取不能整除的数
# *  乘法
# ** 幂运算(次方运算)

#Python中所有引用的符号都是英文状态下的

#字符串 str
#用引号引起来的字符，就叫做字符串
#必须用引号引起来的：字母(不包括变量)、文字
#字符串的定义:
#单引号
' '
#双引号
" "
#三引号（文本）
#可以用来注释（不能写在代码后面和前面）
#并且可以在字符串里面进行换行
#三单引号
'''三单引号
我是青椒：adfjldksjfl
dasl;kdsal;daskjdlk'''
##三双引号
"""三双引号"""

#字符串的计算
#加法 +  起拼接作用
##a = '1'
##b = '2'
##c = a+b
##print(c,type(c))
#乘法  * 字符串乘以整型  作用：复制
##a = '*'
##b = a*20
##print(b)

#字符串的凭借
#join  只能对字符串类型进行拼接
##a = 'this'
##b = 'is'
##c = 'python'
####print(' '.join([a,b,c,'!!!']))
##
###f-string 格式
##print(f'{2*4} {b} {c}',2*8)

#字符串的格式化 按照固定的格式进行输出
# % 表示占位符 站位符后接到是占位类型
#字符串占位%s、整型占位%d、浮点型占位%f
##a = 1.25
##print('%.7f'%a)

#常用模块
#浮点型之间进行计算的时候  不精确
##a = 1.1
##b = 0.9
#import 导入模块
#dicimal 高精度模块 传入的数据类型必须是字符串类型
##int(float)
##import decimal
##c = decimal.Decimal(str(a))-decimal.Decimal(str(b))
##print(c)

##pi = 3.14
##import math #math 数学模块
####math.pi
##print(pi)
##print(math.pi)
