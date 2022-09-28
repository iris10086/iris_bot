from iris_bot.plugins.task.pojo import task, timelimittask, timetask
from iris_bot.plugins.task.redisOption import myredis as redis

class taskfactoryc():

    def getbean(self, mod: int):
        if mod == 0:
            return task(id=redis.getID())
        elif mod == 1:
            return timetask(id=redis.getID())
        elif mod == 2:
            return timelimittask(id=redis.getID())


taskfactory = taskfactoryc()
