from nonebot import on_command, exception
from nonebot.adapters import Message
from nonebot.exception import FinishedException
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, ArgPlainText

from iris_bot.plugins.task.service import select, deltaskbyid
from iris_bot.plugins.task.myutils import checkmodintaskmod as checkmod, getspecialprop

task_delete_bot = on_command(
    "deltask",
    aliases={
        "deletetask",
        "删除任务"
    },
    block=False,
    priority=5
)




# 获取mod
@task_delete_bot.handle()
async def firsthandler(matcher: Matcher, args: Message = CommandArg()):
    # 获取mod
    text = args.extract_plain_text()
    if text and text.isdigit():
        if not checkmod(int(text)):
            await matcher.finish("输入有误")
        matcher.set_arg("mod", args)


@task_delete_bot.got("mod", prompt="输入删除的任务类型\n0.每日任务\n1.定时任务\n2.限时任务")
async def getmod(matcher: Matcher,
                 mod: str = ArgPlainText("mod")):
    if not mod.isdigit():
        await task_delete_bot.finish("输入有误:输入不是数字")
    mod = int(mod)
    if not checkmod(mod):
        await matcher.finish("输入有误:请输入上述id")
    task_list = select(mod)
    props = ["_id", "name"]
    for task in task_list:
        await task_delete_bot.send(getspecialprop(task, props))


@task_delete_bot.got("id", prompt="输入要删除的任务id")
async def getid(id: str = ArgPlainText("id"),
                mod: str = ArgPlainText("mod")):
    try:
        if not checknum(id):
            await task_delete_bot.finish("id输入有误")
        id = int(id)
        mod = int(mod)
        deltaskbyid(id, mod)
        await task_delete_bot.finish("删除成功")
    except Exception as e:
        if not isinstance(e, FinishedException):
            await task_delete_bot.finish("id有误")


def checknum(item: str):
    if item.isdigit():
        return True
    return False
