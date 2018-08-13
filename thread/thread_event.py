import threading

ev = threading.Event()

class PrepareThread(threading.Thread):
    def run(self):
        ev.set() # set flag 1
        print 'Set Flag 1'

class ActionThread(threading.Thread):
    def run(self):
        print self.getName(), 'waiting...'
        ev.wait()
        print self.getName(), 'Done...'

threads = []

for i in range(5):
    threads.append(ActionThread())
for th in threads:
    th.start()

PrepareThread().start()

for th in threads:
    th.join()

print 'Finish All of the work'
