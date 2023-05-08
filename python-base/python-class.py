# _*_coding :utf-8 _*_
# @Time :2022/5/18 21:53
# @File : 练习003
# @Project : python-base

# class 关键字用于创建类。
# 类就像对象构造函数。请看下面的例子，理解如何使用类创建对象。
class Person:
  name = "Bill"
  age = 63

# p1 = Person()

# print(p1.name)
# print(p1.age)
# 用类创建函数
class Person:
  # 每次使用类创建新对象时，都会自动调用 __init__() 函数
  def __init__(self, name, age):
    # self参数
    # self
    # 参数是对类的当前实例的引用，用于访问属于该类的变量。
    # 它不必被命名为
    # self，您可以随意调用它，但它必须是类中任意函数的首个参数：
    self.name = name
    self.age = age

p1 = Person("Bill", 63)

print(p1.name)
print(p1.age)


































