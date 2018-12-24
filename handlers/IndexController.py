import tornado.web


class Index(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render('../static/html/login.html')
