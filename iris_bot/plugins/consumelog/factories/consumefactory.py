from iris_bot.plugins.consumelog.factories.factorylib import consume, getbean, getbeanmap

'''
    处理consume对象。
'''


class consumefactory():
    def __init__(self):
        # 表中的列号所对应的属性名称
        #                   对象成员类型名:数据库列名
        self.consume_table_map = {"id": "id",
                                  "name": "name",
                                  "money": "money",
                                  "time": "time",
                                  "uid": "uid",
                                  "tid": "tid"}
        self.consume_key = list(self.consume_table_map.keys())

    def getconsume(self, list: ()) -> [consume]:
        '''
        :param list: 属性元组
        :return: consume列表
        '''
        res = []
        for props in list:
            res.append(self.getoneconsume(props))
        return res

    def getoneconsume(self, list: ()) -> consume:
        return getbean(consume(), self.consume_key, list)

    # 通过consume对象获取map
    def getmapbyconsume(self, consume: consume) -> {}:
        '''
        :param consume: consume对象
        :return: consume的属性:值 的map对象
        '''
        return getbeanmap(consume, self.consume_table_map)

    # 通过map获取consume对象
    def getconsumebymap(self, props: {}) -> consume:
        '''
        :param props: consume 属性的 属性名:属性值
        :return: consume对象
        '''
        return getbean(consume(), list(props.keys()), list(props.values()))


consumefactory = consumefactory()
