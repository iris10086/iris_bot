from iris_bot.plugins.consumelog.factories.factorylib import t_type, getbean, getbeanmap


class typefactory():
    def __init__(self):
        # 表中的列号所对应的属性名称
        #                   对象成员类型名:数据库列名
        self.type_table_map = {
            "id": "id",
            "name": "type_name",
        }
        self.type_key = list(self.type_table_map.keys())

    # 获得type对象
    def gettype(self, list: ()) -> [t_type]:
        '''
        :param list: type属性值
        :return: type对象列表
        '''
        res = []
        for props in list:
            res.append(self.getonetype(props))
        return res

    def getonetype(self, list: ()) -> t_type:
        return getbean(t_type(), self.type_key, list)

    # 获取 map by type
    def getmap(self, type: t_type) -> {}:
        '''
        map数据
        :param type:
        :return:
        '''
        return getbeanmap(type, self.type_table_map)

    # 获取type by map
    def gettypebymap(self, map: {}) -> t_type:
        '''
        :param map:{id:v1,name:v2}
        :return: type(id=v1,name=v2)
        '''
        return getbean(t_type(), list(map.keys()), list(map.values()))

    def getIdNameMaps(self, types: [t_type]) -> {}:
        res = {}
        for type in types:
            res.update(self.getIdNameMap(type))
        return res

    def getTypesByMap(self, map: {}) -> [t_type]:
        '''
        :param map: {k:v}
        :return: [type(id=k,name=v)]
        '''
        res = []
        for k, v in map.items():
            res.append(t_type(id=k, tname=v))
        return res

    def getTypeByMap(self, map: {}) -> t_type:
        res = self.getTypesByMap(map)
        if len(res) == 0:
            return None
        return res[0]

    # 获取{id:name} map
    def getIdNameMap(self, type: t_type) -> {}:
        return {type.id: type.name}


typefactory = typefactory()

if __name__ == '__main__':
    type = typefactory.gettypebymap({"id": 1, "type_name": "test"})
    print("hello")
