import pyautogui
import subprocess
import time
import webbrowser
import getpass
import time
import sys

username = getpass.getuser()

year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

if hour >= 13:
    print("Good evening" + " " + username + "!" + "\n" + "Program start time: " + current_time + "\n")     
else:
    print("Good morning" + " " + username + "!" + "\n" + "Program start time: " + current_time + "\n")

print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ Developed by TheDevsIsHere ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀" + "\n")

if dow == 3:
    print("Today there should be free games to redeem on Epic Games!!")
    time.sleep(3)
    url = "https://store.epicgames.com/en-US/free-games?lang=en-US"
    webbrowser.open(url)
    print("exiting the program")
    sys.exit()
    
if dow == 4:
    print("If you did not redeem the games yesterday today is the last day!!")
    time.sleep(3)
    url = "https://store.epicgames.com/en-US/free-games?lang=en-US"
    webbrowser.open(url)
    print("exiting the program")
    sys.exit()
    
val = False    
while not val:
    if dow <3 or dow >4:
        print("No game is about to expire on Epic Games!!")
        val = True
        print("Self-closing in progress..")
        time.sleep(3)
        sys.exit()
