# _*_coding :utf-8 _*_
# @Time :2022/7/25 14:03
# @File : 实例03_合并pdf
# @Project : python_NCRE

from os import listdir
from pprint import pprint
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfMerger

pdf_file_path = input(r'请输入PDF文件的绝对路径:')

# #合并pdf 文件
# 1.获取 需要 操作pdf文件 （同一目录下 、且顺序排好）
pdf_list = listdir(rf"{pdf_file_path}")
# print(pdf_list)
print('正在过滤 非PDF的文件')

# 过滤 不是PDF 的文件
for filename in pdf_list:
    # 匹配字符串 后缀名
    if not filename.endswith('.pdf'):
        # remove方法 指定 元素名 移除元素
        pdf_list.remove(filename)
        continue


print('请查看 文件顺序 是否符合预期')
pprint(pdf_list)
# eval(input('继续 请回车;停止 键入exit()'))     设置异常 防止程序 报错终止
try:
    eval(input('继续 请回车;停止 键入exit()'))
except SyntaxError as error:
    # print(error) 不需要展示 报错信息
    pass

# 2.使用 模块的 PdfFileWriter() 创建 新PDF
# new_pdf = PdfFileWriter()

# 使用 PdfMerger() 创建 新PDF ，并添加 目录 和 书签
merger = PdfMerger()

for i in pdf_list:
    # 打开 第一个 pdf  文件
    pdf = open(rf"{pdf_file_path}\{i}", 'rb')
    # 读取 PDF 二进制数据
    pdfRead = PdfFileReader(pdf)
    # for i_page in range(0, pdfRead.numPages):
    #     # 获取 PDF每一页 二进制数据
    #     page_content = pdfRead.getPage(i_page)
    #     # 将二进制数据 添加到 新pdf中
    #     new_pdf.addPage(page_content)       # new_pdf 变量 保存 所有的PDF 二进制数据

    # 变量 merger 保存 所有的 PDF二进制数据 ，以原文件名为目录，导入原文件书签
    merger.append(pdfRead, bookmark=f'{i.replace(".pdf", "")}', import_bookmarks=True)


new_pdf_name = input('键入新文件名:')
# 3.保存数据
with open(rf".\{new_pdf_name}.pdf", 'wb+') as fp:
    # fp.write(new_pdf)  不能往 将对象写入文件里，只能调用对象的写入方法
    merger.write(fp)

try:
    eval(input('加密 请回车；否则 exit()退出'))
except SyntaxError as fp:
    pass

# 加密处理
with open(rf".\{new_pdf_name}.pdf", 'rb+') as fp:
    # fp.write(new_pdf)  不能往 将对象写入文件里，只能调用对象的写入方法
    new_pdf_r = PdfFileReader(fp)
    new_pdf_w = PdfFileWriter()         # PdfFileWriter 对象 只能一页一页的添加 数据
    for page in range(new_pdf_r.numPages):
        new_pdf_w.addPage(new_pdf_r.getPage(page))

    new_pdf_w.encrypt('wufake')
    new_pdf_w.write(fp)


print('task over!!\n感谢使用！！')
