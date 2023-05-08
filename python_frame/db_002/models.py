from django.db import models


# 学院信息表
class Academy(models.Model):
    a_id = models.AutoField(primary_key=True,)
    a_name = models.CharField(max_length=20)

    def __str__(self):
        return f'a_id={self.a_id},a_name={self.a_name}'


# 学生表
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=20)
    # 设置外键(另一张表的主键)，**字段名 会自动修改为 'a_id'
    # 级联删除 on_delete=models.SET_NULL，删除学院 时，学生表 对应设置为null
    # 注意: on_delete=models.SET_NULL，null=True ，一起使用
    a = models.ForeignKey('Academy', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f's_id={self.s_id},s_name={self.s_name},a={self.a}'


# 学生详情表
class StuInfo(models.Model):
    # 级联删除 on_delete=models.CASCADE，删除学生时，学生详情表 对应 删除
    stu_id = models.OneToOneField('Student', on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.BooleanField(default=True)

    def __str__(self):
        return f'stu_id={self.stu_id},age={self.age},gender={self.gender}'


# 课程表
class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=20)
    # 表关系: 多对多,自动创建中间表
    stu = models.ManyToManyField('Student')

    def __str__(self):
        return f'c_id={self.c_id},c_name={self.c_name}'


# 创建用户注册的模型类
# class Users(models.Model):
#     pass
    # name = models.CharField(max_length=50, unique=True)
    # pwd = models.CharField(max_length=50)
    # email = models.EmailField()




























