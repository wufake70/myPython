# _*_coding :utf-8 _*_
# @Time :2022/5/9 20:19
# @File : 049-python-文件的序列化和反序列化
# @Project : python-base
'''
"""
通过文件的操作，我们可以将字符串写入到一个本地文件，但是，如果是一个对象（就如列表、字典、元祖等）
就无法直接写入到一个文件里，需要对这个对象进行序列化，然后才能写入到文件里。

序列化：就是一套协议，按照某种要求，把内存中的数据转化为字节序列，保存到文件里，
反之，从文件的字符序列恢复到内存中，就是反序列化
例如：
   对象==》字节序列————序列化
   字节序列==》对象————反序列化

Python中提供了JSON这个模块来实现数据的序列化和反序列化
注意：默认情况下，我们只能将字符窜写入到文件中，对象不能实现写入
"""

# 序列化的两种方式
# 1.dumps（） 转存; (注意：需要导入JSON模块进入Python中）
#
fp = open('file_storage/002.txt', 'a')
name_list = [1, 3, 3, 4, 5]
# 导入JSON模块
import json
# 序列化,将Python对象编程JSON字符串
name_list = json.dumps(name_list)
fp.write(name_list)
fp.close()
# print(fp.read())，没有在读取的模式下不能使用read（）方法读取

"""
 2.dump（）在将对象转换为字符串的同时，指定一个文件的对象，
 然后把转换后的字符串写入到这个文件里，

"""
fp = open('file_storage/003.txt', 'w')
import json
name1_list = {'name': 'wufake', 'age': '33', 'profession': 'actor'}
# 只需一步就将对象进行序列化，并存入文件中
json.dump(name1_list, fp)
# 记得关闭文件
fp.close()
'''

# # 反序列化，两种方法loads（），load（）
'''
# 注意：不论是那个方法，都只能进行一个字符串对象数据的对象转换，
多个字符串对象数据转化会报错
'''
# loads（），是加载数据，需要将数据从文件中取出来
# # 将json的字符串变成一个python的对象
# fp = open('file_storage/003.txt', 'r')
# # 此时读出文件数据类型为字符串，要将其转换为原来的对象类型
# print(fp.read())
# import json
# # 将json字符串转换为python对象
# result = json.loads(fp.read())
# print(result)

# load()的使用，
# load（），加载的是文件，
fp = open('file_storage/002.txt', 'r')
import json
# 直接读取并加载文件
result = json.load(fp)
print(result)


































