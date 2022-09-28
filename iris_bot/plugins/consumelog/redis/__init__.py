import redis
from iris_bot.plugins.consumelog.config import redisConf
from iris_bot.plugins.consumelog.pojo import t_type, user, consume
from iris_bot.plugins.consumelog.factories import userfactory, consumefactory, typefactory

redis_clent = redis.Redis(
    host=redisConf.get("host"),
    port=redisConf.get("port"),
    password=redisConf.get("password"),
    db=redisConf.get("db"),
)
prefix = "iris:bot:"
