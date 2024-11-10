import threading
import queue,time
import serial,sys
from ssr_sw_th import ssr
import RPi.GPIO as GPIO
import datetime
from time import sleep
import os

pin_id1=str(11)
path1='./go'+pin_id1+'.txt'
pin_id2=str(18)
path2='./go'+pin_id2+'.txt'
t1on=1
t1of=2
t2on=2
t2of=1

q1 =queue.Queue()  # queue which stores a result of a thread
q2 =queue.Queue()  # queue which stores a result of a thread
#
while True:
  try:
    if threading.active_count()==3:
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
