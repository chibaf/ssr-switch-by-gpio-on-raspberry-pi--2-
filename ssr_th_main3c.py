import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os
import random

gpio=[11,12,13,15,16,18]
to=[2,3,4,2,6,1]
ts=[1,1,1,1,1,1]
path=[]
for i in range(0,len(gpio)):
  path.append('./go'+str(gpio[i])+'.txt')
#
qu=[]
for i in range(0,len(gpio)):
  qu.append(queue.Queue())
th=[]
for i in range(0,len(gpio)):
  th.append("")
for i in range(0,len(gpio)):
  qu[i].put(0)
#
while True:
  try:
    if threading.active_count()==len(gpio)+1:
      continue
    elif threading.active_count()<len(gpio)+1:
      for i in range(0,len(gpio)):
        is_file=os.path.isfile(path[i])
        if is_file:
          if qu[i].get()==0:
            print(i)
            t_on=to[i]
            t_off=ts[i]
#            t_on=random.randrange(1,4,1)
#            t_off=random.randrange(1,4,1)
            th[i]=threading.Thread(target=ssr,args=(gpio[i],t_on,t_off,qu[i]),daemon=True)
            th[i].start()
          else:
            qu[i].put(1)
    else:
       continue
#
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
