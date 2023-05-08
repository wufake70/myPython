# _*_coding :utf-8 _*_
# @Time :2022/9/13 11:40
# @File : 008_Django操作数据库3
# @Project : python_Django

"""
++++++++++++++++++++多表之间的 数据操作+++++++++++++++++++++

from django.shortcuts import render
from django.http import HttpResponse
from .models import Academy, Student, StuInfo, Course


# 添加数据
def add(request):
    # 学院添加
    # 设置a_id的起始值 为 100001，后面一次增加
    Academy.objects.get_or_create(a_id=100001, a_name='计算机学院', )
    Academy.objects.get_or_create(a_name='数理学院', )
    Academy.objects.get_or_create(a_name='经济管理学院', )
    Academy.objects.get_or_create(a_name='机电学院', )

    # 学生添加
    Student.objects.get_or_create(s_id=10001, s_name='陈冠希', a_id=100001)
    Student.objects.get_or_create(s_name='罗志祥', a_id=100002)
    Student.objects.get_or_create(s_name='吴亦凡', a_id=100003)
    Student.objects.get_or_create(s_name='王力宏', a_id=100004)
    Student.objects.get_or_create(s_name='李易峰', a_id=100001)
    Student.objects.get_or_create(s_name='郑爽', a_id=100002)
    Student.objects.get_or_create(s_name='成龙', a_id=100003)
    Student.objects.get_or_create(s_name='李连杰', a_id=100004)

    # 学生详情表
    StuInfo.objects.get_or_create(stu_id_id=10001, age=50, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10002, age=39, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10003, age=30, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10004, age=40, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10005, age=35, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10006, age=30, gender=0)
    StuInfo.objects.get_or_create(stu_id_id=10007, age=60, gender=1)
    StuInfo.objects.get_or_create(stu_id_id=10008, age=60, gender=1)

    # 课程表
    Course.objects.get_or_create(c_id=1001, c_name='Python')
    Course.objects.get_or_create(c_name='Web')
    Course.objects.get_or_create(c_name='C++')
    Course.objects.get_or_create(c_name='Java')

# 课程与学生 中间表(对于模型类来说，我们无法直接操作 中间表)
    # c_all = Course.objects.all()  获取 全部课程
    # 单独 获取 课程
    py = Course.objects.get(c_id=1001)
    web = Course.objects.get(c_id=1002)
    c__ = Course.objects.get(c_id=1003)
    java = Course.objects.get(c_id=1004)

    # 获取 全部 学生
    s_all = Student.objects.all()

    # 通过 主键 找外键（表），给学生添加课程
    s_all.get(s_name='吴亦凡').course_set.add(py, c__)
    s_all.get(s_name='陈冠希').course_set.add(py, web)
    s_all.get(s_name='罗志祥').course_set.add(py, java, c__)
    s_all.get(s_name='王力宏').course_set.add(web, c__)
    s_all.get(s_name='李易峰').course_set.add(py, web, c__)
    s_all.get(s_name='郑爽').course_set.add(java, web, c__)
    s_all.get(s_name='成龙').course_set.add(web, c__)
    s_all[7].course_set.add(py, web, c__, java)

    return HttpResponse('数据添加成功')


# 查询
def query_data(request):
    pass
# ##一对多的查找  (学院 对 学生)

    stu = Student.objects.get(s_name='陈冠希')  # 注意: 只能使用 get方法
    # 直接通过 外键 查找 外键表 “.外键名”
    stu_academy = stu.a.a_name

    # 反向查找 与该主键关联的表，".外键表名_set"  set==》一对多
    # 查找一个学院 所有的学生， .student_set.all()
    # all_stu = Academy.objects.get(a_id=100003).student_set.all()
    all_stu = Academy.objects.get(a_id=100003).student_set.get(s_name='成龙')

# 一对一 查找  （学生 对 学生详情）
    stu = Student.objects.get(s_id=10001)
    # 反向查找 与该主键关联的表， ".外键表名" ==》一对一
    stu_info = stu.stuinfo

# 多对多 查找
    # 单独 获取 课程
    py = Course.objects.get(c_id=1001)
    web = Course.objects.get(c_id=1002)
    c__ = Course.objects.get(c_id=1003)
    java = Course.objects.get(c_id=1004)

    # 获取 全部 学生
    s_all = Student.objects.all()
    # 反向查找 与该主键关联的表，".外键表名_set"，获取某个学生 课程情况
    result = s_all[0].course_set.all()

    # 获取 一个课程 的学生人数
    # 通过 外键 查找 主键表  ".外键名"
    result = py.stu.all()

    return HttpResponse(result)


# 数据删除
def delete(request):
    pass
# 移除某个学生的 某个课程。
    stu = Student.objects.get(s_id=10001)
    py = Course.objects.get(c_id=1001)
    # result = stu.course_set.get(c_name='Python')
    # result = stu.course_set.remove(py)  # 返回None

# 清空某个学生的 课程。
    # result = stu.course_set.all()
    result = stu.course_set.clear()  # 返回None
    return HttpResponse(result)


# 数据修改; add 可以 添加，也可修改。
def modify(request):
    pass
# 学生转专业
    stu = Student.objects.get(s_id=10002)
    stu_academy = stu.a  # 数理学院
    # academy = Academy.objects.get(a_name='机电学院')
    # 给该学院 加该学生，即可完成转专业 (一对多)
    # academy.student_set.add(stu)
    # stu_academy = stu.a
    # return HttpResponse(stu_academy)
    return HttpResponse(stu_academy)


# 多表(联结)查询 (多表无关联 查询)=======》filter()
def more_query(request):
    # 查询 计算机学院 所有 学生 的 详细信息，（学院表，学生表，学生信息表）
    result = StuInfo.objects.filter(stu_id__a__a_name='计算机学院')

    # 查询 有Python课程 的学生 的学院表，(课程表，学生表，学院表)
    result = Academy.objects.filter(student__course__c_name='Python')

    # 查询 郑爽 的课程信息表
    result = Course.objects.filter(stu__s_name='郑爽')
    return HttpResponse(result)
    # return HttpResponse(academy)




def select(request):
    pass
# 聚合 查询
    # aggregate()是QuerySet的 一个终止句，他返回一个包含一些键值对的字典

    # 求年龄 总和,返回值为 字典形式 使用中括号 ['键名'] 进行取值。
    result = StuInfo.objects.all().aggregate(Sum('age'))
    result = f"所有学生的年龄总和:{result}"

    # 求平均年龄
    result = StuInfo.objects.all().aggregate(Avg('age'))
    result = f"所有学生的平均年龄:{result['age__avg']}"

    # 求统计 个数
    result = StuInfo.objects.filter(age__gte=40).aggregate(Count('age'))
    result = f"age大于等于 40的个数:{result['age__count']}"

    # 求最大
    result = StuInfo.objects.all().aggregate(Max('age'))
    result = f"年龄最大的:{result['age__max']}"

# 分组查询 annotate()
    # 安学院分组，并显示 学院的名字
    result = Student.objects.values('a__a_name').annotate(count=Count('a'))

    # F查询 对表中字段操作
    # 查询 学生ID 小于等于 学院ID 的数据
    result = Student.objects.filter(s_id__lte=F('a'))

    # Q查询
    # 查询 学生名字 为 郑爽 或 成龙 的学生
    result = Student.objects.filter(Q(s_name='郑爽') | Q(s_name='成龙'))

    return HttpResponse(result)














"""






































