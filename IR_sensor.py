import RPi.GPIO as GPIO

IR_SENSOR_PIN = 26  

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

def detect_object():
    if GPIO.input(IR_SENSOR_PIN) == 0:
        print("Waste detected", flush=True)
        return True
    return False

"""
# To test IR sensor
ch = 'y'
while ch == 'y':
    print(detect_object())  
    ch = input("ch= ")
"""
