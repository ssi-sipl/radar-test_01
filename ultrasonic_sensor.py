#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

def measure_distance():
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

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(2)

def cleanup_gpio():
    GPIO.cleanup()

if __name__ == "__main__":
    PIN_TRIGGER = 7
    PIN_ECHO = 11

    try:
        print("Waiting for sensor to settle")
        setup_gpio()

        print("Starting continuous distance measurement")
        while True:
            distance = measure_distance()
            print(f"Distance: {distance} cm")
            time.sleep(1)  # Wait for 1 second before next measurement

    except KeyboardInterrupt:
        print("Measurement stopped")

    finally:
        cleanup_gpio()
