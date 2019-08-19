import RPi.GPIO as GPIO
import time


def door_lock(channel):
    GPIO.output(channel, GPIO.LOW)

def reset(channel):
    time.sleep(10)
    door_lock(channel)
    time.sleep(1)
    GPIO.cleanup()

def door_unlock():
    channel = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.out)
    GPIO.output(channel, GPIO.HIGH)
    reset(channel)
