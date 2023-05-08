# _*_coding :utf-8 _*_
# @Time :2022/7/12 11:07
# @File : 004_组合数据类型
# @Project : python_NCRE

"""
组合数据类型： 是指能将多个数据（元素）组合起来
有 列表 元祖 字典 集合 **字符串**

列表 list 常用方法
    append() 方法：用于向列表末尾添加一个新元素，只能添加非一个参数。
    extend() 方法：用于 将一个列表中的元素 添加到该列表的末尾。
    insert() 方法：用于在列表中插入一个新元素，可以指定插入的位置。
    remove() 方法：用于从列表中删除 一个指定的元素，没有就报错。
    pop() 方法：用于从列表中删除末尾元素，并返回该元素的值，也可以传入 索引值 进行删除。
    index() 方法：用于查找 一个元素在列表中 第一次出现的位置，没有就报错，不存在 ls.index("a",0)。
    count() 方法：用于计算一个元素在列表中出现的次数。
    sort() 方法：用于对列表进行排序(只针对数值，其余会报错)。
    reverse() 方法：用于将列表中的元素反转。
    copy() 方法：用于创建一个列表的副本,不是同一个对象。

    去重操作保留原顺序并统计其频率， 不使用 集合
        a = []
        b = []  # 计数容器
        for i in ls:
            if i not in a:
                a.append(i)
                b.append(ls.count(i))
    上面方法中 count方法 原理使用的循环遍历，在面临大量数据时，效率并不高，
    可以使用 字典来实现 统计出现的频率（保留原顺序）
        a = {}
        for i in ls:
            a[i] = a.get(i,0)+1
    在此基础上 实现 词频排序，
        c = list(b.items())
        c.sort(key=lambda x:x[1], reverse=True) # 这里不推荐使用 lambda函数，数据量巨大
        print(c)
        b = {}
        b.update(c)
        
        推荐使用 collection库中Counter类
        from collections import Counter
        c = Counter([...])
        d = c.most_common()     # 可以传入参数,指定前几名，返回 list,类似 [['a',33],['b',22]]

元祖 tuple 常用方法
    count(x)：返回元组中指定元素出现的次数
    index(x)：返回元组中指定元素的索引值，如果指定元素不在元组中，则抛出ValueError异常

集合 set 常用方法
    add(): 向set中添加元素，如果元素已存在则不进行任何操作。
    clear(): 清空set中的所有元素。
    copy(): 返回set的一个浅拷贝。
    remove(): 删除set中指定的元素，如果元素不存在则抛出KeyError异常
    pop(): 删除任一元素，并返回 该值

字典 dict 常用方法
    注意: 字典的键名 必须是 可哈希类型(即 不可改变对象str、num、tuple)
    clear(): 删除字典中的所有元素。
    copy(): 返回字典的一个浅拷贝。
    fromkeys(): 传入一个可迭代对象,第二个参数是 默认值
        d = {}
        d.fromkeys(['name','age'])        # {'name':None,'age':None}
    get(): 传入键名，有就返回；传入第二个参数，不存在键名 就返回参数二（默认值）

    items(): 返回字典中所有键值对的元组，dict_items([(1, 1), (2, 2), ('a', 'a')])。
    keys(): 返回字典中所有的键 dict_items类型。
    values(): 返回字典中 所有的值 dict_items类型。
        注意: 以上的 items、keys、values方法，返回的dict_items不是元组、列表、，不能索引取值，需要转换 list()、tuple();
        
    pop(key,default): 存在key 就删除，没有就返回default参数值
    setdefault(key[, default]): 返回字典中key对应的值，如果key不存在则将key和default作为键值对加入字典中并返回default
    update(): 添加键值对，
        a = {}
        a.update({1:1})     # 键值对
        a.update([(2,2)])   # 键值对序列
        a.update({(3,3)})   # 键值对序列
        print(a)
"""




































