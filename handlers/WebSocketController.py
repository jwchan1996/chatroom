import json

import tornado.websocket


class SocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()
    userNames = list()

    # 跨域
    def check_origin(self, origin):
        return True

    # 服务端接受到消息
    def on_message(self, message):
        parsedJson = json.loads(message)
        userName = parsedJson['userName']
        data = parsedJson['data']

        print(userName + ' ' + data)

        # 群发
        SocketHandler.sendToAll({
            'status': 213,
            'message': 'mass',
            'type': 'user',
            'userName': userName,
            'data': data,
        })

    # 群发消息
    @staticmethod
    def sendToAll(message):
        for client in SocketHandler.clients:
            client.write_message(json.dumps(message, ensure_ascii=False))

    # WebSocket连接打开
    def open(self):
        print('WebSocket连接打开')
        # 用户名
        userName = self.get_argument("userName")
        SocketHandler.userNames.append(userName)

        self.write_message(json.dumps({
            'status': 200,
            'message': 'WebSocket connect successfully',
            'type': 'sys',
            'userNames': SocketHandler.userNames
        }))

        SocketHandler.sendToAll({
            'status': 211,
            'message': 'joined',
            'type': 'sys',
            'userName': userName,
        })
        SocketHandler.clients.add(self)

    # WebSocket连接关闭
    def on_close(self):
        print('WebSocket连接关闭')
        # 用户名
        userName = self.get_argument("userName")
        SocketHandler.userNames.remove(userName)
        SocketHandler.clients.remove(self)

        SocketHandler.sendToAll({
            'status': 212,
            'message': 'left',
            'type': 'sys',
            'userName': userName,
        })

    def data_received(self, chunk):
        pass
