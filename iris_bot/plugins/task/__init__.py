from iris_bot.plugins.task.task_add import task_add_bot
from iris_bot.plugins.task.task_select import task_select_bot
from iris_bot.plugins.task.task_delete import task_delete_bot
add = task_add_bot
select = task_select_bot
delete = task_delete_bot
'''
    controller 层
        接收参数 调用service 层
        1. 获取参数 设置任务
            create [0.1.2]
        2. 分类返回任务列表
            select [0.1.2]

'''

