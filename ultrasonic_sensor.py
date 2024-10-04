#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 7
    PIN_ECHO = 11
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    return PIN_TRIGGER, PIN_ECHO

def measure_distance(PIN_TRIGGER, PIN_ECHO):
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    
    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()
    
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    return distance

try:
    PIN_TRIGGER, PIN_ECHO = setup()
    print("Sensor initialized. Starting continuous measurement.")
    
    while True:
        distance = measure_distance(PIN_TRIGGER, PIN_ECHO)
        print(f"\rDistance: {distance} cm", end="", flush=True)
        time.sleep(0.5)  # Adjust this value to change update frequency

except KeyboardInterrupt:
    print("\nMeasurement stopped by user")
finally:
    GPIO.cleanup()
