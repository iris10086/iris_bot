from nonebot import on_command

task_finish_bot = on_command(
    "finishtask",
    aliases={
        "finish",
        "完成任务"
    },
    block=False,
    priority=5
)



