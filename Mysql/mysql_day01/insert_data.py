import pymysql
import time

#建立连接
con = pymysql.connect('localhost', 'root', '123456', 'country', charset='utf8')

cursor = con.cursor()

t1 = time.time()
data_list = []
for i in range(1000000):
    name = 'Tom_%s'%(i)
    data_list.append(name)

t2 = time.time()
cost_time = t2-t1
print('t2-t1 is %s'%(cost_time))

ins = 'insert into students(name) values(%s)'
cursor.executemany(ins, data_list)
con.commit()

t3 = time.time()
cost_time_sql = t3 - t2
print('sql cost time is %s'%(cost_time_sql))

#关闭
cursor.close()
con.close()





















