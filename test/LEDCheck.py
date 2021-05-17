import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:

	while True:
		GPIO.output(LED_PIN, GPIO.HIGH)
		sleep(1.0)
		GPIO.output(LED_PIN, GPIO.LOW)
		sleep(1.0)

except KeyboardInterrupt:
  GPIO.cleanup()