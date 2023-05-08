# _*_coding :utf-8 _*_
# @Time :2022/6/30 17:30
# @File : 作业_008_面向对象高级2
# @Project : python_base_payment

print('===========第一题===========')
# 1.一个人他父亲名字为smith，他母亲的名字为Alice，他的名字为Tom，
# 父亲为英国人，母亲为法国人，
# 分别定义Father、Mother类，Son三个类，
# 类中分别有自己的information方法(输入对应信息)。
# 要求:在调用Son类中的information方法时，同时输入他父母的信息

# 判断 变量的 类型 第二种方法 isinstance()
# isinstance(variable, types)
# 如果前面 变量 属于 后面的类型(前面对象 是后面类型的实例化 对象) 返回 true


class Father:
    def __init__(self, name, nationality=None, father=None, mother=None):
        # 判断参数 None bool值为False
        if not bool(father):  # 
            self.name = name
            self.nationality = nationality
        else:
            self.name = name
            self.father = father
            self.nationality = self.father.nationality
            self.mother = mother

    def information(self):
        print(f'名字:{self.name}\n国籍:{self.nationality}')


class Mother:
    def __init__(self, name, nationality=None, father=None, mother=None):
        if not bool(father):
            self.name = name
            self.nationality = nationality
        else:
            self.name = name
            self.father = father
            self.nationality = self.father.nationality
            self.mother = mother

    def information(self):
        print(f'名字:{self.name}\n国籍:{self.nationality}')


class Son(Father, Mother):

    def information(self):
        print(f'名字:{self.name}\n国籍:{self.nationality}')
        print('父亲')
        self.father.information()
        print('母亲')
        self.mother.information()


Smith = Father('Smith', '英国')
Alice = Mother('Alice', '法国')
Tom = Son('Tom', None, Smith, Alice)
# Smith.information()
# Alice.information()
Tom.information()





























