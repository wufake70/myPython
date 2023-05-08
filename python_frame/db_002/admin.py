from django.contrib import admin

# 导入模型类
from .models import Academy, Student, StuInfo, Course
# 导入 auth系统 的数据表
from django.contrib.auth.models import User, Group, Permission


# 模型类 页面管理
class UsersAdmin(admin.ModelAdmin):
    pass


# 学院类 页面显示管理类
class AcademyAdmin(admin.ModelAdmin):
    # 显示 学院表的 a_id、a_name字段，
    list_display = ['a_id', 'a_name']
    # 设置 字段 可以 点击
    list_display_links = ['a_id', 'a_name']
    # 字段内容 搜索
    search_fields = ['a_name']
    # 分页显示 数据
    list_per_page = 2


# 注册模型类
# admin.site.register(Users)
admin.site.register(Academy, AcademyAdmin)   # 将对应的显示管理类 注册到相应的模型类
admin.site.register(Student)
admin.site.register(StuInfo)
admin.site.register(Course)

# admin.site.register(User)


