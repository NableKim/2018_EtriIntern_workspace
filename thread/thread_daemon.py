import threading, requests, time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')

# Daemon Thread
t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.daemon = True    # default = False
t1.start()

print("### End ###")
