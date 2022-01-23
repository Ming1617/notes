'''使用executenany()方法插入2条记录'''


#1.创建2个对象
import pymysql

#连接数据库
db=pymysql.connect(host="localhost",
                   port=3306,
                   user='root',
                   password='010113',
                   database='maoyandb',
                   charset='utf8')

# 获取游标（操作数据库，执行sql语句，承载直接执行结果）
cur=db.cursor()
#直接执行sql命令
ins='insert into filmtab values(%s,%s,%s)'
film_list=[('月光宝盒','周星驰','1993'),('大圣娶亲','周星驰','1993')]
cur.executemany(ins,film_list)
#3.提交到数据库执行
db.commit()
#4.关闭数据库
cur.close()
db.close()