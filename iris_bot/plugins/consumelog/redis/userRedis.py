from iris_bot.plugins.consumelog.redis import redis_clent as redis, prefix, user, userfactory


class userRedis():

    def __init__(self):
        self.prefix = prefix

    '''
        操作缓存中的user。
            索引有两个:qq,id
            存两个键值对。
                key为QQ的value为ID
                key为ID的value为对象
            使用 hash 类型存储对象
            qqkey 使用 set
    '''

    # 存储对象
    def hset(self, user: user):
        idkey = self.prefix + f"id:{user.uid}"
        redis.hmset(name=idkey, mapping=userfactory.getmapbyuser(user))
        qqkey = self.prefix + f"qq:{user.qq_number}"
        redis.set(qqkey, idkey)

    # 获取对象
    def getUserById(self, uid) -> user:
        idkey = self.prefix + f"id:{uid}"
        return self.getUserByIdKey(idkey)

    def getUserByIdKey(self, idkey: str):
        if not redis.exists(idkey):
            return None
        user_map = redis.hgetall(idkey)
        return self.getUserByBitesMap(user_map)

    def getUserByBitesMap(self, bitesMap: {bytes}) -> user:
        tempuser = user()
        for k, v in bitesMap.items():
            key = str(k, 'utf-8')
            # 判断值的类型
            if isinstance(getattr(tempuser, key), str):
                setattr(tempuser, key, str(v, 'utf-8'))
            elif isinstance(getattr(tempuser, key), int):
                setattr(tempuser, key, int(v))
        return tempuser

    def getUserByQQ(self, qq: int):
        qqKey = self.prefix + f"qq:{qq}"
        if not redis.exists(qqKey):
            return None
        idkey = redis.get(qqKey)
        return self.getUserByIdKey(idkey)

    def deleteUser(self, user: user):
        idkey = self.prefix + f"id:{user.uid}"
        qqkey = self.prefix + f"qq:{user.qq_number}"
        self.deleteKey(idkey)
        self.deleteKey(qqkey)

    def deleteKey(self, key: str):
        if redis.exists(key):
            redis.delete(key)


userredis = userRedis()

if __name__ == '__main__':
    # userredis.hset(
    #     user(
    #         uid=1,
    #         username="testname",
    #         password="testpw",
    #         nickname="testnick",
    #         money=100,
    #         qq_number=1142542541
    #     )
    # )
    by_id = userredis.getUserByQQ(1142542541)

    print("hello")
