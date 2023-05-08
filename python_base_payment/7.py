'''定义一个账户类，可以创建账户、存款、取款 、查询余额、以及销户等操作'''
from decimal import Decimal
dic = {}

class Account:
    def __init__(self,name,password,money=0):
        self.name = name
        self.password = password
        self.money = money

    def deposit(self,money):#存款
        if money >=0:#isinstance(money,(int,float))判断元素是不是int或者float类型
            Money = Decimal(str(dic[user_name1]['money']))
            Money += Decimal(str(money))
            dic[user_name1]['money'] = Money
            print('成功存款%s元，账号余额为%s元。'%(money,dic[user_name1]['money']))
        else:
            print('输入的存款金额有误，请重新存款。')

    def withdraw(self,password,money):#取款   
        if password==dic[user_name1]['password']:
            if money >=0 and money <= dic[user_name1]['money']:
                Money = Decimal(str(dic[user_name1]['money']))
                Money -= Decimal(str(money))
                dic[user_name1]['money'] = Money
                print('成功取款%s元，账号余额为%s元。'%(money,dic[user_name1]['money']))
            elif money < 0 or money > dic[user_name1]['money']:
                print('输入的取款金额有误,请重新取款。')

    def query(self):#余额查询
        print('你的账户余额为%s元。'%dic[user_name1]['money'])

    def close(self,password):#注销账户
        if  password==dic[user_name1]['password']:
            if dic[user_name1]['money'] == 0:
                dic.pop(user_name1)
                print('销户成功')
            else:
                print('你的账户还有余额%s元，请先取完余额再来进行注销.'%(dic[user_name1]['money']))

def login():
    a = Account(user_name1, pwd2)
    while True:
        number2 = input('选择你需要进行的操作1.存款 2.取款 3.余额查询 4.销户 5.退出（请选择你要进行的操作）：')
        if number2 == '1':
            if user_name1 in dic:
                Money1 = input('输入存款金额：')
                while float(Money1)<=0:
                    Money1 = input('你输入存入金额有误，请重新输入:')
                else:
                    a.deposit(money=float(Money1))
            else:
                print('你已注销，无法进行操作,请退出。')
        elif number2 == '2':
            if user_name1 in dic:
                pwd3 = input('请输入密码：')
                while pwd3 != dic[user_name1]['password']:
                    pwd3 = input('密码有误，请重新输入密码：')
                else:
                    Money2 = input('选择取款金额：')
                    while float(Money2)<=0:
                        Money2 = input('你输入存入金额有误，请重新输入:')
                    else:
                        a.withdraw(password=pwd3, money=float(Money2))
            else:
                print('你已注销，无法进行操作,请退出。')
        elif number2 == '3':
            if user_name1 in dic:
                a.query()
            else:
                print('你已注销，无法进行操作,请退出。')
        elif number2 == '4':
            if user_name1 in dic:
                pwd4 = input('请输入密码：')
                while pwd4 != dic[user_name1]['password']:
                    pwd4 = input('密码有误，请重新输入密码：')
                else:
                    a.close(password=pwd4)
                    if user_name1 not in dic:
                        print('你已注销，无法进行任何操作')
            else:
                print('你已注销，无法进行操作,请退出。')
        elif number2 == '5':
            print('退出成功')
            break

while True:
    print('------欢迎来带青椒银行------')
    number1 = input('请选择你需要进行的操作：1.开户 2.登录 3.退出 （请选择你要进行的操作）：')
    if number1 == '1':
        user_name = input('请输入账户名：')
        pwd = input('请输入密码：')
        pwd1 = input('请再次输入密码:')
        if user_name not in dic:
            while pwd != pwd1:
                print('你两次输入的密码不一致，请重新输入')
                pwd = input('请输入密码：')
                pwd1 = input('请再次输入密码:')
            else:
                print('开户成功')
                dic[user_name]={'name':user_name,'password':pwd,'money':0}

        else:
            print('您已开户，请选择登录')

    elif number1 == '2':
        user_name1 = input('请输入你的账户名：')
        if user_name1 in dic:
            pwd2 = input('请输入你的密码：')
            while user_name1 not in dic and pwd2 != dic[user_name1]['password']:
                print('你输入的账户名或者密码有误，请重新输入。')
                pwd2 = input('请输入你的密码:')
            else:
                print('登录成功')
                login()
        else:
            print('没有你的账户，请先开户。')
    elif number1 == '3':
        print('已退出，欢迎下次光临！')
        break
