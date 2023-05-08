# _*_coding :utf-8 _*_
# @Time :2022/9/28 13:15
# @File : 测试6
# @Project : python_web


from fontTools.ttLib import TTFont


def get_char_list_from_ttf(font_file):
    ' 给定font_file,获取它的中文字符 '
    f_obj = TTFont(font_file)
    m_dict = f_obj.getBestCmap()

    unicode_list = []
    for key, _ in m_dict.items():
        unicode_list.append(key)

    char_list = [chr(ch_unicode) for ch_unicode in unicode_list]
    return char_list


font_file = 'text.otf'
chars = get_char_list_from_ttf(font_file)
# print(chars)
# print(len(chars))

import execjs

print(execjs.get().name)
