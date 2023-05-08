from django.db import models

# Create your models here.


# 创建模型类， 模型类 对应表(即 创建表)
class User(models.Model):
    id = models.AutoField(primary_key=True)     # 创建id字段，并赋予主键约束
    name = models.CharField(max_length=50)      # .....
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    # 如果 新增字段 必须要用默认值
    gender = models.CharField(default='男', max_length=2)

    def __str__(self):  # 使用查询方法时，数据的展示方法
        return 'User<id=%s,name=%s,age=%s,gender=%s>' % (self.id, self.name, self.age, self.gender)


# 字段约束
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
    # 自动记录 更改 该数据的时间
    update_time = models.DateTimeField(auto_now=True)

