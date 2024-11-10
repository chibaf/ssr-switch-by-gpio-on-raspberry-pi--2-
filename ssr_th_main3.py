import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os

gpio=[11,12,13,15,16,18]
pin_id=[]
for i in range(0,len(gpio)):
  pin_id.append(str(gpio[i]))
path=[]
for i in range(0,len(gpio)):
  path.append('./go'+pin_id[i]+'.txt')
#  print(path[i])
#exit()
ton=[1,1,1,1,1,1]
toff=[1,1,1,1,1,1]
qu=[]
for i in range(0,len(gpio)):
  qu.append(queue.Queue())
#  print(qu[i])
#exit()
#
while True:
  try:
    if threading.active_count()==len(gpio):
      continue
    elif threading.active_count()<3:
     is_file1=os.path.isfile(path1)
     if is_file1:
       th1 = threading.Thread(target=ssr,args=(11,t1on,t1of,q1),name=pin_id1,daemon=True)
       th1.start()
       print(th1.name)
     is_file2=os.path.isfile(path2)
     if is_file2:
       th2 = threading.Thread(target=ssr,args=(18,t2on,t2of,q2),name=pin_id2,daemon=True)
       th2.start()
       print(th2.name)
     else:
       continue
#       print("go??.txt not found")
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
