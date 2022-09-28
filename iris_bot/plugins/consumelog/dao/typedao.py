from iris_bot.plugins.consumelog.dao.daolib import mysql, t_type, typefactory


class typeDao():
    def __init__(self):
        self.connection = mysql.getconnection()

    # 添加type
    def add(self, type: t_type):
        cursor = self.connection.cursor()

        sql = '''
            insert into t_type values(
            %(id)s,%(type_name)s
            )
        '''

        try:
            num = cursor.execute(sql, typefactory.getmap(type))
            return num
        except Exception as e:
            print(e.args)
            return 0

    def delete(self, id: int):
        cursor = self.connection.cursor()

        sql = '''
                    delete from t_type
                    where id = %s
                '''

        try:
            num = cursor.execute(sql, [id])
            return num
        except Exception as e:
            print(e.args)
            return 0

    def modify(self, type: t_type):
        cursor = self.connection.cursor()

        sql = '''
                update t_type
                set
                    type_name = %(type_name)s
                where id = %(id)s
            '''

        try:
            num = cursor.execute(sql, typefactory.getmap(type))
            return num
        except Exception as e:
            print(e.args)
            return 0

    def findall(self) -> [type]:
        cursor = self.connection.cursor()

        sql = '''
                select * from t_type
            '''

        try:
            num = cursor.execute(sql)
            return typefactory.gettype(cursor.fetchall())
        except Exception as e:
            print(e.args)
            return 0

    def findById(self, id) -> t_type:
        cursor = self.connection.cursor()

        sql = '''
                select * from t_type
                where id = %s
            '''

        try:
            num = cursor.execute(sql, [id])
            return typefactory.gettype(cursor.fetchall())[0]
        except Exception as e:
            print(e.args)
            return None

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()


typedao = typeDao()

if __name__ == '__main__':
    pass
