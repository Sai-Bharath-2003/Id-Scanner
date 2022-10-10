
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

reader =SimpleMFRC522()

print("place tag")

try:
    while True:
        id,text=reader.read()
        print(hex(id))
        time.sleep(2)
finally:
    GPIO.cleanup()
