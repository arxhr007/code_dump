import os
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
p = "\033[35m"
banner=f"""{r} ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄▓██   ██▓     
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██  ██▒     
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌ ▒██ ██░     
▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌ ░ ▐██▓░     
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓  ░ ██▒▓░     
░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒   ██▒▒▒      
▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▓██ ░▒░      
 ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ▒ ▒ ░░       
 ░          ░  ░    ░ ░      ░ ░     ░    ░ ░          
      ░                            ░      ░ ░          
▓█████▄  ██▀███   ▄▄▄        ▄████  ▒█████   ███▄    █ 
▒██▀ ██▌▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒
░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒     ░   ░ ░ 
   ░       ░           ░  ░      ░     ░ ░           ░ 
 ░"""
logo=f"""{r}                 ___====-_  _-====___
           _--^^^#####//      \\\\#####^^^--_
        _-^##########// (    ) \\\\##########^-_
       -############//  |\^^/|  \\\\############-
     _/############//   (@::@)   \\\\############\\_
    /#############((     \\\\//     ))#############\\
   -###############\\\\    (oo)    //###############-
  -#################\\\\  / VV \\  //#################-
 -###################\\\\/      \\//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv){y}
                  
                   by BLINKING-IDIOT
                 {p}insta: @arn_beatz{g}
                  """
def chos(x):
 try:
  wefa=int(x)
 except:
  os.system("clear")
  print(banner)
  print(logo)
  print("not a tool...retry")
 import modules,choose
 fil=open("number.txt","r")
 ko=int(fil.read())
 if x=="0":
  modules.lis()
 elif x=="1":
  modules.screen()
 elif x=="2":
  modules.battery()
 elif x=="3":
  modules.activity()
 elif x=="4":
  modules.info()
 elif x=="5":
  modules.type()
 elif x=="6":
  modules.netstat()
 elif x=="7":
  modules.reboot()
 elif x=="8":
  modules.wifi_on()
 elif x=="9":
  modules.wifi_off()
 elif x=="10":
  modules.openurl()
 elif x=="11":
  modules.adv_prop()
 elif x=="12":
  modules.shell()
 elif x=="13":
  modules.download()
 elif x=="14":
  modules.upload()
 elif x=="15":
  modules.keycode()
 elif x=="16":
  modules.about()
 elif x=="17":
  modules.not_working()
 elif int(x)>ko:
  os.system("clear")
  print(banner)
  print(logo)
  print("not a tool...retry")
 elif x=="18":
  modules.adder()
