'''
    dao层
    增删改查
'''
from abc import abstractmethod
import pymongo

from iris_bot.plugins.task.myutils import gettaskdict, gettaskobject, gettaskname, gettasknamebymod
from iris_bot.plugins.task.pojo import task, timelimittask
from iris_bot.plugins.task.config import tablenames


class dbOption():
    @abstractmethod
    def add(self, task):
        pass

    @abstractmethod
    def delete(self, task):
        pass

    @abstractmethod
    def modify(self, task):
        pass

    @abstractmethod
    def select(self, mod):
        pass


class Mongodb(dbOption):
    def __init__(self, host: str = "localhost", port: int = 27017, dbname: str = "iris_task_bot"):
        self.client = pymongo.MongoClient(f"mongodb://{host}:{port}")[dbname]

    def add(self, task: task):
        # 根据task查找表名
        tablename = gettaskname(task)

        table = self.client[tablename]

        table.insert_one(gettaskdict(task))

        pass

    def delete(self, task: task):
        tablename = gettaskname(task)

        self.client[tablename].delete_many(gettaskdict(task))

    def deletebyid(self, id: int, mod: int):
        tablename = gettasknamebymod(mod)
        self.client[tablename].delete_one({"_id": id})

    def modify(self, task: task):
        tablename = gettaskname(task)

        self.client[tablename].replace_one(filter={"_id": task._id},
                                           replacement=gettaskdict(task))
        pass

    def finish(self, task: task):
        tablename = gettaskname(task)

        self.client[tablename].replace_one(filter={"_id": task._id},
                                           replacement=gettaskdict(task))

    def selecttaskdb(self):
        dicts = self.select(tablenames["task"])
        list = []
        for attr in dicts:
            list.append(gettaskobject(timelimittask(), attr))
        return list

    def selecttimetaskdb(self):
        dicts = self.select(tablenames["timetask"])
        list = []
        for attr in dicts:
            list.append(gettaskobject(timelimittask(), attr))
        return list

    def selecttimelimittaskdb(self):
        dicts = self.select(tablenames["timelimittask"])
        list = []
        for attr in dicts:
            list.append(gettaskobject(timelimittask(), attr))
        return list

    def selectall(self):
        list = []
        list.extend(self.selecttaskdb())
        list.extend(self.selecttimetaskdb())
        list.extend(self.selecttimelimittaskdb())
        return list

    def select(self, tablename="*"):
        return self.client[tablename].find()


mongo = Mongodb()

if __name__ == '__main__':
    import pojo
    import datetime

    t = pojo.timelimittask(6, "test", "this is a test", datetime.datetime(year=2022, month=9, day=23))
    mongo = Mongodb()
    mongo.add(t)
    # list = mongo.selecttimelimittaskdb()
    # print(list)
    print("finished")
