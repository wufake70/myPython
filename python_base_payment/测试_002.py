# _*_coding :utf-8 _*_
# @Time :2022/6/23 17:04
# @File : 测试_002
# @Project : python_base_payment

# 验证码生成器
import string  # 导入string这个模块

print(string.digits)  # 输出包含数字0~9的字符串
print(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
print(string.ascii_lowercase)  # 包含所有小写字母的字符串
print(string.ascii_uppercase)  # 包含所有大写字母的字符串

import random


# 用range()
def code(len):
    code_list = []
    for i in range(10):  # range(0, 10)
        code_list.append(str(i))  # 生成数字
    for i in range(65, 91):       # 大写字母的ascll范围
        code_list.append(chr(i))  # 生成大写字母
    for i in range(97, 123):      # 小写字母的ascll范围
        code_list.append(chr(i))  # 生成小写字母

    print(code_list)
    r = random.sample(code_list, len)
    m = ''.join(r)
    return m


if __name__ == '__main__':
    n = code(4)
    print(n)

# 方法二：
# 用randint()
code = ''
for i in range(6):
    n = random.randint(0, 9)
    print(n)
    b = chr(random.randint(65, 90))
    print(b)
    s = chr(random.randint(97, 122))
    print(s)
    code += str(random.choices([n, b, s]))
    print(code)
print(code)
