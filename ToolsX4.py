#Tools Installer
#Author X4
#Copyright (c) 2019
#Please Dont Recode
#Thanks (X4)

#importing library
import os
import sys
import time
import argparse
from time import ctime

os.system('cls()')

messstring = ('command not Found')

#color
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#banner
banner = (bcolors.OKBLUE + '''
██╗  ██╗██╗  ██╗      ███████╗███████╗ ██████╗
╚██╗██╔╝██║  ██║      ██╔════╝██╔════╝██╔════╝
 ╚███╔╝ ███████║█████╗███████╗█████╗  ██║     
 ██╔██╗ ╚════██║╚════╝╚════██║██╔══╝  ██║     
██╔╝ ██╗     ██║      ███████║███████╗╚██████╗
╚═╝  ╚═╝     ╚═╝      ╚══════╝╚══════╝ ╚═════╝
''')
print (banner)

#tools info
toolsinfo = (bcolors.WARNING + '''
╔═══════════════════════════════════════════════╗
║                                               ║
║   Author      : MrX4                          ║
║                                               ║
║   Instagram   : X4-Security                   ║
║                                               ║
║   Facebook    : Don't Have                    ║
║                                               ║
║   Team        : No Team                       ║
║                                               ║
╚═══════════════════════════════════════════════╝
''')

print (toolsinfo)

try:
    print (bcolors.OKBLUE + '''┌──'''+ctime())
    command = input ('''│
└─── Root@X4 : ~ # ''')
    
    #Command List Tools
    if (command == 'listtools'):
        os.system('cls()')
        toolban = (bcolors.OKGREEN + '''


 ██╗  ██╗██╗  ██╗      ███████╗███████╗ ██████╗
 ╚██╗██╔╝██║  ██║      ██╔════╝██╔════╝██╔════╝
  ╚███╔╝ ███████║█████╗███████╗█████╗  ██║     
  ██╔██╗ ╚════██║╚════╝╚════██║██╔══╝  ██║     
 ██╔╝ ██╗     ██║      ███████║███████╗╚██████╗ ┌─TOOLS
 ╚═╝  ╚═╝     ╚═╝      ╚══════╝╚══════╝ ╚═════╝ └─INSTALLER V1


─────List Tools────────────────────

[1] Port Scanner
[2] DNS Spoofing
[3] Brute Force Facebook
[4] Brute Force Instagram
[5] XAttacker
[6] Bypass Firewall
[7] Metasploit (Root)
[8] Sqlmap
[9] Nmap
[10] Hammer DDos
[11] SayCheese
[12] Trojan DDos
[13] Auto Deface Wevdav
[14] Check Ip Website
[15] Dork Scanner
[16] Spam Whatsapp
[17] Admin Finder
[18] Fat Rat
[19] IP Geolocation
[20] Vbug
''')
        print (toolban)
        try:
            print ('''┌──'''+ctime())
            tcommand = input ('''│
└─── Root@X4 ./listtools : ~ # ''')
            #port Scanner
            if (tcommand == '1'):
                os.system('git clone https://github.com/Oseid/SpyPorte')
            
            #Dns spoofing
            if (tcommand == '2'):
                os.system('git clone https://github.com/DanMcInerney/dnsspoof')

            #FB Bute
            if (tcommand == '3'):
                os.system('git clone https://github.com/Gameye98/FBBrute')

            #Brute IG
            if (tcommand == '4'):
                os.system('git clone https://github.com/Pure-L0G1C/Instagram')

            #Xattacker
            if (tcommand == '5'):
                os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
            
            #Bypass Firewall
            if (tcommand == '6'):
                os.system('git clone https://github.com/vincentcox/bypass-firewalls-by-DNS-history')

            #metasploit
            if (tcommand == '7'):
                os.system('git clone https://github.com/rapid7/metasploit-framework')

            #Sqlmap
            if (tcommand == '8'):
                os.system('git clone https://github.com/sqlmapproject/sqlmap')

            #Nmap
            if (tcommand == '9'):
                os.system('git clone https://github.com/nmap/nmap')

            #DDos Hammer
            if (tcommand == '10'):
                os.system('git clone https://github.com/rk1342k/Hammer')

            #saycheese
            if (tcommand == '11'):
                os.system('git clone https://github.com/thelinuxchoice/saycheese')

            #DDos Trojan
            if (tcommand == '12'):
                os.system('git clone https://github.com/pashayogi/Trojan')

            #Auto Deface
            if (tcommand == '13'):
                os.system('git clone https://github.com/Ranginang67/AOXdeface')

            #Ip Scanner
            if (tcommand == '14'):
                os.system('git clone https://github.com/hedii/ip-checker')
            
            #DorkScanner
            if (tcommand == '15'):
                os.system('git clone https://github.com/E4rr0r4/XGDork')

            #Spam Whatsapp
            if (tcommand == '16'):
                os.system('git clone https://github.com/RavicharanN/Spam-Whatsapp')

            #Admin FInder
            if (tcommand == '17'):
                os.system('git clone https://github.com/the-robot/admin-finder')

            #Fat rat
            if (tcommand == '18'):
                os.system('git clone https://github.com/Screetsec/TheFatRat')

            #Ip geolocation
            if (tcommand == '19'):
                os.system('git clone https://github.com/maldevel/IPGeoLocation')

            #Vbug
            if (tcommand == '20'):
                os.system('git clone https://github.com/Junior60/vbug')
                
        except KeyboardInterrupt:
            os.system('cls()')
            print (bcolors.FAIL + 'User Exit')
except KeyboardInterrupt:
    os.system('cls()')
    print (bcolors.FAIL + 'User Exit')