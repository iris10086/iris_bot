import MySQLdb
from iris_bot.plugins.consumelog.config import mysql


class mysqlOption():

    def __init__(self):
        self.host = mysql["host"]
        self.port = mysql["port"]
        self.username = mysql["username"]
        self.password = mysql["password"]
        self.database = mysql["database"]
        self.connection: MySQLdb.connections.Connection = None

    # 维护一个链接
    def getconnection(self):
        if self.connection == None:
            self.connection = MySQLdb.Connect(host=self.host,
                                              port=self.port,
                                              user=self.username,
                                              password=self.password,
                                              database=self.database)
        return self.connection

    def getcursor(self):
        return self.getconnection().cursor()

    def close(self):
        self.connection.close()

mysqloption = mysqlOption()