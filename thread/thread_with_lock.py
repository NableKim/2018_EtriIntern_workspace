import threading
import time

count = 10
lock = threading.Lock()

class developer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name
        self.fixed=0

    def run(self):
        global count
        while 1:
            if count > 0:
                with lock:
                    count -= 1
                self.fixed += 1
                time.sleep(0.1)
            else:
                break

dev_list=[]
for name in ['usr1', 'usr2', 'usr3']:
    dev = developer(name)
    dev_list.append(dev)
    dev.start()

for dev in dev_list:
    dev.join()
    print(dev.name, 'fixed', dev.fixed)
