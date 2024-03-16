#!/usr/bin/python
# << CODE BY HUNX04
# << MAU RECODE ??? IZIN DULU LAH,  MINIMAL TAG AKUN GITHUB MIMIN YANG MENGARAH KE AKUN INI, LEBIH GAMPANG SI PAKE FORK
# << KALAU DI ATAS TIDAK DI IKUTI MAKA AKAN MENDAPATKAN DOSA KARENA MIMIN GAK IKHLAS
# “Wahai orang-orang yang beriman! Janganlah kamu saling memakan harta sesamamu dengan jalan yang batil,” (QS. An Nisaa': 29). Rasulullah SAW juga melarang umatnya untuk mengambil hak orang lain tanpa izin.

#IMPOER MODULE

import requests
import json
import time
from sys import stderr
import sys

Bl='\033[30m' # VARIABLE COLORS
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

def autoketik(x): #TYPING
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.030)

#BANNER

stderr.writelines(f"""{Ye} 
   ____  ____  ____  _   _ __  __ ____    _____ ___   ___  _     ____  
  / ___|| __ )|  _ \| | | |  \/  |  _ \  |_   _/ _ \ / _ \| |   / ___| 
  \___ \|  _ \| | | | | | | |\/| | |_) |   | || | | | | | | |   \___ \ 
   ___) | |_) | |_| | |_| | |  | |  __/    | || |_| | |_| | |___ ___) |
  |____/|____/|____/ \___/|_|  |_|_|       |_| \___/ \___/|_____|____/      
                            {Wh}TOOLS V.1.2 {Ye}  {Wh} © by hidd3n                   
""")

try:
    domain = input(f"\n\n{Ye}[ {Wh}+ {Ye}] {Wh}ENTER TARGET WEB EX [{Ye}hacker.com{Wh}] : ") #INPUT LINK WEBSITE
    autoketik(f"{Ye}[ {Wh}+ {Ye}] {Wh}SCANNING SUBDOMAIN FOR {Ye}{domain}{Wh}...")

    time.sleep(2)

    def Subdomain_CRT(): #FUNCION
        subdo_main = []
        url = f"https://crt.sh/?q=%.{domain}&output=json" #WEB_API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for entry in data:
                subdomain = entry['name_value']
                if subdomain not in subdo_main:
                    subdo_main.append(subdomain)
        return subdo_main


    subdomains = Subdomain_CRT() #CALL FUNCTION
    print(f"\nSUBDOMAIN FOUND : {Ye}", len(subdomains)) #SUBDOMAIN FOUND
    print(f"{Wh}------------------------------------{Gr}")

    for subdomain in subdomains: #OUTPUT AND LOOP
        print(subdomain)
except KeyboardInterrupt:
    print(f" {Wh}[{Re}!{Wh}] {Re}PROGRAM STOPPED...")