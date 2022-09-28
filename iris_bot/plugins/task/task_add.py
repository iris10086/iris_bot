import datetime
from typing import Any, Dict, List

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import CommandArg, Arg, ArgPlainText

from iris_bot.plugins.task.factory import taskfactory
from iris_bot.plugins.task.myutils import checkmodintaskmod as checkmod
from iris_bot.plugins.task.service import addtask

task_add_bot = on_command(
    "addtask",
    aliases={"添加任务",
             "at"},
    block=False,
    priority=5
)


@task_add_bot.handle()
def firsthandler(matcher: Matcher, args: Message = CommandArg()):
    # 获取mod
    text = args.extract_plain_text()
    if text and text.isdigit():
        matcher.set_arg("mod", args)


def check(matcher: Matcher, mod: int, mymod: int):
    if not mod == mymod:
        matcher.skip()


@task_add_bot.got("mod", prompt="添加的任务类型\n0.每日任务\n1.定时任务\n2.限时任务")
async def add_task_getmod(matcher: Matcher, mod: Message = Arg("mod")):
    if not mod.extract_plain_text().isdigit():
        await task_add_bot.finish("类型错误哦")
    else:
        if not checkmod(int(mod.extract_plain_text())):
            await matcher.finish("输入有误")
        matcher.set_arg("mod", mod)


@task_add_bot.got("name", prompt="输入任务名称")
@task_add_bot.got("desc", prompt="输入任务描述")
async def add_task_getinfo(matcher: Matcher,
                           mod: str = ArgPlainText("mod"),
                           name: str = ArgPlainText("name"),
                           desc: str = ArgPlainText("desc")):
    mod = int(mod)
    checkmod(mod)
    check(matcher, mod, 0)
    mytask = taskfactory.getbean(mod)
    mytask.name = name
    mytask.desc = desc
    addtask(mytask)
    await task_add_bot.finish(f"添加成功 id:{mytask._id}")


# mod == 2
# 限时任务
'''
    获取结束时间
'''


@task_add_bot.got("endertime", prompt="结束时间 MM-DD-hh\nafter:xd")
async def add_task_getendertime(matcher: Matcher,
                                mod: str = ArgPlainText("mod"),
                                name: str = ArgPlainText("name"),
                                desc: str = ArgPlainText("desc"),
                                endertime: str = ArgPlainText("endertime")
                                ):
    mod = int(mod)
    check(matcher, mod, 2)
    task = taskfactory.getbean(mod)
    task.name = name
    task.desc = desc
    task.endertime = gettime(endertime)
    addtask(task)
    await task_add_bot.finish(f"添加成功 id:{task._id}")
    pass


def gettime(time: str) -> datetime.datetime:
    now = datetime.datetime.now()
    if time.startswith("after"):
        days = 0
        for i in range(len(time)):
            char = time[i]
            if char.isdigit():
                days *= 10
                days += int(char)
        time = now + datetime.timedelta(days=days)
        return time
    else:
        date = time.split("-")
        mouth = 0
        day = 0
        hour = 0
        if len(date) > 0:
            if date[0].isdigit():
                mouth = int(date[0])
        if len(date) > 1:
            if date[1].isdigit():
                day = int(date[1])
        if len(date) > 2:
            if date[2].isdigit():
                hour = int(date[2])

        return datetime.datetime(now.year, month=mouth, day=day, hour=hour)

    # mod == 1


# 定时任务
'''
    获取时间间隔，结束时间
'''


@task_add_bot.got("interval", prompt="间隔时间 d/h/s")
@task_add_bot.got("endertime", prompt="结束时间 MM-DD-hh\nafter:xd")
async def add_task_gettime(matcher: Matcher):
    mod = int(matcher.get_arg("mod"))
    check(matcher, mod, 1)
    await matcher.finish("暂为完善定时任务功能")
    pass
