from picamera import PiCamera
from time import sleep
import os
import subprocess
from PIL import Image
from pytesseract import *   # tessseract lib
import webbrowser
import threading
import blt_com # user define lib - blt connect and ftp

stringDomain = "" # web site link
# Thread class for web browser
class WebBrowseThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    
    def run(self):
        os.system('chromium-browser --new-window '+url)
        #webbrowser.open_new(url)
        os.system('clear')

# Function : Set text in the middle of screen
def print_centered(s):
    terminal_width=int(subprocess.check_output(['stty', 'size']).split()[1])
    print s.center(terminal_width)

# Remove cursor
os.system('setterm -cursor off')

# Get Username from iput
#print '===================================================================='
os.system('clear')
print '\n'
s=raw_input('What is your name!? : ')
##print '===================================================================='

print '\n\n'
#os.system('clear')
print '===================================================================='
print 'Welcome, '+s+'!!! How are you?'
print '\n\n'
print 'Shall we take a picture!?'
print '===================================================================='

sleep(3)

# Get PiCamera object
camera = PiCamera()

while True:
    # clear Screen
    os.system('clear')
    
    # Start PiCamera
    camera.start_preview()
    camera.annotate_text_size=50

    # Count for 3 seconds
    t = 3
    while t>0:
        camera.annotate_text='Ready for taking picture in '+str(t)+' seconds!!!'
        sleep(1)
        t-=1
        
    if t==0:
        camera.annotate_text=''

    # Take a picture
    camera.capture('/home/pi/kss/image.jpg')
    camera.stop_preview()

    # Open the .jpg image
    os.system("sudo fbi -T 2 -d /dev/fb0 -noverbose -a /home/pi/kss/image.jpg")
    os.system('clear')

    # Ask whether user wanna do again
    #print '===================================================================='
    answer=raw_input('Would you like to try again? Please answer (yes) or (no) : ')
    #print '===================================================================='
    if answer=="no":
        os.system('clear')
        os.system('setterm -cursor on')
    
        print '===================================================================='
        print 'Please wait... Finding nearby devices...'
        print '===================================================================='
        # Search and connect with around devices and file transfer
        blt_com.bltFTP()
        sleep(3)
        os.system('clear')

        # Get a string on a photo using tesseract lib
        print '===================================================================='
        print 'Please wait... Finding letters on a photo...'
        print '===================================================================='
        stringInPhoto = pytesseract.image_to_string(Image.open('/home/pi/kss/image.jpg'))

        # if letters on a photo
        if stringInPhoto:
            stringList = stringInPhoto.split()
            for str in stringList:
                if str.count('.')==2:
                    stringDomain=str
                    break
            print '\n\n'
            print '********************************************************************'
            print 'We Found this letters on Photo! : ' + stringInPhoto
            print 'There is a web site link on Photo! : ' + stringDomain
            print '********************************************************************'
            break

        # if no letters on a photo
        print '\n\n'
        print '********************************************************************'
        print 'You need to try again! NO Letters Detected...!'
        print '********************************************************************'
        sleep(3)
        os.system('clear')

print '\n\n'
print '===================================================================='
print 'Do you want to enter the web site using Web Browser!?'
answer=raw_input('Please press \'y\' or \'n\' : ')
print '===================================================================='

if answer == "n":
    # shutdown
    os.system('clear')
    print '===================================================================='
    print 'Terminating now...'
    print '===================================================================='
    sleep(3)
    os.system('clear')
    quit()

# open a web browser
url='http://'+stringDomain
webBrowseThread = WebBrowseThread(url)
webBrowseThread.start()

os.system('clear')
print '===================================================================='
print "Main Thread Ended...."
print '===================================================================='
sleep(3)
os.system('clear')
