import RPi._GPIO as GPIO
from time import sleep

BuzzerPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT) 
GPIO.setwarnings(False)

global Buzz 
Buzz = GPIO.PWM(BuzzerPin, 440) 


while True:
	Buzz.start(1)
	sleep(50)
	Buzz.stop(2)
	sleep(1)