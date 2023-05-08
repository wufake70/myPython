# _*_coding :utf-8 _*_
# @Time :2022/8/20 14:28
# @File : 03_Ajax
# @Project : python_web

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):          # get方式 用于页面渲染 ； post方式 用于数据的提交
        self.render("")     # 渲染页面

    def post(self, *args, **kwargs):        # 表单形式提交数据，
        # print(self.get_argument('user'))   通过 input标签的name属性 获取数据
        # print(self.get_argument('pwd'))
        # self.write('登陆成功！！')         # 回显前端页面，
        # 传统网页 数据提交，网页会被全部刷新

        # 获取 JSON数据
        key1 = int(self.get_argument('key1'))
        key2 = int(self.get_argument('key2'))
        sum1 = key1 + key2
        return_data ={"result": sum1}
        self.write(return_data)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

























