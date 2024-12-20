import time
import serial
from pylab import *
import sys

y1=[0]*100
y2=[0]*100
x=range(0, 100, 1)
ser=serial.Serial(sys.argv[1],19200)
while True:
  try:
    line=ser.readline()
    line2=line.strip().decode('utf-8')#,errors='replace')
    line=line2.split(',')
    y1.insert(0,float(line[1]))
    y2.insert(0,float(line[2]))
    #print(line)
    y1.pop(100)
    y2.pop(100)
    clf()
    ylim(-1.2,1.2)
    line1,=plot(x,y1,label='Ts 1')
    line2,=plot(x,y2,label='Ts 2')
    legend(handles=[line1, line2])
    pause(0.01)
  except KeyboardInterrupt:
    ser.close()
    print ('exiting')
    exit()