import redis
from iris_bot.plugins.task.pojo import task
from iris_bot.plugins.task.myutils import *
from iris_bot.plugins.task.config import redisconfig

'''
    与redis缓存交互
        redis存的数据：
            三个ID，实现ID自增。
            使用hash类型存储task对象。
                key : 类型名称_ID
            删除对象，
'''


class redisOption():
    def __init__(self, host: str = "localhost", port: int = 6379, password: str = None):
        if redisconfig.get("host") and not redisconfig.get("host") == "":
            host = redisconfig.get("host")
        if redisconfig.get("port") and not redisconfig.get("port") == "":
            port = redisconfig.get("port")
        if redisconfig.get("password") and not redisconfig.get("password") == "":
            password = redisconfig.get("password")
        self.client = redis.Redis(host=host, port=port, password=password, decode_responses=True)

    def save(self, task: task):
        key = f"{gettaskname(task)}:{task._id}"
        self.client.hmset(key, gettaskdict(task))

    def getID(self):
        return self.client.incr("task_ID")


myredis = redisOption()
if __name__ == '__main__':
    import pojo

    redisOption().save(pojo.timelimittask(1, "test1", "this is a test"))
    print("finished")
