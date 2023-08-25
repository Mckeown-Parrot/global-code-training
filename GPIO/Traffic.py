import os
from gpiozero import LED, Buzzer
from time import sleep
import RPi.GPIO as GPIO



ledred = LED(17) # 17 stands for the number on the gpio
ledyellow = LED(18) # 18 stands for the number on the gpio
ledgreen = LED(27) # 27 stands for the number on the gpio


while True:
    #Redlight
    ledred.on()
    sleep(5)
    Buzzer.on()
    ledred.off()
    Buzzer.of()
    #Yellowlight
    ledyellow.on()
    sleep(5)
    Buzzer.on()
    ledyellow.off()
    Buzzer.off()
    #Greenlight
    ledgreen.on()
    sleep(5)
    Buzzer.on()
    ledgreen.off()
    Buzzer.off()