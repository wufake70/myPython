from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import *


def index(request):
    return render(request, 'Online_Course/index.html')


@method_decorator(csrf_exempt, name='dispatch')
# (局部)取消CSRF_token校验，有利于 (在该路由下)跨域资源共享
class UploadAnswer(View):
    def get(self, request):
        return render(request, 'Online_Course/upload.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        my_answer = request.POST.get('myanswer')
        isTrue = request.POST.get('isTrue') or 'true'
        last_one = request.POST.get('isLastOne') or 0
        course = request.POST.get('course')

        # 如果没有该课程 就自动 创建
        course = Course.objects.get_or_create(name=course)
        course_id = course[0].id

        # 测试
        # print(f'题目:\n{title}\n选项:\n{content}\n我的答案: {my_answer}\n课程名称: {course}        对/错: {isTrue}')

        # 存入数据库
        TiMu.objects.get_or_create(title=title, content=content, answer=my_answer, istrue=isTrue, course_id=course_id)
        # 判断 最后一个, (页面传过来的值 都是字符串)
        if last_one == '1':
            return HttpResponse(1)  # 跳转下一页

        return HttpResponse('ok')
        # message = 'hello world'
        # # 返回JSON字符串
        # return JsonResponse(data={'message': message}, safe=False)


@csrf_exempt  # (局部)取消CSRF_token校验，有利于 (在该路由下)跨域资源共享
def aa(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title, content)
    return HttpResponse('00000')


def add_course(reqeust):
    Course.objects.get_or_create(name='计算机网络技术')
    Course.objects.get_or_create(name='大学生创业基础')
    Course.objects.get_or_create(name='情绪管理')
    Course.objects.get_or_create(name='大学生职业发展与就业指导')
    Course.objects.get_or_create(name='马克思主义原理')
    Course.objects.get_or_create(name='中国近现代史纲要')
    Course.objects.get_or_create(name='从爱因斯坦到霍金的宇宙')
    Course.objects.get_or_create(name='军士理论')
    return HttpResponse('添加成功')


@method_decorator(csrf_exempt, name='dispatch')
class SearchAnswer(View):
    def get(self, request):
        return render(request, 'Online_Course/search.html')

    def post(self, request):

        sc = request.POST.get('SearchContent')

        if '*' in sc:
            # 处理 学习通 特殊字体问题
            sc1 = sc.split('*')
            result = TiMu.objects.all()
            for i in sc1:
                # print(i)
                if i == '':
                    continue
                result = result.filter(title__contains=i).all()
                # print(len(result))

                if len(result) == 1:
                    break

            result = result.values_list('title', 'content', 'answer', 'course__name', 'id')
        else:
            result = TiMu.objects.filter(title__contains=sc).values_list('title', 'content', 'answer', 'course__name', 'id')
            # result = TiMu.objects.filter().values_list('title', 'content', 'answer', 'course__name')
            # result = TiMu.objects.filter(course__name__contains=sc).values_list('title', 'content', 'answer', 'course__name')

        # 'course__name')
        result = [{'title': i[0], 'content': i[1], 'answer': i[2], 'course': i[3], 'id': i[4]} for i in result]

        # return HttpResponse('ok')
        return JsonResponse(result, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AnalysisAnswer(View):
    def get(self, request):

        return render(request, 'Online_Course/text-answer-analysis.html')

    def post(self, request):
        pass


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AnswerEdit(View):
    def get(self, request, answer_id):
        result = TiMu.objects.get(id=answer_id)

        return render(request, 'Online_Course/answer-detail-edit.html', context={'result': result})

    def post(self, request, answer_id):
        # user = request.session.get('username')
        user = request.user
        # 如果使用 auth表 来保存用户新户(并进行注册登录)，
        # 可以使用 request.user 来获取 用户名

        super_user = User.objects.get(username=user).is_superuser
        if super_user == 1:
            # answer_id = int(request.POST.get('id'))
            title = request.POST.get('title')
            content = request.POST.get('content')
            answer = request.POST.get('answer')
            result = TiMu.objects.get(id=answer_id)
            # print(f'{title}\n{content}\n{answer}')

            # 数据库修改
            result.title = title
            result.content = content
            result.answer = answer
            result.save()
            return HttpResponse('ok')
        return HttpResponse('你不是超级管理员!!!')


@login_required
def delete(request, answer_id):
    # user = request.session.get('username')
    user = request.user
    # print(user)

    super_user = User.objects.get(username=user).is_superuser
    if super_user == 1:

        result = TiMu.objects.get(id=answer_id).delete()
        return redirect('Search')

    return HttpResponse('你不是超级管理员!!!')


# 搜索 课程全部答案
@method_decorator(csrf_exempt, name='dispatch')
class SearchCourseAnswer(View):
    def get(self, request):

        return render(request, 'Online_Course/search-course-answers.html')

    def post(self, request):

        sc = request.POST.get('SearchContent')
        result = Course.objects.filter(name__contains=sc).values_list('id', 'name')
        result = [{'id': i[0], 'name': i[1]} for i in result]
        return JsonResponse(result, safe=False)


# 课程全部答案 展示
def courseshow(request, course_id):
    name = Course.objects.get(id=course_id).name
    result = TiMu.objects.filter(course_id=course_id).values_list('title', 'content', 'answer', 'course__name', 'id')

    result = [{'title': i[0], 'content': i[1], 'answer': i[2], 'course': i[3], 'id': i[4]} for i in result]

    return render(request, 'Online_Course/course-answer-show.html', context={'name': name, 'result': result})




