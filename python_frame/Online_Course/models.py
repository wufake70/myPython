from django.db import models

# Create your models here.


# 课程表
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Course<id={self.id},name={self.name}>'


# 总习题库
class TiMu(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=500, default=None)
    answer = models.CharField(max_length=200, default=None)
    istrue = models.CharField(max_length=10, default=None)
    course = models.ForeignKey('Course', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'TiMu<id+{self.id}title={self.title},content={self.content},answer={self.answer},istrue={self.istrue},course={self. course}>'






#
#
#
#
#
#
#
