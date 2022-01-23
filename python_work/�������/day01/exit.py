"""
    退出进程
"""
import os,sys

#父子进程退出不会影响对方继续运行

os._exit(0) #退出进程
# sys.exit('退出')
print("exet test")