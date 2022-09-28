import datetime

from iris_bot.plugins.consumelog.dao.daolib import consume, mysql, consumefactory


class consumeDao():

    def __init__(self):
        self.connection = mysql.getconnection()

    # 添加账单
    def add(self, consume: consume) -> int:
        cursor = self.connection.cursor()

        sql = '''
            insert into t_consume values(
            %(id)s,%(name)s,%(money)s,%(time)s,%(uid)s,%(tid)s
            )
        '''
        try:
            num = cursor.execute(sql, vars(consume))
            return num
        except:
            return 0

    # 删除账单 按id删除
    def delete(self, id: int) -> int:
        cursor = self.connection.cursor()

        sql = '''
                delete from t_consume
                where id = %s
            '''
        try:
            num = cursor.execute(sql, [id])
            return num
        except Exception as e:
            print(e)
            return 0

    # 有点麻烦，应该用不到。
    def deletebytime(self,
                     starttime: datetime.datetime,
                     endtime: datetime.datetime):
        cursor = self.connection.cursor()

        sql = '''
                delete from t_consume
                where time > %(starttime)s and time < %(endtime)s
            '''
        try:
            num = cursor.execute(sql, {"starttime": starttime, "endtime": endtime})
            return num
        except Exception as e:
            print(e)
            return 0

    def deleteByUid(self, uid: int):
        cursor = self.connection.cursor()

        sql = '''
                delete from t_consume
                where uid = %s
            '''
        try:
            num = cursor.execute(sql, [uid])
            return num
        except Exception as e:
            print(e)
            return 0

    # 修改账单
    def modify(self, consume: consume):
        cursor = self.connection.cursor()

        sql = '''
                        update t_consume
                        set 
                            name = %(name)s,
                            money = %(money)s,
                            time = %(time)s,
                            uid = %(uid)s,
                            tid = %(tid)s
                        where id = %(id)s
                        '''
        try:
            num = cursor.execute(sql, consumefactory.getmapbyconsume(consume))
            return num
        except Exception as e:
            print(e)
            return 0

    def findAll(self) -> [consume]:
        cursor = self.connection.cursor()
        sql = '''
                select * from t_consume
            '''
        try:
            num = cursor.execute(sql)
            return consumefactory.getconsume(cursor.fetchall())
        except Exception as e:
            print(e)
            return []

    def findById(self, id: int) -> consume:
        cursor = self.connection.cursor()
        sql = '''
                select * from t_consume
                where id = %s
            '''
        try:
            num = cursor.execute(sql, [id])
            if num == 0:
                return None
            return consumefactory.getconsume(cursor.fetchall())[0]
        except Exception as e:
            print(e)
            return None

    def findByUid(self, id: int) -> [consume]:
        cursor = self.connection.cursor()
        sql = '''
                select * from t_consume
                where uid = %s
            '''
        try:
            num = cursor.execute(sql, [id])
            if num == 0:
                return None
            return consumefactory.getconsume(cursor.fetchall())
        except Exception as e:
            print(e)
            return None
    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()


consumedao = consumeDao()
if __name__ == '__main__':
    # consumedao.add_consume(consume(
    #     id=1,
    #     name="吃饭",
    #     money=10,
    #     uid=1,
    #     tid=0
    # ))
    # consumedao.deleteconsumebyid(1)
    print("hello")
