from datetime import datetime
from iris_bot.plugins.task.config import taskmod


# 普通任务  长期任务/打卡任务
class task():

    def __init__(self, id: int = -1, taskname: str = "", taskdesc: str = ""):
        self._id = id
        self.name = taskname
        self.desc = taskdesc
        self.addtime = datetime.now()
        self.isend = False
        self.mod = taskmod["task"]


# 定时任务  每天提醒
class timetask(task):

    def __init__(self,
                 id: int = -1,
                 taskname: str = "",
                 taskdesc: str = "",
                 interval: int = 0,  # 间隔时间  秒值
                 starttime: datetime = None,
                 endertime: datetime = None
                 ):
        task.__init__(self, id, taskname, taskdesc)
        self.interval = interval
        self.starttime = starttime
        self.endertime = endertime
        self.mod = taskmod["timetask"]


# 限时任务  作业之类
class timelimittask(task):
    def __init__(self,
                 id: int = -1,
                 taskname: str = None,
                 taskdesc: str = None,
                 endertime: datetime = None
                 ):
        task.__init__(self, id, taskname, taskdesc)
        self.endertime = endertime
        self.mod = taskmod["timelimittask"]
