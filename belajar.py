GNU nano 5.4                     belajar.py

import os.sys.time

def bersih():
    os.system("clear")

def menu():
    bersih()
    print "+----------------------+"
    print "Author : M.Farid.H."
    print "FB     : Mas kanchill"
    print "WA     : 085226214439"
    print "+----------------------+"
    print "[1] Install Dark Fb"
    print "[2] Install Metasploit"
    print "[3] Keluar/Exit"
    pil = raw_imput("Pilih Sesuai Nomor.>>)"
    if pil == "1":
       os.system("pkg update && pkg upgrade pkg -y")
       os.system("pkg install git -y")
       os.system("pkg install python2")
       os.system("git clone https://github.com/Rendi-ID/DarkFb")
    elif pil =="2":
       os.system("pkg update && pkg upgrade -y")
       os.system("pkg install git -y")
       os.system("pkg install bash")
       os.system("git clone https://github.com/Rendi-ID/Install_Metasploit")
    elif pil =="3":
       system.exit():
        
 menu()