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
    print("Buonasera" + " " + username + "!" + "\n" + "Sono le: " + current_time + "\n")     
else:
    print("Buongiorno" + " " + username + "!" + "\n" + "Sono le: " + current_time + "\n")

print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ Sviluppato da TheDevsIsHere ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀" + "\n")

if dow == 3:
    print("Oggi dovrebbero esserci dei giochi gratuiti da riscattare su Epic Games!!")
    time.sleep(3)
    url = "https://store.epicgames.com/it/free-games?lang=it"
    webbrowser.open(url)
    print("uscita dal programma")
    sys.exit()
    
if dow == 4:
    print("Se non avete riscattato i giochi ieri, oggi è l'ultimo giorno!!")
    time.sleep(3)
    url = "https://store.epicgames.com/it/free-games?lang=it"
    webbrowser.open(url)
    print("uscita dal programma")
    sys.exit()
    
val = False    
while not val:
    if dow <3 or dow >4:
        print("Nessun gioco sta per scadere su Epic Games!!")
        val = True
        print("Autochiusura in corso..")
        time.sleep(3)
        sys.exit()
