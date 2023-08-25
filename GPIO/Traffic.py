from gpiozero import LED
from time import sleep

ledred = LED(17) # 17 stands for the number on the gpio
ledyellow = LED(18) # 18 stands for the number on the gpio
ledgreen = LED(27) # 27 stands for the number on the gpio


while True:
    #Redlight
    ledred.on()
    sleep()
    ledred.off()
    #Yellowlight
    ledyellow.on()
    sleep(5)
    ledyellow.off()
    #Greenlight
    ledgreen.on()
    sleep(5)
    ledgreen.off()