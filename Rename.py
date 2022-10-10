import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader =SimpleMFRC522()

print("place tag")
try:
    
    rename=input("Enter the Correct Roll No  -  ")
    reader.write(rename)
    print("Successfull changed")
finally:
    GPIO.cleanup()