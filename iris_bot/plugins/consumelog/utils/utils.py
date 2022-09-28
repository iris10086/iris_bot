from iris_bot.plugins.consumelog.pojo import user

'''
    bean: 实例对象
    propnames: bean的属性名称
    values: bean属性名称对应值
    return bean : 将values按照propnames顺序封装给bean并返回
'''
def getbean(bean, propnames: [], values: []):
    for i in range(len(propnames)):
        setattr(bean, propnames[i], values[i])
    return bean


'''
    bean: 实例对象
    propnames: bean的属性名称
    return map : bean的属性:value的键值对
'''
def getbeanmap(bean, propmap: {}) -> {}:
    map = {}
    for k, v in propmap.items():
        map[v] = getattr(bean, k)
    return map
