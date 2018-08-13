import threading

# define function for sub thread to run
def sum(start, end):
    total=0
    for i in range(start, end):
        total+=i
    print ("Subthread ", total)


# make thread object and run it
t = threading.Thread(target=sum, args=(1, 10000))
t.start()

print ("Main Thread")
