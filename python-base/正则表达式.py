import re
import json

# txt = "China is a great country"
# st1r = '<a href="www.baidu.com">'
# # 编写一个正则表达式
# findLink = re.compile(r'<a href="(.*?)">')
# # findall（）方法返回的是 列表对象
# a = re.findall(findLink, st1r)
# print(a)
#
# # fp = open('file_storage/正则表达式练习.txt', 'wa = json.dumps(a)
# encoding='utf-8')
# fp.write(a)

"""
re模块
compile() 提前把规则写好
findall（）匹配所有满足条件的数据，并存入列表中
sub（）替换字符串
split（）字符串切割
"""

eg_1 = 'j2sdf8222848o-_e2222hj ion ' \
       '478728222225iwkjnchi78adjkaisue9' \
       '59kn 吴签 吴\t亦凡 freestyle \n \d \s \d'
# 元字符
# 通配符（.），能匹配所有的字符，除了 \n (换行符） 除外
a = re.findall(r's', eg_1)  # 匹配所有的 s ； 这里的 r 是取消字符串的转义
a = re.findall(r'.s', eg_1)  # 匹配所有的 s字符和它前一个字符

# 正则转义（\)
# \d 表示匹配所有的数字;    \D 相反
# \s 匹配空白字符串（空格符，制表符\t，换行符\n）; \S 相反
# \w 匹配字母、数字、汉字、下划线;  \W 相反
# \. 匹配点本身
a = re.findall(r'\d', eg_1)  #
a = re.findall(r'\\d', eg_1)  # \\d 双斜杠可以取消正则的转义
a = re.findall(r'\S', eg_1)
a = re.findall(r'\W', eg_1)

# 脱字符（^） 匹配开头
a = re.findall(r'^j', eg_1)  # 匹配相应字符串，并返回，如果没有就返回空列表

# 美元符（$） 匹配结尾
a = re.findall(r'\\d$', eg_1)  # 匹配相应字符串，并返回，如果没有就返回空列表

# 大括号（{}） 连续匹配设置的字符
a = re.findall(r'2{2}', eg_1)  # 连续匹配数字 2 两次，符合的列入列表

# 大括号（{min,max}) 最少连续匹配min次，最多连续匹配max次
# {min,} 最少匹配min次，不限制最大
# {,max} 最大匹配max次，最少匹配0次，注意：0次，会返回空字符串
a = re.findall(r'2{2,5}', eg_1)  # 结果['222', '2222', '22222']

# 星号 *  ， 表示匹配零到多次
# 加号 +  ， 表示匹配1到多次
# 问号 ？ ， 表示匹配0到1次
a = re.findall(r'2*', eg_1)
a = re.findall(r'2+', eg_1)
a = re.findall(r'2?', eg_1)

eg_2 = '<div><p>hello world<p><h2>免费直播课</h2></div>'

# 默认匹配模式是以贪婪模式进行匹配的 ,尽量减少贪婪模式
# <div><p>hello world<p><h2>免费直播课</h2></div> (贪婪模式匹配最多次数)
a = re.findall(r'<.*>', eg_2)  # 匹配尖括号中的任意字符串0到多次
# 强大的 .*?  去除贪婪模式（匹配最少次数）
# ['<div>', '<p>', '<p>', '<h2>', '</h2>', '</div>']
a = re.findall(r'<.*?>', eg_2)

# 集合[] 中括号里面放要匹配的字符，注意：是单个单个字符来匹配
a = re.findall(r'[a-z0-9]', eg_1)  # 表示匹配所有的小写字母，所有的数字
a = re.findall(r'[^a-z\d]', eg_1)  # 加上 ^(脱字符) 表示取反

# 分组 小括号() 匹配分组内的数据（即只要括号中的数据）
a = re.findall(r'>(.*?)<', eg_2)

