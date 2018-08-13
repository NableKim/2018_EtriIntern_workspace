from threading import Thread
import time

def thread_run():
    print "Thread Started..."
    time.sleep(3)
    print "Thread Finished..."

t = Thread(target=thread_run, args=())
t.start()

t.join()
print "Main Thread Finished"
