from multiprocessing import Pool, Manager
import os
import time

"""
多进程中,主进程不会等待子进程结束,当自身任务完成即退出
开启子进程后,主进程继续执行不变
"""


def work(num, qu):
    time.sleep(3)
    qu.put('yeason')
    print('num = %d pid = %d' % (num, os.getpid()))


def get_data(jack_queue):
    print('start get')
    name = jack_queue.get()
    print('end get')
    print(name)


q = Manager().Queue()
po = Pool(3)
po.apply_async(work, args=(1, q))
po.apply_async(get_data, args=(q, ))
po.close()
# po.join()

print('----end----')
