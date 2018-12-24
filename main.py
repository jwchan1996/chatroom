import os

import tornado.httpserver
import tornado.ioloop
import tornado.web

from handlers.IndexController import Index
from handlers.UserController import UserLogin, UserRegister
from handlers.WebSocketController import SocketHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', Index),
            (r'/user/login', UserLogin),
            (r'/user/register', UserRegister),
            (r'/socket', SocketHandler),
        ]

        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(8080)

    tornado.ioloop.IOLoop.instance().start()
