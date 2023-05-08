# _*_coding :utf-8 _*_
# @Time :2022/7/8 21:07
# @File : 作业v_010_正则表达式regex
# @Project : python_base_payment
import re

print('===============第一题===============')
# 1.检查用户名是否由字母数字和下划线组成,字母或下划线开头 (8-16)
user = input('请输入用户名：')
rule = re.compile(r'[^\d,a-z,A-Z,_]')
rule_1 = re.compile(r'^[^a-z, A-Z,_]')         # 脱字符匹配开头 第一个字母
# print(re.findall(rule, user))             # 无匹配值 返回空列表
# print(re.search(rule, user))              # 无匹配值 返回None
# print(re.findall(rule_1, user))

if 16 >= len(user) >= 8:
    if re.findall(rule_1, user) is None:
        if re.search(rule, user) is None:
            print('用户名正确')
        else:
            print('格式错误')
    else:
        print('首字母开头错误')
else:
    print('长度在[8, 16]')


print('===============第二题==============')
# 2.检查邮箱是否符合
# 邮箱格式 谷歌:用户名@gmail.com
#          腾讯:用户名@qq.com

mailbox = input('请输入您的邮箱号:')

rule_1 = re.compile(r'([^\d, a-z, A-Z]*)@')  # 匹配用户名是否规范
rule_2 = re.compile(r'@(.*).com')  # 匹配@后面的格式是否正确
# print(re.findall(rule_1, mailbox))
# print(re.search(rule_1, mailbox))


if '@' in mailbox:
    if re.findall(rule_1, mailbox) == ['']:  # mailbox 存在@ 将返回 空字符串的列表，此时用search方法 返回的值 也不是None
        if re.search(rule_2, mailbox) is None:
            print('格式错误')
        elif re.findall(rule_2, mailbox)[0] == 'gmail':
            print('邮箱正确')
        elif re.findall(rule_2, mailbox)[0] == 'qq':
            print('邮箱正确')
        else:
            print('其他类型邮箱暂不支持')
    else:
        print('用户名编写不规范')
else:
    print('格式错误')


print('===============第三题=============')
# 3.检查用户的身份证号是否符合规范
# 前1、2位数字表⽰：所在省(直辖市、⾃治区)的代码;
# 第3、4位数字表⽰：所在地级市(⾃治州)的代码;
# 第5、6位数字表⽰：所在区(县、⾃治县、县级市)的代码;
# 第7—14位数字表⽰：出⽣年、⽉、⽇;
# 第15、16位数字表⽰：所在地的派出所的代码;
# 第17位数字表⽰性别：奇数表⽰男性(1、3、5、7、9)，偶数表⽰⼥性(0、2、4、6、8);
# 第18位数字是校检码：也有的说是个⼈信息码，不是随计算机的随机产⽣，它是⽤来检验⾝份证的正确性。校检码 可以是0—9的数字，有时也⽤x表⽰。

people_id = input('请输入您的身份证:')
rule = re.compile(r'[\d{18}]')
rule_1 = re.compile(r'\d{6}(.{8})')  # 注意年月日
rule_2 = re.compile(r'[^\d, x]')  # 判断最后一位是否合理
# print(re.findall(rule_2, people_id))
# print(re.findall(rule_1, people_id)[0][5:7])

if re.findall(rule, people_id):
    if re.findall(rule_1, people_id):
        # 判断年月日是否合理
        if 1900 <= int(re.findall(rule_1, people_id)[0][0:4]) <= 2022 and 0 <= int(
                re.findall(rule_1, people_id)[0][4:6]) <= 12 and 0 <= int(re.findall(rule_1, people_id)[0][6:8]) <= 31:
            if not re.findall(rule_2, people_id):
                print('正确格式')
            else:
                print('格式错误')
        else:
            print('格式错误')
    else:
        print('格式错误')
else:
    print('格式错误')

print('=============第四题================')
# 4.检查用户输入的手机号码是否符合规范

phone = input('请输入您的手机号:')

rule = re.compile(r'1\d{10}')
# rule_1 = re.compile(r'^[^1]')
# rule_2 = re.compile(r'')

if re.findall(rule, phone):  # 判断首数字是否为1
    print('手机号格式正确')
else:
    print('格式错误')


print('==============第四题==============')
# 5.检查用户输入的密码是否符合规范（以字符或下划线开头长度8-10）

pwd = input('请输入您的密码:')

rule = re.compile(r'^[a-z,A-Z,_]')      # 设置首字母格式
rule_1 = re.compile(r'[a-z,A-Z,_!@#$%^&*\d]{8,10}')             # 连续匹配零次即空字符串,连续匹配不满足长度范围，findall方法 即返回空列表

if 8 <= len(pwd) <= 100:
    if re.findall(rule, pwd):
        if re.findall(rule_1, pwd):
            print(re.findall(rule_1, pwd))
            print('密码正确')
        else:
            print('格式错误2')

    else:
        print('格式错误1')
else:
    print('长度超过或不足')


print('=============第六题=============')
# 6.使用正则获取文件中的文字数据

str = '''
    <div>
        <ul>
            <li>hello world</li>
            <li>同学们好！</li>
            <li>欢迎来到码趣教育</li>
        </ul>
    </div>
'''

rule = re.compile(r'li>(.*?)</li')

txt = re.findall(rule, str)
print(txt)








