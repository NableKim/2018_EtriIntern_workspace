import threading
import time

pool_sema = threading.Semaphore(3)
count=0

def thread_run():
    global count
    with pool_sema:
        print 'Hello World!'
        for i in range(0, 3):
            count += 1
            print count
        time.sleep(0.3)

thread_list = []
thread_size = 3

for i in  range(0, thread_size):
    t = threading.Thread(target=thread_run, args=())
    thread_list.append(t)

for th in thread_list:
    th.start()
    print 'Thread Started'

for th in thread_list:
    th.join()
    print 'Thread Join'
