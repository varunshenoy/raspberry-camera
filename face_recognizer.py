from picamera import PiCamera
import RPi.GPIO as GPIO
import cv2

camera = PiCamera()

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        camera.capture('image.jpg')
