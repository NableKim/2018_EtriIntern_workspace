from picamera import PiCamera
from time import sleep
import os
import subprocess
from PIL import Image

# Function : Set text in the middle of screen
def print_centered(s):
    terminal_width=int(subprocess.check_output(['stty', 'size']).split()[1])
    print s.center(terminal_width)

# Remove cursor
os.system('setterm -cursor off')

# Get Username from iput
s=raw_input('What is your name!? : ')

os.system('clear')
print_centered('Welcome, '+s+'!!! How are you?')
print_centered('Lets take a picture')

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

    # Ask whether user wanna do again
    answer=raw_input('Would you like to try again? Please answer (yes) or (no) : ')
    os.system('clear')
    if answer=="no":
        # shutdown
        print_centered('Terminating now...')
        sleep(3)
        os.system('clear')
        os.system('setterm -cursor on')
        break
   
