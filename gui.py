



import os, sys, subprocess,time
import os, sys, json, urllib, re
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")


def logo():
 print("""
                                              
@@@@@@@              @@@@@@@@  @@@  @@@  @@@  
@@@@@@@             @@@@@@@@@  @@@  @@@  @@@  
  @@!               !@@        @@!  @@@  @@!  
  !@!               !@!        !@!  @!@  !@!  
  @!!    @!@!@!@!@  !@! @!@!@  @!@  !@!  !!@  
  !!!    !!!@!@!!!  !!! !!@!!  !@!  !!!  !!!  
  !!:               :!!   !!:  !!:  !!!  !!:  
  :!:               :!:   !::  :!:  !:!  :!:  
   ::                ::: ::::  ::::: ::   ::  
   :                 :: :: :    : :  :   :    
                                     
\n\t\033[31m\033[1m\033[33m..:;\033[31m Termux \033[36mGUI \033[31mInstaller\033[33m ;:..
 \n\033[0m\033[1m
\t \033[33m[-] \033[0mPlatform : \033[33m\033[1mTermux
\t \033[1m\033[33m[-] \033[0mName     : \033[33m\033[1mTermux GUI
\t \033[1m\033[33m[-] \033[0mSite     : \033[33m\033[1mwww.bhai4you.blogspot.com
\t \033[1m\033[33m[-] \033[0mCoded by :\033[1m \033[33m[  \033[32mParixit \033[33m ]
\t \033[1m\033[33m[-] \033[0mSec.Code : \033[33m\033[1m8h4i\033[0m
\t \033[1m\033[33m[-] \033[0mGithub   : \033[33m\033[1mhttps://github.com/Bhai4You\033[0m
\t \033[1m\033[33m[-] \033[0mYoutube  : \033[33m\033[1mBullAnonymous\033[0m
  """)

os.system("clear")
logo()

print("\n\n\nPress Enter To Continue...!")
print
os.system("read jkr")
os.system("clear")
  
print
print
print("""    	    \033[33m\033[1m\033[33m..::; \033[36m Architecture \033[33m;::..\033[0m
       \n\n\033[1m\033[33m1. \033[1m\033[36mArm\033[31m Or \033[36mArmhf
       \n\n\033[1m\033[33m2. \033[36mAarch
\n\n\033[1m\033[32m 
       \033[0m""")


def help():
	print ("\n\033[1mFirst Check Your Device Architecture..!!. ")
	print
	print ("\n\033[1mFollowing Command Type in other Terminal Window")
	print
	print ("\033[1m\033[32m1. \033[33muname -m\n\n\033[32m2.\033[33m uname -a\n\n\033[32m3.\033[33m lscpu\n\n\033[32m4. \033[33mecho $HOSTTYPE\n\n\033[32m5. \033[33mdpkg --print-architecture")


	


Tgui = raw_input("\n\n\033[31m\033[1m\033[36m[\033[31m$\033[36m]\033[32m\033[1m T-GUI \033[1m\033[33m :\033[0m ")
if Tgui == "help":
            help()

elif Tgui == '1':
	print
	print
	os.system("bash /sdcard/arm.sh")
	os.system("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	os.system("figlet 'Update' | lolcat")
	os.system("apt update -y")
	os.system("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	os.system("figlet 'TigerVnc' | lolcat")
	os.system("apt install tigervnc -y")
	os.system("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	os.system("figlet 'X-Term' | lolcat")
	os.system("apt install xterm -y")
	os.system ("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	
	
	
elif Tgui == '2' or  Tgui == '02':
	print
	print
	os.system("bash /sdcard/aarch64.sh")
	os.system("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	os.system("figlet '                   Update' | lolcat")
	os.system("apt update -y")
	os.system("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	os.system("figlet '                   TigerVpn' | lolcat")
	os.system("apt install tigervpn -y")
	os.system("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	os.system("figlet '                   X-Term' | lolcat")
	os.system("apt install xterm -y")
	os.system ("clear")
	os.system("echo")
	os.system("echo")
	os.system("echo")
	



else:
	print "\n\n\n\t[!] 3V3ryTh1n9 15 P0551613 \033[32m\033[0m\n\n"

print "\n\n\n\n\033[1m\033[32m<=======[ \033[33m\033[1m\033[33m:.\033[36mAuthor \033[1m\033[31m:\033[36m Sutariya Parixit\033[33m.:\033[32m ]=======>\n\n\033[0m"

	
sys.exit()

