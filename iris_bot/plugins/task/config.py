tablenames = {
    "task": "task",
    "timetask": "timetask",
    "timelimittask": "timelimittask",
}

taskmod = {
    "task": 0,
    "timetask": 1,
    "timelimittask": 2
}

redisconfig = {
    "host": "localhost",
    "port": 6379,
    "password": None,
}

mongodbconfig = {

}

sendkeys = {
    "task": ["_id", "name", "desc"],
    "timetask": [],
    "timelimittask": ["_id", "name", "desc", "endertime"],
}

skipprops = ["mod", "isend", "addtime"]
