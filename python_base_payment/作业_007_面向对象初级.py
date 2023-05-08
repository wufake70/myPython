# _*_coding :utf-8 _*_
# @Time :2022/6/26 17:51
# @File : 作业_007_面向对象初级
# @Project : python_base_payment
import pprint

print('=============第一题=============')
# 1.定义一个账户类，可以创建账户、存款、取款、查询余额、销户等操作。

# 创建一个字典，装入用户数据
dic = {}


# 定义一个类
class MakeAccount:
    # __init__()初始化方法，用类创建一个对象时，会自动执行
    # self 类创建的对象本身
    # 类里面的定义函数，一定要有 self参数 类对象本身
    def __init__(self, name, pwd, money_sum=0):
        self.pwd = pwd
        self.name = name
        self.money_sum = money_sum
        # 字典内在存入用户信息
        dic[self.name] = {'姓名': self.name, '余额': self.money_sum, '密码': self.pwd}
        # pprint.pprint(dic[self.name])
        # print(f'您的基本信息：\n姓名:{self.name}\n性别:{self.sex}\n年龄:{self.age}\n您的余额:{self.money_sum}')

    # 查看基本信息
    def info(self):
        print(f'您的基本信息：\n姓名:{self.name}\n性别:{self.sex}\n年龄:{self.age}\n您的余额:{self.money_sum}')

    # 定义一个存钱函数
    def storage_money(self, money_1):
        self.money_sum += money_1
        print(f'您已成功存入{self.money_sum}，您的余额为{self.money_sum}')

    # 析构 会自动执行
    # def __del__(self):
    #     print(f'感谢{self.name}的使用，您已成功销户')

    # 定义以个去钱函数
    def draw_money(self, money_2):
        if self.money_sum >= money_2:
            self.money_sum -= money_2
            print(f'您已成功取走{money_2} \n您的余额为{self.money_sum}')
        else:
            print('余额不足，请充值')


# 定义一个函数
def make_account():
    a = input('请输入您的名字：')
    a_6 = int(input('请设置您的登录密码：'))
    user_0 = MakeAccount(a, a_6)
    a_3 = int(input('请输入存款金额：'))
    user_0.storage_money(a_3)
    a_4 = int(input('请输入取款金额：'))
    user_0.draw_money(a_4)
    # 判断是否进行销户（析构）
    a_5 = input('您是否确定销户(yes 或 no):')
    if a_5 in 'yes':
        del user_0
    else:
        return


# make_account()

print('============第二题============')

# 2.现在三个人分别去开户、存款、销户、请用利用上面的类实现出来
# 小明 存入1000 销户
# 小红 存入900  销户
# 小亮 存入100  销户
"""
print('===小明的操作===')
user_1 = MakeAccount('小明', '男', 20, 1111)
user_1.storage_money(900)
del user_1
print('===小红的操作===')
user_2 = MakeAccount('小红', '女', 19, 2222)
user_2.storage_money(700)
del user_2
print('===小亮的操作===')
user_3 = MakeAccount('小亮', '男', 23, 3333)
user_3.storage_money(888)
del user_3
"""

print('============第三题============')
# 3.设置登录系统，可供用户选择账户操作


def login():
    b_1 = input('请输入序号选择操作： 1.登录 2.注册 3.退出:')
    if b_1 == '1':
        b_1 = input('请输入用户名：')
        b_2 = input('请输入您的密码：')
        if b_1 in dic:
            i = 0
            while i < 5:
                if b_2 == dic[b_1]['密码']:
                    print('成功登陆')
                    control()
                else:
                    print(f'密码错误，请重试,您还有{4-i}次机会')
                    i += 1
                    if i < 5:
                        b_2 = input('请再次输入您的密码：')
            else:
                return login()
        else:
            print('您还未注册，请选择注册')
        return login()

    elif b_1 == '2':
        print('请输入您的相关信息：')
        b_3 = input('请输入您的账号名：')
        while True:
            b_4 = input('请设置您的密码：')
            b_5 = input('请再次确认您的密码：')
            if b_3 in dic:
                print('您已有账号，请选择登录')
                return login()
            else:
                if b_5 == b_4:
                    global user_4
                    user_4 = MakeAccount(b_3, b_5)
                    print('开户成功，请重新登陆')
                    return login()
                else:
                    print('两次密码不一致，请重试')

        print('=' * 10)
    elif b_1 == '3':
        print('开始退出~~~')
        return
    else:
        print('操作错误，请重试')
        return login()


def control():
    # 全局变量声明，可改变 不可变对象变量的值
    global user_4
    c_1 = input('请选择您的操作：\n1.存款 2.取款 3.查询余额 4.销户 5.退出登录\n')
    if c_1 == '1':
        d_1 = input('请输入存款金额：')
        user_4.storage_money(float(d_1))
        print('=' * 10)
        return control()
    elif c_1 == '2':
        d_2 = input('请输入提款金额：')
        user_4.draw_money(float(d_2))
        print('=' * 10)
        return control()
    elif c_1 == '3':
        print(f'您的余额为{user_4.money_sum}')
        print('=' * 10)
        return control()
    elif c_1 == '4':
        del user_4
        print('您已成功销户')
        return login()
    elif c_1 == '5':
        print('正在退出~~')
        return login()
    else:
        print('操作失误，请重试')
        return control()


while True:
    login()

