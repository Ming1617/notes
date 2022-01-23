"""
    pymysql 写操作示例  流程演示
    insert update delete
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

#写数据库
try:
    # 写sql语句执行
    # 插入操作
    # name=input("Name:")
    # age=input("Age:")
    # score=input("Score:")
    """
    
     sql="insert into class (name,age,score)  \
        values ('%s',%s,%s)"%(name,age,score)
        
    cur.execute(sql)#执行
    
    """
    #插入
    # sql = "insert into class (name,age,score)  \
    #         values (%s,%s,%s)"
    # # 可以使用列表直接给sql语句的values传值
    # cur.execute(sql,[name,age,score])#执行

    #更新，修改
    # sql='update interest set price=11800\
    #     where name="李四"'
    # cur.execute(sql)

    #删除操作
    sql='delete from class where score<80;'
    cur.execute(sql)

    db.commit()#提交
except Exception as e:
    db.rollback()#退回到commit执行之前的数据库状态
    print(e)


# 关闭数据库
cur.close()#关闭游标
db.close()#关闭数据库