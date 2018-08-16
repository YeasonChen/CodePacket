from threading import Thread
import threading
import time


age = 100
"""
多线程中,父线程会等待子线程全部结束后才退出
开启子线程后,主线程不会受影响会继续执行


串行:任务一个接一个的执行
并行:多核cpu同时执行几个进程中的线程
并发:cpu快速切换线程,造成多个线程同时执行的假象


每个核心的cpu同一时刻只能执行一个进程中的一个线程!!!

cpu核心通过快速切换进程来实现多任务,然后调度到某个进程的时候,执行该进程中的线程任务.

python中,多核cpu可以同时执行多个进程,使得利用率较高
python中,由于有GIL使得每个时候解释器只会执行一个线程的任务而不管有几个核心,所以python中多线程利用率低


进程的出现:是为了使多个程序并发执行,提高资源使用效率
线程的出现:是为了降低多个进程间切换所带来的时空开销,使得并发的粒度变得更小
在一个相对更大的时间内切换进程,在比这个时间更小的间隔内切换当前进程中的线程,使得并发执行粒度更小

"""


def thread_work():
    print(threading.Thread.getName(threading.current_thread()))
    global age
    age += 100
    print(age)


def next_age():
    print(threading.Thread.getName(threading.current_thread()))
    global age
    time.sleep(1)
    print(age)


t1 = Thread(target=thread_work, name='first')
t1.start()

t2 = Thread(target=next_age, name='second')
t2.start()
