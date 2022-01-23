#消费者  生产者消费者演示 生产者producer
import json

import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='17')

while True:
    task=r.brpop('pyl2',10)
    print(task)
    if task :
        json_obj=json.loads(task[1])
        #具体任务执行逻辑
    else:
        print('-----no task-----')
