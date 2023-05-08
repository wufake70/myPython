# _*_coding :utf-8 _*_
# @Time :2022/9/28 9:55
# @File : 测试4
# @Project : python_web


#coding = utf-8
from zhconv import convert
code_lib = []
scr_lib = []
real_lib = []
code = '岆嵐困嶇的任岕,岜么样的动嶴水平效峴最高?()'
scr = '俄国十月革命开辟了世界世界无产阶级社会主义革命的新时代'
for i in code:
    decode = ord(i)
    code_lib.append(decode)
for j in scr:
    decode = ord(j)
    scr_lib.append(decode)
for k in range(len(code_lib)):
    real = code_lib[k] - scr_lib[k]
    real_lib.append(real)
print(code_lib)
print(scr_lib)
print('---------差数--------')
print(real_lib)
print(decode)
decode = convert(scr,'zh-hans')
print(decode)



















