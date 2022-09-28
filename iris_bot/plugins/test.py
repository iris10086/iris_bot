from nonebot import on_command, require

require('dailynotehelper')

from iris_bot.plugins.dailynotehelper import run_once

genshin = on_command(
    "原神",
    aliases={
        "yuanshen",
        "o",
    }
)


#
# @test.handle()
# async def func():
#     await test.reject("test")

@genshin.handle()
async def test():
    messeges = run_once()
    for mesg in messeges:
        await genshin.send(mesg)



if __name__ == '__main__':
    test()
