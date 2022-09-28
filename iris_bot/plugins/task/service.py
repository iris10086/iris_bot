import datetime

from iris_bot.plugins.task.mydao import mongo, task, timelimittask
from iris_bot.plugins.task.config import taskmod

'''
    service 层
        1. 添加任务 mod指定任务类型
        2. 完成任务
        3. 删除任务
        4. 查看任务列表
        5. 获取下次定时任务时间
    维护三个列表
        
'''


def addtask(task: task):
    mongo.add(task)


def deltask(task: task):
    mongo.delete(task)


def deltaskbyid(id:int, mod:int):
    mongo.deletebyid(id,mod)


def modify(task: task):
    mongo.modify(task)


def select(mod=-1):
    if mod == -1:
        return mongo.selectall()
    if mod == 0:
        return mongo.selecttaskdb()
    elif mod == 1:
        return mongo.selecttimetaskdb()
    elif mod == 2:
        return mongo.selecttimelimittaskdb()


def selecttask():
    return select(taskmod["task"])


def selecttimetask():
    return select(taskmod["timetask"])


def selecttimelimittask():
    return select(taskmod["timelimittask"])


def takeendtime(task: timelimittask):
    return task.endertime


# 获取下次定时任务时间
def getnexttask() -> datetime:
    tasklist = selecttimelimittask()
    tasklist.sort(key=takeendtime)
    for task in tasklist:
        if not task.isend:
            return task.endertime


def finishtask(task: task):
    task.isend = True
    mongo.finish(task)


if __name__ == '__main__':
    # addtask(timelimittask(11, "timelimittask", "test desc", datetime.datetime.now()))
    # nexttask = getnexttask()
    # print(nexttask)
    # print("finished")


    l = selecttimelimittask()
    for i in l :
        print(i.name,i.endertime,i.isend)

    now = datetime.datetime.now()
    for task in l:
        if task.endertime < now:
            finishtask(task)

    l = selecttimelimittask()
    for i in l:
        print(i.name, i.endertime,i.isend)

    pass
