# _*_coding :utf-8 _*_
# @Time :2022/9/27 9:11
# @File : 014_Django跨域请求和油猴脚本
# @Project : python_Django

"""
跨域资源共享

一、同源策略
    规定: 请求的url地址,必须与浏览器上的url地址处于同域上,也就是域名,端口,协议相同.
    同源策略（Same origin policy）是一种约定，它是浏览器最核心也最基本的安全功能，如果缺少了同源策略，
    则浏览器的正常功能可能都会受到影响。可以说Web是构建在同源策略基础之上的，浏览器只是针对同源策略的一种实现。
    浏览器上就会报错，个就是同源策略的保护,如果浏览器对javascript没有同源策略的保护,那么一些重要的机密网站将会很危险。


二，油猴 实现 跨域发送 请求
    由于 同源策略的存在 ， 在 当前的 域下 是无法 跨域 发请求。
    方法一:（无插件）
         JSONP,CORS,反向代理

    方法二:（油猴插件）
        油猴代码:
        .......
        // @grant        GM_xmlhttpRequest
        ......
        (function() {
    'use strict';

    GM_xmlhttpRequest({
        url:"http://192.168.0.198:8000/onlinecourse/upload/",
        method :"POST",
        data:"title=1&answer=1", ******post请求的中 参数连接 也用 &。******
        headers:
        {
            "Referer": "http://192.168.0.198:8000/onlinecourse/",
            "Content-Type": "application/x-www-form-urlencoded",

            "DNT": "1",
            "Connection": "keep-alive",
            "Cookie": "sessionid=x758f8hbbooo425kyud6yfwepl3j7e02",
            "Upgrade-Insecure-Requests": "1",
        },
        onload:function(xhr){
            //alert(99)
            console.log(xhr.response); 打印返回的参数
            console.log(JSON.parse(xhr.response).message) // 获取 返回的JSON 数据的 message属性。
            console.log('跨域请求成功')
        }
        });
    })();


三、django 接收 跨域请求
    上述设置 可以使我们实现 跨域发请求，但是 当django接收到 该(跨域)请求时，
    会校验 csrf_token(防止跨域请求伪造而设置 令牌 校验，是通过 中间件实现的。)，
    此时 请求 仍是失败的。

    方法一:
        我们可以将 校验 csrf_token中间件('django.middleware.csrf.CsrfViewMiddleware') 注释掉,
        此方法 会让 网站 数据 传输 变得 不安全。(不建议)

    方法二:
        使用 装饰器
        @csrf_exempt  # (局部)取消CSRF_token校验，有利于 (在该路由下)跨域资源共享

        注意: 当我们在使用 类视图时 如要单独 导入 method_decorator 方法，
            将上面 csrf_exempt 装饰器 进行转换
        from django.utils.decorators import method_decorator

        @method_decorator(csrf_exempt, name='dispatch')
        类视图代码 ......







































"""