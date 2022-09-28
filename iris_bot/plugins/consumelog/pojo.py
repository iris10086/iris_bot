import datetime


class user():

    def __init__(self,
                 uid: int = -1,
                 username: str = "",
                 password: str = "",
                 nickname: str = "",
                 money: int = 0,
                 qq_number: int = 0, ):
        self.uid = uid
        self.username = username
        self.password = password
        self.nickname = nickname
        self.money = money
        self.qq_number = qq_number

    def subMoney(self, num: int):
        self.money -= num


class consume():
    def __init__(self,
                 id: int = 0,
                 name: str = "",
                 money: int = 0,
                 uid: int = 0,
                 tid: int = 0,
                 time=datetime.datetime.now(),
                 ):
        self.id = id
        self.name = name
        self.money = money
        self.uid = uid
        self.tid = tid
        self.time = time


class t_type():
    def __init__(self,
                 id: int = 0,
                 tname: str = ""):
        self.name = tname
        self.id = id
