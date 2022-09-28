from iris_bot.plugins.consumelog.factories.factorylib import user, getbean, getbeanmap


# 简化对user对象的操作
class userfactory():

    def __init__(self):
        # 表中的列号所对应的属性名称
        #                   对象成员类型名:数据库列名
        self.user_table_map = {"uid": "uid",
                               "username": "username",
                               "password": "password",
                               "nickname": "nickname",
                               "money": "money",
                               "qq_number": "qq_number"}
        self.user_key = list(self.user_table_map.keys())

    # 将元组封装为user对象数组
    def getuser(self, list: ()) -> [user]:
        if isinstance(list, tuple):
            return self.list2user(list)
        pass

    # 将元组封装为user对象数组
    def list2user(self, list: ()) -> [user]:
        res = []
        for props in list:
            res.append(self.getoneuser(props))
        return res

    def getoneuser(self, list: ()) -> user:
        return getbean(user(), self.user_key, list)

    # 通过映射关系获取k:v键值对
    def getusermap(self, user: user):
        return getbeanmap(user, self.user_table_map)

    # 通过map获取对象
    def getuserbymap(self, props:{}) -> user:
        return getbean(user(), list(props.keys()), list(props.values()))


userfactory = userfactory()
