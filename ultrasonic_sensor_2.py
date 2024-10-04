import RPi.GPIO as GPIO
import time

# Define the pins for the HC-SR04
TRIG_PIN = 7
ECHO_PIN = 11

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        # Clear the TRIG_PIN by setting it LOW
        GPIO.output(TRIG_PIN, False)
        time.sleep(0.000002)

        # Set the TRIG_PIN HIGH for 10 microseconds
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)

        # Measure the duration of the echo pulse
        start_time = time.time()
        while GPIO.input(ECHO_PIN) == 0:
            start_time = time.time()
        while GPIO.input(ECHO_PIN) == 1:
            end_time = time.time()
        duration = end_time - start_time

        # Calculate the distance
        distance = (duration * 34300) / 2

        # Print the distance to the console
        print("Distance: {:.2f} cm".format(distance))

        # Wait for 500 milliseconds
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