eg_3 = """<div class="ZyBottom" id="ZyBottom">
												
													
										
															
	                
                    <div class="TiMu" style="position:relative">
                        <div class="Zy_TItle clearfix">
                            <i class="fl">1</i>
                            <div class="clearfix" style="line-height: 35px; font-size: 14px;padding-right:15px;width:516px;">
								<div style="width:80%;height:100%;float:left;">
								【单选题】国防是阶级斗争的产物,它伴随着()的形成而产生。								</div>
								<div style="width:20%;height:100%;float:right;">
								
								</div>
							</div>
                        </div>
													
							<form action="http://fanyapbl.fy.chaoxing.com/questionError/addQuestion" method="post" id="questionErrorForm1" target="_blank">
							<ul class="Zy_ulTop">
    							    							    								    									<li class="clearfix"><i class="fl">A、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    军队 </a></li>
    								    							    								    									<li class="clearfix"><i class="fl">B、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    生产力 </a></li>
    								    							    								    									<li class="clearfix"><i class="fl">C、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    工人与农民 </a></li>
    								    							    								    									    										<li class="clearfix"><i class="fl">D、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    阶级与国家 </a></li>
    									    								    														</ul>
                            </form>
							<div class="Py_answer clearfix">
																<span>我的答案：D</span>
								    								        								<i class="fr dui"></i>
        																							                            </div> 
												 <!--显示答案解析-->
					
												 <!--显示答案解析-->
                    </div>
                     <!--单选题结束-->
														
										
															
	                
                    <div class="TiMu" style="position:relative">
                        <div class="Zy_TItle clearfix">
                            <i class="fl">2</i>
                            <div class="clearfix" style="line-height: 35px; font-size: 14px;padding-right:15px;width:516px;">
								<div style="width:80%;height:100%;float:left;">
								【单选题】国字的演变的过程告诉我们,国防就是国家的防务,国防与()是密不可分的。								</div>
								<div style="width:20%;height:100%;float:right;">
								
								</div>
							</div>
                        </div>
													
							<form action="http://fanyapbl.fy.chaoxing.com/questionError/addQuestion" method="post" id="questionErrorForm2" target="_blank">
							<ul class="Zy_ulTop">
    							    							    								    									<li class="clearfix"><i class="fl">A、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    男人 </a></li>
    								    							    								    									    										<li class="clearfix"><i class="fl">B、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    国家 </a></li>
    									    								    							    								    									<li class="clearfix"><i class="fl">C、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    女人 </a></li>
    								    							    								    									<li class="clearfix"><i class="fl">D、</i><a href="javascript:void(0)" class="fl" style="word-break: break-all;text-decoration: none;">    老人 </a></li>
    								    														</ul>
                            </form>
							<div class="Py_answer clearfix">
																<span>我的答案：B</span>
								    								        								<i class="fr dui"></i>
        																							                            </div> 
												 <!--显示答案解析-->
					
												 <!--显示答案解析-->
                    </div>
                     <!--单选题结束-->
														
										
															
	                
                    <div class="TiMu" style="position:relative">
                        <div class="Zy_TItle clearfix">
                            <i class="fl">3</i>
                            <div class="clearfix" style="line-height: 35px; font-size: 14px;padding-right:15px;width:516px;">
								<div style="width:80%;height:100%;float:left;">
								【判断题】国防为国家和民族提供食物保障,并为国家和民族的利益服务。()								</div>
								<div style="width:20%;height:100%;float:right;">
								
								</div>
							</div>
                        </div>
													<div class="Py_answer clearfix">
																																	<span>我的答案：<i class="font20">×</i></span>
																																	    								        								<i class="fr dui"></i>
        																							                            </div>
												 <!--显示答案解析-->
					
												 <!--显示答案解析-->
                    </div>
                     <!--单选题结束-->
														
										
															
	                
                    <div class="TiMu" style="position:relative">
                        <div class="Zy_TItle clearfix">
                            <i class="fl">4</i>
                            <div class="clearfix" style="line-height: 35px; font-size: 14px;padding-right:15px;width:516px;">
								<div style="width:80%;height:100%;float:left;">
								【判断题】<p>国家为防备和抵抗侵略，制止武装颠覆，保卫国家主权、统一，领土完整和安全所进行的军事活动，以及与军事有关的政治、经济、外交、科技、教育等方面的活动就是国防。()</p>								</div>
								<div style="width:20%;height:100%;float:right;">
								
								</div>
							</div>
                        </div>
													<div class="Py_answer clearfix">
																									<span>我的答案：<i class="font20">√</i></span>
																																    								        								<i class="fr dui"></i>
        																							                            </div>
												 <!--显示答案解析-->
					
												 <!--显示答案解析-->
                    </div>
                     <!--单选题结束-->
									            </div>

"""  # 三引号可以将字符串换行
a = re.findall(r'<div style="width:80%;height:100%;float:left;">([\W\w]*?)<', eg_3)  # 网页上存在大量的隐形的制表符 \t ,换行符 \n
# 注意： [\s\S]   [\d\D]  [\w\W]  只有以上三种才能正确匹配到内容，其余写法都获取不了

print(a)
for i in range(len(a)):
# b = a[i].strip()  去除两边的空格（网页中获取来的数据格式大多不理想）
    b = a[i]
    print(b.strip())
