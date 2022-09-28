from iris_bot.plugins.consumelog.service import t_type, typedao, typeredis


class typeServer():
    '''
    类型逻辑类
        增删改查
    '''

    def add(self, type: t_type):
        typedao.add(type)
        typeredis.hset(type)
        typedao.commit()

    def delete(self, type: t_type):
        typeredis.delete(type.id)
        typedao.delete(type.id)
        typedao.commit()

    def modify(self, type: t_type):
        typeredis.hset(type)
        typedao.modify(type)
        typedao.commit()

    def findAll(self) -> [t_type]:
        return typeredis.hgetall()

    def findById(self, id: int) -> t_type:
        return typeredis.hget(id)

    def load(self):
        typeredis.hmset(typedao.findall())

typeserver = typeServer()