from django.shortcuts import render
from django.http import HttpResponse
from .models import User, FieldTest   # 在视图文件中 导入模型文件中的 模型类(数据表)
# Create your views here.


# 向数据表中 添加数据
def add(request):

    # 方法一
    # moran = User(name='moran', age=18, city='长沙')
    # moran.save()    # 保存

    # 方法二
    # wufake = User()
    # wufake.name = 'wufake'
    # wufake.age = 24
    # wufake.city = '贵阳'
    # wufake.gender = '男'
    # wufake.save()

    # 方法三，自动保存
    # User.objects.create(name='孙悟空', age=20, city='花果山', gender='男')

    # 方法四，不会 增加 重复数据
    # User.objects.get_or_create(name='孙悟空', age=20, city='花果山', gender='男')
    # User.objects.get_or_create(name='猪八戒', age=33, city='高老庄', gender='男')

    FieldTest.objects.get_or_create(name='王立阳', age=13, gender=1, note="""大家好，我叫王力央。今年12岁了，我有很多的兴趣比如：跳绳、游泳、看
书、写字和玩耍。我喜欢的东西也很多：水果、蔬菜、大螃蟹、大龙虾。大家要多吃蔬菜
少吃油炸食品身体才能强壮、健康。""")

    FieldTest.objects.get_or_create(name='雷雨豪', age=22, gender=1, note="""我是大北街四年级二班的雷浩雨，活波可爱!就体重有点偏高一点，喜欢笑!不
爱学习!&#10;""")
    FieldTest.objects.get_or_create(name='王力宏', age=20, gender=0, note="""大家好，我是...，很高兴能和大家在同一班里学习，这是一种缘分也是一种福气.我
知道在座的各位都是很优秀出类拔萃的学生，望在以后的日子里请大家多多指教.我很喜
欢交朋友，我想和班上的每位同学都能成为朋友，为这三年写下最光辉最绚丽的一章.我
希望我们××班能成为高一年级最闪亮的一颗星星.假如我们能互相帮助，互相学习，我
相信，第一肯定是我们班，有句俗话说爱拼才会赢.在此我祝愿每位同学通过自己的努力
学习三年后都有好成绩，考上自己理想的大学.""")
    FieldTest.objects.get_or_create(name='吴亦凡', age=30, gender=0, note="""大家好，我是...，很高兴能和大家在同一班里学习，这是一种缘分也是一种福气.我
知道在座的各位都是很优秀出类拔萃的学生，望在以后的日子里请大家多多指教.我很喜
欢交朋友，我想和班上的每位同学都能成为朋友，为这三年写下最光辉最绚丽的一章.我
希望我们××班能成为高一年级最闪亮的一颗星星.假如我们能互相帮助，互相学习，我
相信，第一肯定是我们班，有句俗话说爱拼才会赢.在此我祝愿每位同学通过自己的努力
学习三年后都有好成绩，考上自己理想的大学.""")
    FieldTest.objects.get_or_create(name='李易峰', age=35, gender=1, note="""大家好!我叫李易峰，生日在7月12日。我不高也不矮，中等个。我长相并不
好看，也不丑，我爱吃梨子，我性格活泼。一副水汪汪的大眼、高挺的鼻梁、小巧可爱灵
巧的小嘴，再加上一个苹果脸，构成了一个小小的我。
我热爱科学和画画。成绩很好。喜欢：数学、语文、英语。""")
    FieldTest.objects.get_or_create(name='罗贝尔', age=6, gender=0, note="""大家好，我叫罗贝尔，今年六岁。我的爱好是滑冰，唱歌，跳舞等等。我在长
塘里小学一(四)班学习。我的好朋友有周翼、龙桢贞、何锦娴等，我最喜欢我的班级、同
学和老师啦。""")
    FieldTest.objects.get_or_create(name='成龙', age=60, gender=1)
    FieldTest.objects.get_or_create(name='李连杰', age=60, gender=1)
    return HttpResponse('数据保存成功！！')


# 查询数据
def select(request):
    # all() 返回 所有数据，以列表方式 保存
    # result = User.objects.all()
    # result = [[i.id, i.name, i.age, i.gender] for i in result]

    # filter() 条件查询
    # result = User.objects.filter(name='moran')
    # result = [[i.id, i.name, i.age, i.gender] for i in result]
    # 名字包含 ‘孙’的
    result = User.objects.filter(name__contains='孙').values()
    # name__startswith = '孙'，匹配以'孙'开头
    # name__endswith = '孙'，匹配以'孙'结尾
    # name__iendswith = '孙'，匹配以'孙'结尾，忽略大小写

    # get()  只能查询唯一的 一个(id字段)，如果 多个重复报错
    # result = User.objects.get(id=2)

    # 查询第一条
    # result = User.objects.first()
    # result = [[result.id, result.name, result.age, result.gender]]

    # 排除查询
    # result = User.objects.exclude(name='猪八戒')

    # 排序查询
    # result = User.objects.order_by('age')
    # result = User.objects.order_by('-age')  # 逆序排列
    # result = [[i.id, i.name, i.age, i.gender] for i in result]

    # 数值范围查询
    # result = User.objects.filter(age__gte=19)   # 大于等于 19岁
    # result = User.objects.filter(age__in=[18, 20])   # 等于18,20岁的

    # ##查询完并以 字典形式 返回数据, values方法
    # result = User.objects.filter(age__range=(20, 30)).values()   # 在 25~30岁

    # result = [[i.id, i.name, i.age, i.gender] for i in result]
    return HttpResponse(content={'1': result})


# 修改
def update(request):
    # 方法一，先查询，在修改
    # result = User.objects.last()
    # result.name = '沙和尚'
    # result.save()

    # 方法二
    # User.objects.filter(id=1).update(name='成龙')

    # FieldTest.objects.filter(id=1).update(name='一帆风顺')  修改的时间 无法被记录
    # result = FieldTest.objects.get(id=1)
    result = FieldTest.objects.get(id=1)
    result.name = '?????'
    result.save()

    return HttpResponse('数据修改成功')


# 删除
def delete(request):
    # 先查找获取数据，再删除
    User.objects.get(id=1).delete()

    return HttpResponse('删除成功')






















