
DB_NUMBERS = 16 #数据库数量
KEY_NUMBERS = 20 #每次检查key的数量

current_db = 0 #记录当前检查到哪个库

def activeExpireCycle():

    for i in range(DB_NUMBERS):

        if current_db == DB_NUMBERS:
            current_db = 0

        #获取当前数据库
        redisDB = server.db[current_db]
        first_start = True
        del_key_num = 0
        current_db += 1

        while (first_start or del_key_num > KEY_NUMBERS/4):
            first_start = False
            for j in range(KEY_NUMBERS):

                _key = redisDB.randomExpireKey()
                if is_expire(_key):
                    #过期 则直接删除
                    delete_key(_key)
                    del_key_num += 1

                if time_is_limit():
                    #若执行时间太长 默认25毫秒
                    return


