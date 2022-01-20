# 生产者和消费者

import queue
import time
from queue import Queue
import random
import threading
from threading import Thread, current_thread

q = Queue(5)


class Producer(Thread):
    def run(self):
        name = current_thread().name
        nums = range(100)
        global q
        while True:
            num = random.choice(nums)
            q.put(num)
            t = random.randint(1, 5)
            print('生产者 %s 生产了数据 %s，然后休眠 %s 秒 ' % (name, num, t))
            time.sleep(t)


class Cusumer(Thread):
    def run(self):
        name = current_thread().name
        global q
        while True:
            num = q.get()
            q.task_done()
            t = random.randint(2, 5)
            print('消费者 %s 消费了数据 %s ,然后休眠 %s 秒' % (name, num, t))
            print('队列尺寸 %s' %(q.qsize()))
            time.sleep(t)


p1 = Producer(name='p1')
p1.start()
# p2 = Producer(name='p2')
# p2.start()
c1 = Cusumer(name='c1')
c1.start()
