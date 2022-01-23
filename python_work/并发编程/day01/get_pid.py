"""
    获取进程PID号
"""
import os
from time import sleep

pid=os.fork()

if pid <0:
    print("Error")
elif pid ==0:
    sleep(1)#子进程睡眠，父进程结束，子进程变成孤儿进程  集成养父孤儿院院长进程号
    print("Child PID：",os.getpid())#子PID
    print("Get parent PID:",os.getppid())#父PID
else:
    print("Get child PID:",pid)#子PID
    print("Parent PID:",os.getpid())#父PID
