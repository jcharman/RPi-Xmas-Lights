#Import required libraries
import RPi.GPIO as GPIO
from multiprocessing import Process
import time

#Add pin numbers to arrays
pins = [12,25,24,23,18]
pin2 = [16,26,13,6,5]

#Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set up and flash the LEDs
def pins1():
    for pin in pins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin,GPIO.LOW)

def pins2():
    for p in pin2:
        GPIO.setup(pin2,GPIO.OUT)
        GPIO.output(p,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(p,GPIO.LOW)

try:
    #Run the methods until Ctrl+C is pressed
    while True:
        p1 = Process(target=pins1)
        p2 = Process(target=pins2)
        p1.start()
        p2.start()
        p1.join()
        p2.join()

#Catch the keyboard interrupt
except KeyboardInterrupt:
    #Turn off LEDs
    GPIO.cleanup()


