import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='17')

# key_list=r.keys('*')
# print(key_list)
# print(r.type('l1'))
# print('111')

###string###
r.set('puname','jcm',ex=30)
print(r.get('puname'))
