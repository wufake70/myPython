# _*_coding :utf-8 _*_
# @Time :2022/9/12 20:40
# @File : 007_Django操作数据库2
# @Project : python_Django

"""
1.常用的字段类型映射关系:
int     =====》IntegerField  整型
varchar =====》CharField     字符类型
longtext ====》TextField     文本类型
date    =====》DateField     日期类型
datetime ====》DateTimeField 日期事件类型
tinyint  ====》BooleanField 布尔类型，0/1形式

2.字段的常用的参数
primary_key: 指定是否为主键。
unique: 指定是否唯一。
null: 指定是否为空，默认false。
blank: 等于 true时 form 表单验证时可以为空，默认为 false。
default: 设置默认值。
DateField.auto_now: 每次修改都会将当前时间更新进去

4.字段约束（在相关的 模块目录的 models.py 文件 编写）
class FieldTest(models.Model):
    # id 字段会自动创建
    # name字段，并添加唯一约束
    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField()
    # 长文本类型 不需要设置长度
    note = models.TextField(default='这家伙很懒，什么都没有介绍。')
    # 1 代表男生，0 代表女生
    gender = models.BooleanField(default=True)
    # 第一次创建的时间
    create_time = models.DateField(auto_now_add=True)
    # 自动记录 更改 该数据的时间 ，注意: 这里更新数据时 只能 先获取数据，在使用save 方法才有效，update方法 无效
    update_time = models.DateTimeField(auto_now=True)


5.表关系的实现(，一对一，多对多)
            数据库层面               模型类层面
一对多         外键                  ForeignKeyField     （学院 对应 学生）
一对一      外键+唯一键              OneToOneField       （学生 对应 学生个人信息表）
多对多   (两个)关联表+外键+中间表     ManyToManyField     （学生 对应 选修课）
中间表自动创建


6.在models.py 模型文件 创建 相应的模型类
    # 学院信息表
    class Academy(models.Model):
        s_id = models.AutoField(primary_key=True)
        a_name = models.CharField(max_length=20)


    # 学生表
    class Student(models.Model):
        s_id = models.AutoField(primary_key=True)
        s_name = models.CharField(max_length=20)
        # 设置外键(另一张表的主键)，**字段名 会自动修改为 'a_id'
        # 级联删除 on_delete=models.SET_NULL，删除学院 时，学生表 对应设置为null
        # 注意: on_delete=models.SET_NULL，null=True ，一起使用
        a = models.ForeignKey('Academy', null=True, on_delete=models.SET_NULL)


    # 学生详情表
    class StuInfo(models.Model):
        # 级联删除 on_delete=models.CASCADE，删除学生时，学生详情表 对应 删除
        # OneToOneField 一对一 （学生 对 学生详情）
        stu_id = models.OneToOneField('Student', on_delete=models.CASCADE)
        age = models.IntegerField()
        gender = models.BooleanField(default=True)


    # 课程表
    class Course(models.Model):
        c_id = models.AutoField(primary_key=True)
        c_name = models.CharField(max_length=20)
        # ManyToManyField 多对多，自动创建中间表
        stu = models.ManyToManyField('Student')











"""