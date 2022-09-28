from iris_bot.plugins.consumelog.redis import t_type, typefactory
from iris_bot.plugins.consumelog.redis import redis_clent as redis, prefix


class typeRedis():

    def __init__(self):
        self.name = prefix + "type"
        self.client = redis

    '''
        操作缓存中的type。
            添加type到redis。
            从redis读取type。
        序列化：
            使用redis的hash 存储 id:name
    '''

    # 加入缓存
    def hset(self, type: t_type):
        self.client.hset(name=self.name,
                         mapping=typefactory.getIdNameMap(type))

    def hmset(self, types: [t_type]):
        self.client.hmset(name=self.name,
                          mapping=typefactory.getIdNameMaps(types))

    # 从缓存提取
    def hget(self, id: int) -> t_type:
        hget = self.client.hget(self.name, key=id)
        if hget:
            return t_type(id=id,
                        tname=str(hget, "utf-8"))
        return None

    # 获取所有type
    def hgetall(self) -> [t_type]:
        bitemap = redis.hgetall(self.name)
        strmap = {}
        for k, v in bitemap.items():
            strmap[int(k)] = str(v, 'utf-8')
        return typefactory.getTypesByMap(strmap)

    def delete(self, id: int):
        redis.hdel(self.name, id)


typeredis = typeRedis()

if __name__ == '__main__':
    # typeredis.hset(t_type(1, "test"))
    names = typeredis.hgetall()
    print(names)

    print(1)
