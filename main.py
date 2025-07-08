import RPi.GPIO as GPIO
import time

# This script controls just one pump connected to a Raspberry Pi using GPIO pins for testing purposes.

PUMP1_PIN = 17  # Pin number for pump 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP1_PIN, GPIO.OUT)

# Turn pump ON (pump is active on LOW because of the relay module I use, change to high if needed)
GPIO.output(PUMP1_PIN, GPIO.LOW)

try:
    print("Pump is ON. Press Control + C to stop the pump and end the program.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    # Turns pump OFF (again change to HIGH if you have different relay logic)
    GPIO.output(PUMP1_PIN, GPIO.HIGH)
    GPIO.cleanup()
    print("Pump is set to OFF.")
