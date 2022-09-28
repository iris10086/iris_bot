import datetime

from iris_bot.plugins.task.pojo import task, taskmod
from iris_bot.plugins.task.config import tablenames, skipprops


def gettaskdict(tasks: task) -> {}:
    return vars(tasks)


def gettaskobject(tasks: task, props: dict) -> task:
    attrs = dir(tasks)
    for attr in attrs:
        if not attr.startswith("__") and attr in props.keys():
            setattr(tasks, attr, props[attr])
    return tasks


def gettaskname(task: task):
    return gettasknamebymod(task.mod)

def gettasknamebymod(mod: int):
    for key, value in taskmod.items():
        if mod == value:
            return tablenames[key]

# 将task的转换为发送的字符串
def solvetask(task) -> str:
    taskdict = gettaskdict(task)
    msg = ""
    for k, v in taskdict.items():
        if k == "_id":
            msg += f"id:{v}\n"
        elif not v == None:
            if k in skipprops:
                continue
            if k == "endertime":
                lasttime = (v - datetime.datetime.now())
                msg += f"剩余时间:"
                if lasttime.days != 0:
                    msg += f"{lasttime.days}天\n"
                else:
                    msg += f"{int(lasttime.seconds / 3600)}小时{(int(lasttime.seconds / 60) % 60)}分钟\n"
            else:
                msg += f"{v}\n"
    return msg.strip()


def checkmodintaskmod(mod: int):
    if mod in taskmod.values():
        return True
    return False


def getspecialprop(task: task, props: [str]) -> [str]:
    msg = ""
    taskdict = gettaskdict(task)
    for k, v in taskdict.items():
        if k in props:
            msg += f"{k}:{v}\n"
    return msg.strip()