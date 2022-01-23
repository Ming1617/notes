"""
    fork进程演示2
    Windows下不可用
"""
import os
from time import sleep
print("================")
a=1
#创建子进程
pid=os.fork()
if pid<0:
    print("Create process failed")

#子进程执行部分
elif pid==0:
    print('The new process')
    print("a=",a)
    a=1000
#父进程执行部分
else:
    sleep(1)
    print('The old process')
    print("a:",a)

print("all-a:",a)