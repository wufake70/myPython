from django.contrib import admin

# Register your models here.
from .models import *


# 管理模型类
class TimuManager(admin.ModelAdmin):
    list_display = ['title', 'content', 'answer', 'course']
    search_fields = ['title']
    list_per_page = 100


class CourseManager(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name', 'id']
    search_fields = ['name']


admin.site.register(Course, CourseManager)
admin.site.register(TiMu, TimuManager)











