import time
import threading


def coun(n):
    print(threading.Thread.getName(threading.current_thread()))
    while n > 0:
        n -= 1


start_time = time.time()
# coun(10000000)
# coun(10000000)
# end_time = time.time()
# print(end_time - start_time)

t1 = threading.Thread(target=coun, args=(10000000, ))
t2 = threading.Thread(target=coun, args=(10000000, ))
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print(end_time - start_time)
