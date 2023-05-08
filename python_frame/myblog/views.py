from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def base(request):
    return render(request, 'myblog/base.html')


def index(request):
    # 最新10 篇添加的 文章
    blogs = [i for i in BlogInfo.objects.all()]
    blogs = blogs[-10:]

    # 浏览次数
    blog_views = [i.view for i in BlogViews.objects.all()][-10:]
    for a, i in enumerate(blogs, start=0):
        i.views = blog_views[a]
        # print(blog_views[a])

    blogs.reverse()  # 反向排序，功能型函数
    return render(request, 'myblog/index.html', context={'blog_list': blogs})


@login_required
# @permission_required('myblog.add_bloginfo', login_url='/db_002/register/')
def add(request):
    # 判断请求的方式 post / get
    # 页面的渲染 是 get方式 (路由访问该页面)
    if request.method == 'GET':
        # return HttpResponse('get')
        return render(request, 'myblog/add-article.html')

    elif request.method == 'POST':
        # 接收前端 的post请求 ，并将数据 存入数据库
        # title = request.POST.get('title')  # 根据 name属性
        # content = request.POST.get('content')

        title = request.POST['title']  # JSON数据 的键名
        content = request.POST['content']

        if request.is_ajax():  # 判断提交的方式 Ajax/ submit
            info = request.POST['info']
        else:
            info = 1

        # 判断 添加的文章是否存在
        result1 = BlogInfo.objects.filter(title=title)
        result2 = BlogInfo.objects.filter(content=content)

        if result1 or result2:
            # return HttpResponse('文章已存在')
            # return render(request, 'myblog/add-article.html')
            message = '文章已存在'
            return JsonResponse(message, safe=False)

        else:
            if int(info) == 0:
                message = "这是新文章"
                return JsonResponse(message, safe=False)
            else:
                author = request.POST['user']
                author = Author.objects.get(name=author).id
                blog = BlogInfo(title=title, content=content, author_id=author)
                blog.save()
                # 浏览 记录表
                blog_views = BlogViews(info_id=blog.id)
                blog_views.save()

                # 跳转到文章 列表
                # return render(request, 'myblog/article-list.html', context={'blog_list': Blog.objects.all()})
                # 重定向
                return redirect(reverse('list'))


# 文章列表展示
def article_list(request):
    # 获取数据
    blog_list = BlogInfo.objects.all()
    # 浏览 次数
    blog_views = BlogViews.objects.all()
    # 使用列表推导式 将需要的数据 提取并保存为 列表，方便 js索引取值
    blog_views = [i.view for i in blog_views]

    # 分页
    p = Paginator(blog_list, 14)
    curr_page = request.GET.get('page')  # 当前页
    try:
        pages = p.page(curr_page)

    except PageNotAnInteger:
        pages = p.page(1)  # 自动 去到最后一页

    # return render(request, 'myblog/article-list.html', context={'blog_list': blog_list,
    #                                                             'view': blog_views})
    return render(request, 'myblog/article-list.html', context={'pages': pages,
                                                                'view': blog_views})


# 删除文章（普通用户）
@login_required
# @permission_required('myblog.delete_bloginfo', login_url='')
def delete(request, blog_id):
    blog = BlogInfo.objects.get(id=blog_id).author_id
    user = request.session.get('username')
    author = Author.objects.get(name=user).id

    super_user = User.objects.get(username=user).is_superuser
    # 判断是否是原作者 或是 超级管理员
    if blog == author or super_user == 1:
        # 判断该文章 是否存在
        exist = BlogInfo.objects.get(id=blog_id)
        if exist:
            exist.delete()
            blog_list = BlogInfo.objects.all()
            # return render(request, 'myblog/article-list.html', context={'blog_list': blog_list})
            return JsonResponse(None, safe=False)

        else:
            return HttpResponse('该文文章不存在！！')
    else:
        message = '抱歉，你不是原作者或超级管理员，无权删除！！！！'
        return JsonResponse(message, safe=False)


