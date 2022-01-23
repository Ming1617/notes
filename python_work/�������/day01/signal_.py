"""
    信号处理僵尸程序
"""
import os,sys
import signal

#子进程退出时父进程忽略推出行为，子进程由系统处理
# signal.signal(signal.SIGCHLD,signal.SIG_IGN)
pid=os.fork()
if pid<0:
    print("Error")
elif pid==0:
    print("Child PID:",os.getpid())
    sys.exit("子进程退出")
else:
    """
    os.wait()处理僵尸进程
    """
    # pid,status=os.wait()
    # print("pid:",pid)
    # print("statis:",status)#child 退出状态×256
    while True:#父进程不退出
        pass