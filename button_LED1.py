# refernce: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
# modified

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#GPIO.setmode(GPIO.BOARD) #GPIO.BOARD not working

led1 = 5
button1 = 6

# Set button to be an input pin and set initial value to be pulled low (off)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led1, GPIO.OUT)

while True:
    if GPIO.input(button1) == GPIO.HIGH:
        print("Button was pushed")
        time.sleep(0.1)
        GPIO.output(led1, GPIO.HIGH)

    if GPIO.input(button1) == GPIO.LOW:
        print("Button was un-pushed")
        time.sleep(0.1)
        GPIO.output(led1, GPIO.LOW)
