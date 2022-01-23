#生产者  生产者消费者演示  消费者：consumer

import redis
import json
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='17')

json_obj={'task':'send_email','send_email':'aaa','from':'bbb','to':'admin'}
json_str=json.dumps(json_obj)
r.lpush('pyl2',json_str)