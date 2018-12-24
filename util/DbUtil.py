import pymysql


class DbUtil(object):
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='199498xy', db='mybatis',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def query(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.db.close()
