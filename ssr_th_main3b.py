import threading
import queue
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import random

gpio=[11,12,13,15,16,18]
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
    if threading.active_count()==len(gpio):
      continue
    elif threading.active_count()<len(gpio):
      for i in range(0,len(gpio)):
        if qu[i].get()==0:
          t_on=random.randrange(1,5,1)
          t_off=random.randrange(1,5,1)
          th[i]=threading.Thread(target=ssr,args=(gpio[i],t_on,t_off,qu[i]),daemon=True)
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
