# _*_coding :utf-8 _*_
# @Time :2022/6/28 21:33
# @File : 009_装饰器和迭代器
# @Project : python_base_payment

"""
1.装饰器实质就是闭包
2.生成器就是迭代器
3.异常
"""
a = '44444'
try:
    print(int(a))

except NameError as e:
    print(f'命名错误 {e}')

except TypeError as e:
    print(f'类型错误 {e}')

except Exception as e:
    print(f'其他错误 {e}')

else:
    # try里面的代码没有异常，就执行
    print('出现异常')


# raise print('主动抛出异常')
# # 不会执行
# print(99999)

finally:
    # 不论出不出现异常 都会执行
    print('都会执行')
    print('继续执行')


assert 1==1
print('断言调试')
































