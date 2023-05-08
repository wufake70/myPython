# _*_coding :utf-8 _*_
# @Time :2022/5/9 18:32
# @File : 048-python-文件的读写
# @Project : python-base

"""
文件的写入
   write方法
   如果再次来运行这段代码，文件存在的话，会先清空原来的数据，然后在写入新的数据
   如果读取模式变为 a ，就会变成追加的模式

文件的读取
   open('file_storage/001.txt', 'r')该模式下
   read方法，效率慢
   readline 只读取一行
   readlines 读取多行（效率高）,但是会以列表的形式返回，列表中的元素是一行一行的

"""
# 写入
fp = open('file_storage/001.txt', 'a')
# 使用转义字符 \n 换行
fp.write('hello world!!\n' * 4)
fp.close()

# 读数据
fp = open('file_storage/001.txt', 'r')
# 默认情况下 read是一个字节一个字节的读去（效率慢）
# print(fp.read())

# readline 只读取一行
print(fp.readline())

# readlines 读取多行（效率高）
print(fp.readlines())



































