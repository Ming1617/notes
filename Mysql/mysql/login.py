"""
    注册登录模拟
    * 创建用户表user 存储用户
     create table user (id int primary key auto_increment,name varchar(32) not null,passwd char(8) not null);

     * 注册: 将注册信息存储到数据库,用户名不能重复
            基础信息包含用户名,密码

     * 登录: 判断用户名密码是否正确
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

#注册
def register():
    name=input("用户名:")
    passwd=input("密 码：")
    #判断用户名是否重复
    sql="select * from user where name='%s'"%name
    cur.execute(sql)
    result=cur.fetchone()
    if result:
        return False
    try:
        sql="insert into user (name,passwd) \
            values(%s,%s)"
        cur.execute(sql,[name,passwd])
        db.commit()
        return True
    except:
        db.rollback()
        return False

def login():
    name=input("用户名:")
    passwd=input("密 码：")
    sql="select * from user where name='%s' and passwd='%s'"%(name,passwd)
    cur.execute(sql)
    result=cur.fetchone()
    if result :
        return True
while True:
    print("""
              ================
               1.注册    2.登录
              ================
    """)
    cmd=input('输入命令：')
    if cmd=='1':
        #执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd=='2':
        #执行登录
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")

    else:
        print('我也做不到')





#关闭数据库
cur.close()
db.close()