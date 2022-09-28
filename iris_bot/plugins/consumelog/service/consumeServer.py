from iris_bot.plugins.consumelog.service import consume, consumedao, userdao
from iris_bot.plugins.consumelog.service.userserver import userservice


class consumeServer():
    '''
        账单逻辑
            添加账单。
                减钱
            修改账单。
                补差价
            删除账单。
                补钱
    '''

    def add(self, consume: consume):
        u = userservice.getUserById(consume.uid)
        userservice.consumeMoney(u, consume.money)
        consumedao.add(consume)
        consumedao.commit()

    def modify(self, consume: consume):
        oldMoney = consumedao.findById(consume.id).money
        num = consume.money - oldMoney
        if not num == 0:
            u = userservice.getUserById(consume.uid)
            userservice.consumeMoney(u, num)
        consumedao.modify(consume)
        consumedao.commit()

    def delete(self, consume: consume):
        u = userservice.getUserById(consume.uid)
        userservice.consumeMoney(u, -1 * consume.money)
        consumedao.delete(consume.id)
        consumedao.commit()

    def findById(self, id: int) -> consume:
        return consumedao.findById(id)

    def findByUid(self, uid: int) -> [consume]:
        return consumedao.findByUid(uid)

    def findAll(self):
        return consumedao.findAll()

consumeserver = consumeServer()
