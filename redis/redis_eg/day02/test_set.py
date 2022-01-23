import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# r.sadd('pys1', 'a', 'b', 'c', 'd')
# print(r.smembers('pys1'))

# r.sadd('pys2', 'a', 'f', 'c', 'z')
# print(r.sinter('pys1', 'pys2'))

############有序集合#########
#r.zadd('pyz1', {'tom':6000, 'jim':8000, 'jack':12000})
#[(b'tom', 6000.0), (b'jim', 8000.0), (b'jack', 12000.0)]
#print(r.zrange('pyz1',0, -1, withscores=True))
#print(r.zcount('pyz1', "(8000", "(13000"))

#r.zadd('pyz2', {'tom':4000, 'jim':6000})
#r.zinterstore('pyz3', ('pyz1','pyz2'), aggregate='max')
#print(r.zrange('pyz3',0, -1, withscores=True))

r.zinterstore('pyz4', {'pyz1':0.5,'pyz2':1}, aggregate='max')
print(r.zrange('pyz4',0, -1, withscores=True))