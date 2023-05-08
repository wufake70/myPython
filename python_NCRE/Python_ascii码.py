# _*_coding :utf-8 _*_
# @Time :2022/7/20 12:15
# @File : 测试2
# @Project : python_NCRE

# ls = [chr(i) for i in range(0, 127)]    # 128个 0到127
# print(ls)
# print(chr(33))      # ascii码 0-32 包括 127位(Del) 属于功能字符,其余全为常见字符
# ls_1 = [chr(i) for i in range(33, 127)]
# print(ls_1)

ls_symbol = [chr(i) for i in range(33, 48)]
ls_symbol_2 = [chr(i) for i in range(58, 65)]
ls_symbol_3 = [chr(i) for i in range(91, 97)]
# 英文标点符号['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
# '@', '[', '\\', ']', '^', '_', '`']
print(ls_symbol+ls_symbol_2+ls_symbol_3)

ls_num = [chr(i) for i in range(48, 58)]
print(ls_num)           # 数字['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ls_letter_upper = [chr(i) for i in range(65, 91)]
print(ls_letter_upper)  # 大写字母

ls_letter_lower = [chr(i) for i in range(97, 123)]
print(ls_letter_lower)  # 小写字母




























