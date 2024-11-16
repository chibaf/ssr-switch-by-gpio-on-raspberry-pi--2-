import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os

gpio=[11,12,13,15,16,18]
path=[]
for i in range(0,len(gpio)):
  path.append('./go'+str(gpio[i])+'.txt')
#
ton=[2,1,2,1,2,1]
toff=[1,2,1,2,1,2]
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
    if threading.active_count()==len(gpio):
      continue
    elif threading.active_count()<len(gpio):
      for i in range(0,len(gpio)):
        is_file=os.path.isfile(path[i])
        if is_file:
          if qu[i].get()==0:
            th[i]=threading.Thread(target=ssr,args=(gpio[i],ton[i],toff[i],qu[i]),daemon=True)
            th[i].start()
          else:
            continue
    else:
       continue
#
  except KeyboardInterrupt:
    print("Keyboard Interrupt")
    GPIO.cleanup()
    exit()