# 文章 详情页
def detail(request, blog_id):
    blog = BlogInfo.objects.get(id=blog_id)
    # 该表的 浏览次数 增加
    blog_views = BlogViews.objects.get(info_id=blog_id)
    blog_views.view = blog_views.view + 1
    blog_views.save()

    # 博客作者
    blog_author = blog.author_id
    blog_author = Author.objects.get(id=blog_author)
    return render(request, 'myblog/article-detail.html', context={'detail': blog,
                                                                  'views': blog_views,
                                                                  'blog_author': blog_author})


@login_required
def edit(request, blog_id):
    blog = BlogInfo.objects.get(id=blog_id)
    current_user = request.session.get('username')
    if blog.author_id == Author.objects.get(name=current_user).id:
        blog_views = BlogViews.objects.get(info_id=blog_id)
        if request.is_ajax():
            blog.title = request.POST['title']
            blog.content = request.POST['content']
            blog.save()
            update_time = blog.update_time.strftime("%Y年%m月%d日 %H时%M分")
            message = '已成功修改'
            # return JsonResponse(message, safe=False)
            # 局部页面刷新 (返回 JSON数据 必须使用 data参数)
            return JsonResponse(data={"message": message,
                                      "update_time": update_time}, safe=False)
        else:
            return render(request, 'myblog/edit-article.html', context={'edit': blog,
                                                                        'views': blog_views})
    else:
        return HttpResponse('抱歉，你无权访问')

    # @login_required
    # def edit(request, blog_id, user):
    #     blog = BlogInfo.objects.get(id=blog_id)
    #     print(blog.author_id == Author.objects.get(name=user).id)
    #
    #     if blog.author_id == Author.objects.get(name=user).id:
    #     # if True:
    #         blog_views = BlogViews.objects.get(info_id=blog_id)
    #
    #         if request.is_ajax():
    #             blog.title = request.POST['title']
    #             blog.content = request.POST['content']
    #             blog.save()
    #             update_time = blog.update_time.strftime("%Y年%m月%d日 %H时%M分")
    #             message = '已成功修改'
    #             # return JsonResponse(message, safe=False)
    #             # 局部页面刷新 (返回 JSON数据 必须使用 data参数)
    #             return JsonResponse(data={"message": message,
    #                                       "update_time": update_time}, safe=False)
    #         else:
    #             return render(request, 'myblog/edit-article.html', context={'edit': blog,
    #                                                                         'views': blog_views})


# 分页处理
def page(request):
    # 定义数据
    name = ['唐僧', '孙悟空', '猪八戒', '沙和尚', 'Python', 'C++', 'Java', 'MySQL', 'JavaScript']

    # 实例化 分页对象
    p = Paginator(name, 3)
    print(p)
    print(p.count)  # 总数据数量
    print(p.num_pages)  # 分页的总数
    print(p.page_range)  # 页码范围 (从1开始)
    print(p.per_page)   # 每一页的展示的 数据数

    page1 = p.page(1)   # 第一页 数据
    page2 = p.page(2)   # .....

    print(page1.object_list)    # 获取第一页的元素列表
    print(page1.number)         # 当前页的页码
    print(page2.object_list)    # 获取第二页的元素列表

    # 方法
    print(page1.has_next())     # 判断 有没有 下一页
    print(page1.has_previous())  # 判断 上一页
    print(page1.has_other_pages())  # 判断 是否有 上一页、下一页

    print(page1.next_page_number())  # 获取下一页的页码
    # print(page1.previous_page_number())  # .....上一页
    print(page1.start_index())    # 当前页面的 第一个 数据的索引(在总数据中的索引)
    print(page1.end_index())    # 当前页面的 最后一个 数据的索引(在总数据中的索引)

    return HttpResponse('ok')

    pass

