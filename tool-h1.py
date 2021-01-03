'''
pip install pyfiglet
pip install termcolor
pip install pyqrcode
pip install socket
pip install subprocess
pip install stegano
pip install pypng
pip install pyautogui
'''
import pyfiglet
from termcolor import colored
ascii_banner = pyfiglet.figlet_format("Tool-h")
print(ascii_banner)
print(colored("---------created by alhassan alharbi----------",'yellow'))
'''___________________________________________________________________________'''
print("what do you want?")
print(colored("search the web [ 1 ]",'red'))
print(colored('cyberscurity [ 2 ]','blue'))
print(colored('spam MSG [ 3 ] ','green'))
print(colored('QR code [ 4 ]','red'))
print(colored('creat password [ 5 ]','blue'))
tool=input("enter the number: ")
"""___________________________________________________________________________"""
if (tool=="1"):
  from webbrowser import open
  from termcolor import colored
#__________
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  #______
  print("       /\    |         |       |")
  print("      /  \   |         |       |")
  print("     /____\  |         |-------|")
  print("    /      \ |         |       |")
  print("   /        \|_________|       |")
  print("")
  print("")
  print(colored('YouTube [ 1 ]','red'))
  print(colored('Twitter [ 2 ]','blue'))
  print(colored("waybackmechin [ 3 ]",'red'))
  print(colored('virustotal [ 4 ]','blue'))
  print("")
  pro=input("enter the number: ")
  print("_"*60)
  if (pro=="1"):
    sea=input("enter what do you want search: ")
    open('https://www.youtube.com/results?search_query='+sea)
  if (pro=="2"):
    sea=input("enter what do you want search: ")
    open('https://twitter.com/search?q='+sea)
  if (pro=="3"):
    sea=input("enter the url: ")
    open('https://web.archive.org/web/*/'+sea)
  if(pro=="4"):
  	open('https://www.virustotal.com/gui/')

'''______________________________________________________________________'''


'''_________________________________________________________________________'''

