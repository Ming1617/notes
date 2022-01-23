import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='17')
# r.setbit('pybit1',4,1)
# print(r.getbit('pybit1',3))
# print(r.getbit('pybit1',4))
print(r.bitcount('pybit1'))
