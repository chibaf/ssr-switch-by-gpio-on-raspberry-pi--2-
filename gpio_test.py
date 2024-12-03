import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# 11,12,13,15,16,18 = GPIO pin No. on Raspberry Pi board
gpin=[11,12,13,15,16,18]
rgpin=gpin[::-1] # reverse
for i in range(0,len(gpin)):
  GPIO.setup(gpin[i],GPIO.OUT)
for i in range(0,len(gpin)):
  GPIO.output(gpin[i], 0)
#
while True:
  try:
    for i in range(0,len(gpin)):
      GPIO.output(gpin[i], 1)
      time.sleep(0.5)
#
    for i in range(0,len(gpin)):
      GPIO.output(rgpin[i], 0) # reverse
      time.sleep(0.5)
  except KeyboardInterrupt:
    print("KeyboardInterrupt")
    GPIO.cleanup()
    exit()