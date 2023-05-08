# _*_coding :utf-8 _*_
# @Time :2022/7/12 15:12
# @File : python标准库_turtle
# @Project : python_NCRE

import turtle

"""
turtle库绘制图形有一个基本框架:一个小海龟在坐标系中爬行，其爬行轨迹形成了绘制图形。对于小海龟来说，
有前进、后退、旋转、等爬行行为，对坐标系的探索也通过前进方向、后退方向、左侧方向
和右侧方向等小海龟自身角度方位来完成。刚开始绘制时，小海龟位于画布的正中央，此处坐标为(0, 0),
行进方向为水平右方。
"""
# 1.turtle.setup(窗口宽度， 窗口高度， 窗口左侧距离屏幕左侧的距离， 窗口顶部距离屏幕顶部距离)
# turtle.setup(1500, 800, 0, 0)

# 创建画布和画笔
# canvas = tt.Screen()
# pen = tt.Turtle()

# 画笔控制函数
# turtle.penup() 抬起画笔，之后移动画笔不会只形状 无参数
turtle.penup()
# pendown() 落下画笔，之后移动画笔将绘制图像 无参数
turtle.pendown()

# pensize() 可以用来设置画笔尺寸，
turtle.pensize(5)
# pencolor() 用来设置画笔颜色，参数可填入颜色名字（字符串），或者(r, g, b)
turtle.pencolor('red')

# fd() 形状绘制函数 别名: forward() 向前进
turtle.fd(109)
turtle.fd(-188)

# home方法: 可以将画笔回到原点，方向朝东
# goto(x,y): 将画笔移动到 指定坐标，其方向不变
# speed():  画笔加速，1~~10

# seth() 用来改变画笔绘制方向
turtle.seth(90)
turtle.fd(90)
# 也可以使用left()/right()   向 左/右 转多少度。

# circle(半径， 角度)
turtle.circle(89)   # 只设置半径将会画圆

# turtle.circle(79, )   # 绘制切点圆

# 绘制同心圆
turtle.penup()
turtle.seth(to_angle=180)   # 调整方向向左
turtle.fd(10)               # 前进 10个 单位
turtle.pendown()
turtle.seth(90)             # 调整方向向上
turtle.circle(79)           # 画圆


turtle.done()       # 避免画板闪退

























