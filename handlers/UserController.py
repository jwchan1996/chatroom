import json

from handlers.BaseHandler import BaseHandler
from util.DbUtil import DbUtil

dbUtil = DbUtil()


# 用户登录
class UserLogin(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        userName = self.get_argument('userName')
        password = self.get_argument('password')
        print(userName + '：' + password)
        # 查询用户
        sql = "SELECT * FROM  user WHERE name= ('%s')" % userName
        results = dbUtil.query(sql)
        # 用户不为空
        if results:
            for result in results:
                if result[2] == password:
                    self.write(json.dumps({
                        'status': 200,
                        'message': '登录成功',
                        'data': '',
                    }))
                else:
                    self.write(json.dumps({
                        'status': 412,
                        'message': '密码错误',
                        'data': '',
                    }))
                return

        self.write(json.dumps({
            'status': 413,
            'message': '用户名不存在',
            'data': '',
        }))


# 用户注册
class UserRegister(BaseHandler):
    def data_received(self, chunk):
        pass

    def post(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        userName = self.get_argument('userName')
        password = self.get_argument('password')
        print(userName + '：' + password)
        # 检查用户名是否已经注册
        sql = "SELECT * FROM  user WHERE name= ('%s')" % userName
        results = dbUtil.query(sql)
        for result in results:
            if result[1] == userName:
                self.write(json.dumps({
                    'status': 411,
                    'message': '用户名已经注册',
                    'data': '',
                }))
                return
        # 插入数据库
        sql = "INSERT  INTO user(name, password) VALUES ('%s', '%s')" % (userName, password)
        dbUtil.insert(sql)
        self.write(json.dumps({
            'status': 200,
            'message': '注册成功',
            'data': '',
        }))
