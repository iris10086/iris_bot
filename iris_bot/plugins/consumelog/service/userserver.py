from iris_bot.plugins.consumelog.service import user, userredis, userdao, consumedao


class userService():
    '''
        对用户的增删改查。
        设置金额。
        对金额的增加、减少。
    '''

    def getUserByqq(self, qq: int) -> user:
        '''
        通过QQ号获取对象
        '''
        # 尝试从redis读取
        user = userredis.getUserByQQ(qq)
        if user == None:
            user = userdao.findByqq(qq)
        return user

    def getUserById(self, id: int) -> user:
        user = userredis.getUserById(id)
        if user == None:
            user = userdao.findById(id)
        return user

    def getAll(self) -> [user]:
        return userdao.findAll()

    def consumeMoney(self, user: user, num: int):
        user.subMoney(num)
        userredis.hset(user)
        userdao.modify(user)

    def setMoney(self, user: user, num: int):
        user.money = num
        self.modifyUser(user)

    def registerUser(self, user: user):
        userredis.hset(user)
        userdao.add(user)
        userdao.commit()

    def deleteUser(self, user: user):
        userredis.deleteUser(user)
        userdao.delete(user.uid)
        consumedao.deleteByUid(user.uid)
        userdao.commit()

    def modifyUser(self, user: user):
        userredis.hset(user)
        userdao.modify(user)
        userdao.commit()


userservice = userService()
