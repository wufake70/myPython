"""
1.打开文件：使用open函数来打开文件，可以指定文件名、文件模式等参数。
    file = open("filename", "mode")
    with open("filename","mode",encoding="utf-8") as fp: ...
    其中，filename是要打开的文件名，encoding 表示使用编码方式打开,mode是打开文件的模式，常见的模式有：

        "r"：读取模式，打开文件后只能读取文件内容。
        "w"：写入模式，打开文件后可以向文件中写入数据，如果文件不存在则会创建一个新文件，如果文件已经存在则会清空原来的内容。
        "a"：追加模式，打开文件后可以向文件中追加数据，如果文件不存在则会创建一个新文件。
        "x"：创建模式，如果文件不存在则创建一个新文件，如果文件已经存在则会报错。
        "b"：二进制模式，用于处理二进制文件，例如图片、音频等。
        "t": 文本模式，
        注意: 不指定 打开模式，默认以 "rt" 读取文本模式打开

2.读取文件内容
    使用 read() 函数来读取文件内容。例如：
    content = fp.read()  # 读取整个文件内容
    还可以使用 readline() 函数来读取一行内容，使用 readlines() 函数来读取所有行的内容。例如：
    line = fp.readline()  # 读取一行内容
    fp.readable()         # 是否可读
    lines = fp.readlines()  # 读取所有行的内容，返回一个列表，传入int参数，表示读取多少行

3.写入
    fp.write()
    fp.writelines() 写入一行

4. type(fp) 返回 <class '_io.TextIOWrapper'>

5.空文件先写入，在读取
    with open("1.txt",'w+') as fp:
    fp.write("hello")
    a = fp.read()       # 文件指针随着write函数动态变化，其后面没有任何内容
    print(a)    

"""
with open("1.txt",'w+') as fp:
    fp.write("hello")
    a = fp.read()
    print(a)