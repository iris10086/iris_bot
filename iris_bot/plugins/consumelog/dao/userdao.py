from iris_bot.plugins.consumelog.dao.daolib import user, mysql, userfactory


class userDao():
    def __init__(self):
        self.connection = mysql.getconnection()

    # 用户注册
    def add(self, user: user) -> int:
        cursor = self.connection.cursor()

        sql = f'''
            insert into t_user values (%(uid)s,
                                        %(username)s,
                                        %(password)s,
                                        %(nickname)s,
                                        %(money)s,
                                        %(qq_number)s);      
        '''
        try:
            num = cursor.execute(sql, userfactory.getusermap(user))
            return num
        except:
            return 0

    # 查询所有user
    def findAll(self) -> [user]:
        cursor = self.connection.cursor()

        sql = '''
        select * from t_user
        '''

        try:
            num = cursor.execute(sql)
            fetchall = cursor.fetchall()

            return userfactory.getuser(fetchall)
        except Exception as e:
            return []

    # 通过id查询user
    def findById(self, id: int) -> user:
        cursor = self.connection.cursor()

        sql = '''
                select * from t_user
                where uid = %s
                '''
        try:
            num = cursor.execute(sql, [id])
            fetchall = cursor.fetchall()
            if not num == 0:
                return userfactory.getuser(fetchall)[0]
        except Exception as e:
            print(e.args)
            return None

    # 通过id删除user
    def delete(self, id: int) -> int:
        cursor = self.connection.cursor()

        sql = '''
                delete from t_user
                where uid = %s
                '''
        try:
            num = cursor.execute(sql, [id])
            return num
        except Exception as e:
            print(e)
            return 0

    # 修改user信息
    def modify(self, user: user) -> int:
        cursor = self.connection.cursor()

        sql = '''
                update t_user
                set 
                    username = %(username)s,
                    password = %(password)s,
                    nickname = %(nickname)s,
                    money = %(money)s,
                    qq_number = %(qq_number)s
                where uid = %(uid)s
                '''
        try:
            num = cursor.execute(sql, userfactory.getusermap(user))
            return num
        except Exception as e:
            print(e)
            return 0

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()


userdao = userDao()

if __name__ == '__main__':
    user_list = userdao.getuserbyid(1)
    print("hello")