if (tool=="2"):
  print(colored(" DNS website (1)",'green'))
  print(colored(" ip ping (2)",'yellow'))
  print(colored(" hash (3)",'green'))
  print(colored(" hide data inside pictures (4)",'yellow'))
  print(colored(" show data from inside pictures (5)",'yellow'))
  print(" ping scan network (6)")
  cyber=input("enter the number: ")
  if (cyber=="1"):
    #!/usr/bin/python3
    import socket
    import pyfiglet

    ascii_banner = pyfiglet.figlet_format("hassan DNS tool")
    print(ascii_banner)
    print("---------  Cyber Python  ---------")
    print("")

    domain = input("What is the domain? \n")
    ip = socket.gethostbyname(domain)


    print('The DNS of', domain, 'is: ', ip)

    ascii_banner2 = pyfiglet.figlet_format("End")
    print(ascii_banner2)
  if (cyber=="2"):
    #!/usr/bin/python3

    import subprocess
    from termcolor import colored
    from art import *
    tprint("SGS",font="block",chr_ignore=True)
    print("--------- ALHASSAN ALHARBI ---------")
    print("---------  Cyber Python  ---------")
    print("")

    host = input("What is your\he IP? \n")
    result = subprocess.call(['ping','-c' '1', host])
    if result == 0:
      print(colored('The Host is UP', 'green'))
    else:
      print(colored('The Host is DOWN', 'red'))
  if (cyber=="3"):
    print("--------- ALHASSAN ALHARBI ---------")
    print("---------  Cyber Python  ---------")
    print("")

    
    import hashlib

    password = input("Hi, what is your password? \n")

    print("SHA1 Hash: ")
    sha1_pass = hashlib.sha1(password.encode())
    print(sha1_pass.hexdigest())

    print("MD5 Hash: ")
    md5_pass = hashlib.md5(password.encode())
    print(md5_pass.hexdigest())
  if(cyber=="4"):
    #!/usr/bin/python3
    from stegano import lsb
 
    print(r"""

           _ . - = - . _
       . "  \  \   /  /  " .
     ,  \                 /  .
   . \   _,.--~=~"~=~--.._   / .
  ;  _.-"  / \ !   ! / \  "-._  .
 / ,"     / ,` .---. `, \     ". \
/.'   `~  |   /:::::\   |  ~`   '.\
\`.  `~   |   \:::::/   | ~`  ~ .'/
 \ `.  `~ \ `, `~~~' ,` /   ~`.' /
  .  "-._  \ / !   ! \ /  _.-"  .
   ./    "=~~.._  _..~~=`"    \.
     ,/         ""          \,
      . _/             \_ . 
          " - ./. .\. - "
 
                   """)

    print("--------- ALHASSAN ALHARBI ---------")
    print("---------  Cyber Python  ---------")
    print("")
    print(colored("يجب حفظ الصورة في نفس المجلد الذي توجد فيه هذه الأداة (للتعرف على الصورة)",'red'))
    secret=lsb.hide(input('enter the pictur name ==> '),input("enter the data: "))
    secret.save('secret_image.png')
  if(cyber=="5"):
    #!/usr/bin/python3
    from stegano import lsb

    print(r"""

           _ . - = - . _
       . "  \  \   /  /  " .
     ,  \                 /  .
   . \   _,.--~=~"~=~--.._   / .
  ;  _.-"  / \ !   ! / \  "-._  .
 / ,"     / ,` .---. `, \     ". \
/.'   `~  |   /:::::\   |  ~`   '.\
\`.  `~   |   \:::::/   | ~`  ~ .'/
 \ `.  `~ \ `, `~~~' ,` /   ~`.' /
  .  "-._  \ / !   ! \ /  _.-"  .
   ./    "=~~.._  _..~~=`"    \.
     ,/         ""          \,
      . _/             \_ . 
          " - ./. .\. - "
 
                    """)

    print("--------- ALHASSAN ALHARBI ---------")
    print("---------  Cyber Python  ---------")
    print("")
    print(colored("يجب حفظ الصورة في نفس المجلد الذي توجد فيه هذه الأداة (للتعرف على الصورة)",'red'))

    msg = lsb.reveal(input("enter the pictur name ==> "))
    print("The secret message is:", msg)
  if(cyber=="6"):
    #!/usr/bin/python3 

    import subprocess
    from termcolor import colored
    from art import *
    tprint("SGS",font="block",chr_ignore=True)
    print("---------alhassanalharbi ---------")
    print("---------  Cyber Python  ---------")
    print("")

    count = 0
    for ping in range(1,100): 
            host = input("What is your IP? \n")

            result = subprocess.call(['ping', '-c','1', host],stdout = subprocess.PIPE)

            if result == 0:
                    print(host, (colored(' - the Host is UP', 'green')))
            else:
                     print(host, (colored(' - the Host is DOWN', 'red')))
            count = count + 1

    print('Scanned',count,'systems!')  
if (tool=="3"):
   import pyautogui
   from time import sleep


   print("حمل مكتبة pyautogui")
   print("افتح الشاشة التي بها الرسالة ")
   msg=input("enter the msg: ")
   num_msg=int(input("enter number of msg: "))
   print("عند اختيار الوقت اضغط على مربع الرسالة مباشرة")
   time_msg=float(input("enter the time: "))

   for num in range(num_msg+1):
       pyautogui.typewrite(msg)
       sleep(time_msg)
       pyautogui.press('enter')
       sleep(time_msg)
if(tool=='4'):
   import pyqrcode as qqrr
   print("")
   text = input("Please Enter your Massage OR Link : ")
   FileName = input("Please Enter File Name : ")
   # to create the qrcode :
   g = qqrr.create(text)

   g.png(FileName + ".png",scale=10)
if(tool=="5"):
   import random
   def GetPassword(data):
       Max=int(input('enter number ==> '))
       password=""
       while len(password)!=Max:
           value=random.choice(data)
           password+=value
       return password
   data='12345678910qwertyuiopasdfghjklzxcvbnm!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM'
   print(GetPassword(data))
