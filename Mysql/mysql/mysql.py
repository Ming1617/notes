"""
    pymysql 操作数据库基本流程演示
"""

import pymysql

#连接数据库
db=pymysql.connect(host="localhost",
                   port=3306,
                   user='root',
                   password='010113',
                   database='stu',
                   charset='utf8')

# 获取游标（操作数据库，执行sql语句，承载直接执行结果）
cur=db.cursor()

#执行sql语句
sql="insert into class values \
     (1,'Pmma',17,'m',788.5,'2019-7-8');"

cur.execute(sql) # 执行语句

db.commit() #将写操作提交，可以多次写操作一同提交

# 关闭数据库
cur.close()
db.close()
