import time

import redis

pool=redis.ConnectionPool(host='127.0.0.1',db=0,port=6379,password='17')
r=redis.Redis(connection_pool=pool)


def double_account(user_id):
    key='account_%s'%(user_id)
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                pipe.watch(key)
                value=int(r.get(key))
                value*=2
                print('sleep is start')
                time.sleep(20)
                print('sleep -- is end')
                pipe.multi()
                pipe.set(key,value)
                pipe.execute()
                break
            except redis.WatchError:
                print('---key changed---')
                continue
    return int(r.get(key))

if __name__ == '__main__':
    #account_admin
    print(double_account('admin'))