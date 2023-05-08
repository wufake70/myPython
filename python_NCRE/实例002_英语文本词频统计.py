# _*_coding :utf-8 _*_
# @Time :2022/7/13 18:30
# @File : 英语文本词频统计
# @Project : python_NCRE
import pprint


def getText():
    txt = open(r"C:\Users\yui\Desktop\哈姆雷特.txt", 'r').read()
    txt = txt.lower()
    for i in '?!@#$%^&*()''/<>.,+_=-~\n \t':
        txt.replace(i, ' ')  # 将标点符号用空格符代替
        return txt


txt_ = getText()
words = txt_.split()        # 默认情况下以空格方式切割
# print(words)
counts = {}     # 创建一个计数字典

for i in words:             # 循环计数
    counts[i] = counts.get(i, 0) + 1

# pprint.pprint(counts)
vip_word = list(counts.items())
vip_word.sort(key=lambda x: x[1], reverse=True)    # 自定义排序规则直接操作对象，不要变量赋值

# pprint.pprint(vip_word)
for i in vip_word:
    if vip_word.index(i) <= 50:
        print(i)
    else:
        break






































