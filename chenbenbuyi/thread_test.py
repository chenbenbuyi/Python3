import threading
from threading import current_thread
import time


def myThread(arg1, arg2):
    print(current_thread().name, "线程开始")
    print('%s %s ' % (arg1, arg2))
    time.sleep(3)
    print(current_thread().name, "线程停止")


for i in range(1, 5, 1):
    # t1 = myThread(i, i + 1)
    #  target 指定要执行的函数，arg为函数的参数
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()


# 继承 threading 的 Thread 类，重写run方法

class Mythread(threading.Thread):
    def run(self):
        print("当前线程名称：%s" % current_thread().name)


t1 = Mythread()
t1.start()