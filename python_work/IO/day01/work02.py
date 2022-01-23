"""
    3．编写一个程序﹐向一个文件中写入如下内
    1.2019-1-1 18:18:18
    2.2019-1-1 18:18:19
    3.2019-1-1 18: 18:24
    循环每隔1秒写入一次,序号从1排列
    ctrl-c结束程序﹐下次启动程序序号要与之前的衔接
"""
import time
tuple_time=time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",tuple_time))
f=open("time.txt","r+")
time_i=0
for i in f:
    time_i = int(i.split(".")[0])
# print(time_i)
f.close()
f=open("time.txt","a+")
while True:
    tuple_time = time.localtime()
    time_i+=1
    data=str(time_i)+"."+time.strftime("%Y-%m-%d %H:%M:%S",tuple_time)
    f.write(data+"\n")
    time.sleep(1)
f.close()
