# _*_coding :utf-8 _*_
# @Time :2022/9/28 1:17
# @File : 测试3
# @Project : python_web

from fontTools.ttLib import TTFont

font = TTFont('chaoxing.woff')
font.saveXML('chaoxing.xml')
base_map = font['cmap'].getBestCmap()
print(base_map)  # 53个键值对

new_best_map = {}
for key, value in base_map.items():  # 将键 转为 十六进制
    new_best_map[hex(key)] = value

print(new_best_map)

new_map = {  # 映射表
    "uni5AD6": "时",
    "uni5AD7": "述",
    "uni5AD8": "的",
    "uni5AD9": "碍",
    "uni5ADA": "特",
    "uni5ADB": "是",
    "uni5ADC": "经",
    "uni5ADD": "没",
    "uni5ADE": "受",
    "uni5ADF": "感",
    "uni5AE0": "表",
    "uni5AE1": "能",
    "uni5AE2": "情",
    "uni5AE3": "不",
    "uni5AE4": "绪",
    "uni5AE5": "生",
    "uni5AE6": "唤",
    "uni5AE7": "起",
    "uni5AE8": "部",
    "uni5AEA": "有",
    "uni5AEB": "外",
    "uni5AEC": "们",
    "uni5AED": "系",
    "uni5AEE": "与",
    "uni5AEF": "成",
    "uni5AF0": "为",
    "uni5AF3": "行",
    "uni5AF4": "主",
    "uni5AF5": "验",
    "uni5AF6": "体",
    "uni5AF7": "认",
    "uni5AF8": "释",
    "uni5AF9": "解",
    "uni5AFD": "茶",
    "uni5AFE": "增",
    "uni5AFF": "用",
    "uni5B01": "对",
    "uni5B02": "最",
    "uni5B03": "归",
    "uni5B04": "理",
    "uni5B05": "可",
    "uni5B06": "侣",
    "uni5B07": "合",
    "uni5B08": "并",
    "uni5B09": "一",
    "uni5B0A": "分",
    "uni5B0B": "融",
}


new_data = {}  # 重新映射 code，字符
for k,v in new_best_map.items():
    k = chr(eval(k))
    new_data[k] = new_map[v]

# print(eval('0xa'))
# print(new_data)
# for k, v in new_data.items():
#     print(ord(k) - ord(v))







# print(ord("岧") - ord('与'))
# print(ord("岞") - ord('中'))
# print(ord("岤") - ord('么'))
# print(ord("嵐") - ord('于'))
# print(ord("岷") - ord("人"))
# print(ord("岜") - ord("什"))
# print(ord("岻") - ord("从"))
# print(ord("岲") - ord("依"))
# print(ord("岮") - ord("促"))
# print(ord("岍") - ord("信"))
# print(ord("岝") - ord("你"))
# print(ord("岃") - ord("你"))
# print(ord("岋") - ord("你"))
# print(ord("岕") - ord("你"))
# print(ord("岈") - ord("你"))
# print(ord("岏") - ord("你"))
# print(ord("岆") - ord("你"))
# print(ord("岬") - ord("你"))
# print(ord("岄") - ord("你"))
# print(ord("岎") - ord("你"))
# print(ord("岫") - ord("你"))
# print(ord("岊") - ord("你"))
# print(ord("岴") - ord("你"))
# print(ord("岐") - ord("你"))
# print(ord("屽") - ord("你"))
# print(ord("岣") - ord("你"))
# print(ord("岢") - ord("你"))
# print(ord("嶴") - ord("你"))
# print(ord("岾") - ord("你"))
# print(ord("岠") - ord("你"))
# print(ord("岅") - ord("你"))
# print(ord("岶") - ord("你"))
# print(ord("峴") - ord("你"))
# print(ord("峀") - ord("你"))
# print(ord("岌") - ord("你"))
# print(ord("峂") - ord("你"))
# print(ord("屼") - ord("你"))
# print(ord("岦") - ord("你"))
# print(ord("罓") - ord("你"))
# print(ord("崠") - ord("你"))
# print(ord("岥") - ord("你"))
# print(ord("峁") - ord("你"))
# print(ord("岉") - ord("你"))
# print(ord("岵") - ord("你"))
# print(ord("岨") - ord("你"))
# print(ord("岿") - ord("你"))
# print(ord("岰") - ord("你"))
# print(ord("岟") - ord("你"))
# print(ord("岇") - ord("你"))
# print(ord("岯") - ord("你"))
# print(ord("岹") - ord("你"))
# print(ord("岺") - ord("你"))
# print(ord("嶇") - ord("你"))

print(ord("岧"))
print(hex(ord("岧")))
print(ord('与'))
print(hex(ord('与')))
print(int(0xff01))
print(int(0xff5e))
print(int(0xff5e) - int(0xff01))







