import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='17')
r.hmset('pyh1',{'name':'jcm','age':20})
print(r.hgetall('pyh1'))