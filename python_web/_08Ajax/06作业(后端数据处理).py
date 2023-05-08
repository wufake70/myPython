# _*_coding :utf-8 _*_
# @Time :2022/8/20 17:00
# @File : 06作业后端
# @Project : python_web

import tornado.web
import tornado.ioloop
# tornado 框架


class MainHandler(tornado.web.RequestHandler):
    def get(self):          # get方式 用于页面渲染 ； post方式 用于数据的提交
        self.render("07轮播图.html")     # 客户端链接后 要渲染的页面html

    def post(self, *args, **kwargs):        # 获取数据
        # print(self.get_argument('key1'))
        # print(self.get_argument('key2'))
        # self.write('登陆成功！！')         # 回显前端页面，
        # 传统网页 数据提交，网页会被全部刷新

        # key1 = int(self.get_argument('key1'))
        # key2 = int(self.get_argument('key2'))
        # sum1 = key1 + key2
        # return_data ={"result": sum1}
        # self.write(return_data)
        d1 = self.get_argument('d1')
        d2 = self.get_argument('d2')
        d3 = self.get_argument('d3')
        d4 = self.get_argument('d4')
        d5 = self.get_argument('d5')
        d6 = self.get_argument('d6')
        print(f'名字:{d1}\n性别:{d6}\n密码:{d4}\n手机号:({d2}) {d3}\n个人介绍:\n{d5}')


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()






