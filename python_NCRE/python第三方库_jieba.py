# _*_coding :utf-8 _*_
# @Time :2022/7/13 13:16
# @File : python第三方库_jieba
# @Project : python_NCRE

"""
Python中的标准库和第三方库: 在python安装包里的函数库为标准库，不在的为第三方库 第三方库由全球
                        各领域专业人士结合专业和兴趣 开发
jieba库: 对于一段英文文本“china is a country”，如果希望提取其中的单词，
    只需要使用字符串处理的split 即可。
    然而，对于一段中文文本，列如，‘中国是一个伟大的国家’，想要获取其中的字词
    十分困难，因为英文文本可以通过空格或者标点符号分割，而中文字词之间缺少了分隔符，
    这是中文语言的的 "分词问题"
    分词能够将上列中 分为 中国、是、一个、伟大、的、国家 等一系列词语

jieba库是Python中一个重要的 第三方 中文 分词库



"""
import jieba

print([jieba.cut('中国是一个伟大的国家，Python是最简单的程序设计语言之一')])
s = """从不易融化到火烤也不化，钟薛高，这个诞生于2018年的新消费品牌正在经历创办以来最大的舆论危机。
自带“热搜体质”的钟薛高又有新动向了。近日，在“交个朋友”直播间内官宣新公司的罗永浩现身力挺钟薛高，直言：“钟薛高这个产品做得非常好。质量没有问题，拿打火机烤钟薛高的人，肯定精神有问题。”
这位“创业界顶流”也再度将“钟薛高”送上热搜。
哲学家韩炳哲曾说：“在数字媒体时代，愤怒的浪潮通常产生于那些看起来微不足道的事件。”在如今甚嚣尘上“讨伐钟薛高”的浪潮里，很少有人知道这股情绪的起因，其实也源自一件“微不足道”的事件。
时间拨回6月12日，一位素人抖音用户对高价雪糕的吐槽引发了诸多网友的共情，也让“雪糕刺客”成为了今夏的流量密码。除了“钟薛高滚出中国市场”“反人类雪糕必须要被摧毁”等言论外，围绕钟薛高与雪糕刺客，也衍生了充满恶搞色彩和娱乐化的“雪糕文化”与“雪糕情景剧”。
舆论场中的种种现象表明，从一个普通网友的段子式吐槽到如今集体的情绪化讨伐，网友们对钟薛高的讨论显然已超出了理性的范围。
如果只凭借舆论环境，就给高价雪糕打上“贵”的原罪标签，用“全网声讨”让理性科学的讨论淹没于声浪之中，这无疑是另一种形式的暴力。
枪响之后，没有赢家。 在这个后真相时代，钟薛高不会是第一个，也不会是最后一个。让商业回归常识，让消费回归价值，这才是国货崛起与用户消费的正确打开方式。
“火烤钟薛高”背后，是情绪宣泄，还是理性讨论？
传播学学者喻国明曾谈到，在社交媒体上的公共事件讨论存在“逆火效应“。当人们遇上与自身信念抵触的观点或证据时，除非它们足以完全摧毁原信念，否则人们会忽略或反驳它们，原信念反而更加强化。
“逆火效应”导致的危害是，真相在下沉，人们却在狂欢。
重新梳理此次钟薛高事件，从6月中旬的舆情发酵期到近日的舆情高峰期，“逆火效应”也在不断显现。
结合百度搜索大数据来看，网络上对钟薛高讨论热度的高点主要集中在7月1日至7月7日期间。
"""

s = '改变了先实现农业集体化，后实现农业机械化的设想'
jieba.add_word('钟薛高')       # 向分词词典中添加新词

# jieba库中的常用的分词函数
# 1.jieba.cut(s) 精确模式 返回一个可迭代的数据类型(可迭代，只能用for循环去遍历去获取数据 不能直接输输出)
a = jieba.cut(s)        # 返回的数据 能够完整不多于的组合成原始文本
# a = list(a)         # 再将其转换为列表类型
# b = set(a)          # set（）可转换为 集合类型（有去重功能）
# c = tuple(a)          # tuple() 转换为元祖

# 2.jieba.cut(s, cut_all=True) 全模式 ，输出文本s中所有可能的分词，也不能保证全部
a = jieba.cut(s, cut_all=True)
a = list(a)
# print(a)

# 3.jieba.cut_for_search(s) 搜索引擎模式，分词效果更加细致
# a = jieba.cut_for_search(s)
a = list(a)
print(a)

# 4.lcut() lcut(s, cut_all=True) lcut_for_search()  同上 只是返回的数据类型为 列表






























