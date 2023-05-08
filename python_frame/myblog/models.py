from django.db import models


# Create your models here.

# 用户表
class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return f"id={self.id},name={self.name}  "


class BlogInfo(models.Model):
    # id 自动生成
    title = models.CharField(max_length=100)
    content = models.TextField()
    # blog 被浏览的次数
    views = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"id={self.id},title={self.title},content={self.content},views={self.views},create_time={self.create_time},update_time={self.update_time},author={self.author}  "


# 浏览次数
class BlogViews(models.Model):

    info = models.OneToOneField('BlogInfo', on_delete=models.CASCADE)
    view = models.IntegerField(default=0)

    def __str__(self):
        return f"id={self.id},info={self.info},view={self.view}"


