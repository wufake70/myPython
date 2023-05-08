# _*_coding :utf-8 _*_
# @Time :2022/6/27 17:06
# @File : 作业_009_面向对象高级
# @Project : python_base_payment

a = 'nihao'
if isinstance(a, str):
    print('ok')


class Person:
    def __str__(self):
        return 'i'

    def __repr__(self):
        return '3'

    # def __call__(self, *args, **kwargs):
    #     print('beidiaoyongle')


a = Person()
a


# 创建一个序列类，序列协议
class Itu:
    def __init__(self, *args):
        self.a = tuple([i for i in args])
        self.b = tuple(enumerate(self.a))

        # 再用类实例一个对象时，就会打印该对象
        print(self.a)

    def __len__(self):
        return len(self.a)

    def __getitem__(self, key):
        return self.b[key][1]

    def __repr__(self):
        return str(self.a)


tu = Itu(1, 5, 6, 0, 5, 6, 2)
print(tu[0])

for i in tu:
    print(i)

dir(iter)