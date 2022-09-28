# 查看任务
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, Arg, ArgPlainText

from iris_bot.plugins.task.service import select
from iris_bot.plugins.task.pojo import task, timetask, timelimittask
from iris_bot.plugins.task.myutils import solvetask, gettaskdict, checkmodintaskmod as checkmod
from iris_bot.plugins.task.config import sendkeys

task_select_bot = on_command(
    "task",
    aliases={"任务",
             "任务列表",
             "tl",
             "tasklist"},
    block=False,
    priority=5,
)


@task_select_bot.handle()
async def gettasklist(matcher: Matcher, args: Message = CommandArg()):
    text = args.extract_plain_text()
    if text and text.isdigit():
        matcher.set_arg("mod", args)


@task_select_bot.got("mod", prompt="查询的任务类型\n0.每日任务\n1.定时任务\n2.限时任务")
async def selecttasklist(mod: str = ArgPlainText("mod")):
    if not mod.isdigit():
        await task_select_bot.finish("参数错误")
    mod = int(mod)
    if not mod == 9:
        checkmod(mod)
        task_list = select(mod)
    else:
        task_list = select()
    for i in range(len(task_list) - 1, -1, -1):
        if task_list[i].isend == True:
            task_list.pop(i)

    solve(task_list, mod)

    if len(task_list) == 0:
        await task_select_bot.finish("没有任务哦")
    await task_select_bot.send("任务列表")
    for task in task_list:
        await task_select_bot.send(solvetask(task))

    await task_select_bot.finish()

    # 处理不同类型的任务


def solve(task_list: [task], mod: int) -> None:
    if mod == 0:
        solvemod0(task_list)
    elif mod == 1:
        solvemod1(task_list)
    elif mod == 2:
        solvemod2(task_list)


#  处理普通任务 长期任务
'''
    只需要发送id，名称，和描述
'''


def solvemod0(task_list: [task]):
    for task in task_list:
        for k, v in gettaskdict(task).items():
            if not k in sendkeys.get("task"):
                setattr(task, k, None)


# 处理定时任务  间隔提醒
'''
    没有想好发送什么。
    先不发送
'''


def solvemod1(task_list: [timetask]):
    for task in task_list:
        for k, v in gettaskdict(task).items():
            if not k in sendkeys.get("timetask"):
                setattr(task, k, None)


# 发送限时任务  作业之类
'''
    发送id,name,desc,还有endertime
'''


def solvemod2(task_list: [timelimittask]):
    for task in task_list:
        for k, v in gettaskdict(task).items():
            if not k in sendkeys.get("timelimittask"):
                setattr(task, k, None)


