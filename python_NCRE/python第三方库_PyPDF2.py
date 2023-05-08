# _*_coding :utf-8 _*_
# @Time :2022/7/25 10:14
# @File : python第三方库_PyPDF2
# @Project : python_NCRE


import PyPDF2


"""
import PyPDF2
import os

# 以二进制 打开 PDF 文件
pdf = open(r"C:\\Users\yui\Desktop\my-python\python_ubuntu_progress\MySQL\第00章_写在前面.pdf", 'rb')
# 获取 该PDF文件的PdfFileReader 对象，读取 PDF 数据
pdfreader = PyPDF2.PdfFileReader(pdf)
# PDF 页数
page_num = pdfreader.numPages
# print(page_num)

# 读取第一页 txt内容
pdf_content = pdfreader.getPage(0)
pdf_txt = pdf_content.extractText()
# print(pdf_txt)

# 创建一个 PDF文件 使用 PdfFileWrite 对象
# PyPDF 模块 写入PDF的能力 ，
# 仅限于从其他 PDF中拷贝页面，旋转页面、
# 重叠页面和加密页面

# 使用 del 关键字 删除 无用变量 释放内存；
del pdf, pdf_txt, pdf_content, page_num, pdfreader
# print(pdf_txt)


# #合并pdf 文件
# 1.获取 需要 操作pdf文件 （同一目录下 、且顺序排好）
pdf_list = os.listdir(r"C:\\Users\yui\Desktop\my-python\python_ubuntu_progress\MySQL\\", )
# print(pdf_list)
# 过滤 不是PDF 的文件
for filename in pdf_list:
    # 匹配字符串 后缀名
    if not filename.endswith('.pdf'):
        # remove方法 指定 元素名 移除元素
        pdf_list.remove(filename)

# 2.使用 模块的 PdfFileWriter() 创建 新PDF
new_pdf = PyPDF2.PdfFileWriter()

# 3.1 合并PDF 并添加 目录和书签
# merger = PyPDF2.PdfMerger()

for i in pdf_list:
    # 打开 第一个 pdf  文件
    pdf = open(rf"C:\\Users\yui\Desktop\my-python\python_ubuntu_progress\MySQL\{i}", 'rb')
    # 读取 PDF 二进制数据
    pdfRead = PyPDF2.PdfFileReader(pdf)
    for i_page in range(0, pdfRead.numPages):
        # 获取 PDF每一页 二进制数据
        page_content = pdfRead.getPage(i_page)
        # 将二进制数据 添加到 新pdf中
        new_pdf.addPage(page_content)  # new_pdf 变量 保存 所有的PDF 二进制数据

    # 3.2
    # 直接将 PDF 二进制数据 加入 ，bookmark 目录，import_bookmarks 导入 原来书签
    # merger.append(PDF_binary, bookmark=f'{i.replace(".pdf", "")}', import_bookmarks=True)

# 3.保存数据
with open(rf"C:\\Users\yui\Desktop\my-python\python_ubuntu_progress\{'MySQL.pdf'}", 'wb') as fp:
    # fp.write(new_pdf)  不能往 将对象写入文件里，只能调用对象的写入方法
    new_pdf.write(fp)

print('task over!!')
"""

# PDF 解密 / 加密
# 所有的PdfFileReader 对象 多有 isEncrypted 属性 判断是否加密
pdf_bin = open(r'.\encrypt.pdf', 'rb')
pdf_file = PyPDF2.PdfFileReader(pdf_bin)
print(pdf_file.isEncrypted)

# 解密处理 使用 decrypt('密码') 函数
pdf_file.decrypt('wufake')
print(pdf_file.getPage(0))




"""
# 加密处理
with open(rf".\{new_pdf_name}.pdf", 'rb+') as fp:
    # fp.write(new_pdf)  不能往 将对象写入文件里 只能调用对象的写入方法
    new_pdf_r = PdfFileReader(fp)
    new_pdf_w = PdfFileWriter()         # PdfFileWriter 对象 只能一页一页的添加 数据
    for page in range(new_pdf_r.numPages):
        new_pdf_w.addPage(new_pdf_r.getPage(page))

    new_pdf_w.encrypt('wufake','wufake70')      # 第一个 是可读密码 第二个 是可复制 编辑 密码 
    new_pdf_w.write(fp)
"""








