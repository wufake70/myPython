# _*_coding :utf-8 _*_
# @Time :2022/7/13 15:34
# @File : 实例001_文本词频统计
# @Project : python_NCRE
import pprint

import jieba

# 以《三国演义》

# 打开文本并读取数据
# 读取二进制数据，按照一定解码规则进行解码
txt = open(r"C:\Users\yui\Desktop\三国演义.txt", 'rb').read().decode('utf-8')
words = jieba.lcut(txt)             # 创建一个分词列表

counts = {}     # 创建一个计数字典

for word in words:
    if len(word) == 1:
        continue
    elif word in '\r\n------------……':
        continue
    elif word in '孟德曰曹操曰丞相曰':
        word = '曹操'
    elif word in '诸葛卧龙诸葛亮曰孔明曰':
        word = '诸葛亮'
    elif word in '关公曰云长曰关羽曰':
        word = '关羽'
    elif word in '玄德曰刘备曰':
        word = '刘备'
    elif word in '张飞曰翼德曰':
        word = '张飞'
    # counts[word] = counts.get(word, 0) + 1
    counts[word] = counts.setdefault(word, 0) + 1


# 去处非人名词语
non_name = {'将军', '却说', '二人', '不可', '荆州', '如此', '商议', '如何', '主公',
            '不能', '军士', '左右', '军马', '次日', '引兵', '大喜', '天下'}
for i in non_name:
    del(counts[i])

items = list(counts.items())        # 以元祖方式取出字典中的每个键值对 并全部保存为列表

# 使用列表的自定义排序功能（匿名函数），最后在反向排列
items.sort(key=lambda x: x[1], reverse=True)

# 打印频率最高的前十五
for i in items:
    if items.index(i) <= 14:
        print(f'{i[0]:*^10}{i[1]:@^10}')
    else:
        break





































