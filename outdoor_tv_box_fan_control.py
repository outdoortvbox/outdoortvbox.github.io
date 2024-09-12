import RPi.GPIO as GPIO
import time
import Adafruit_DHT

# Setup GPIO
FAN_PIN = 17
TEMP_SENSOR_PIN = 4
TEMP_THRESHOLD = 30  # Temperature in Celsius to turn the fan on

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

# DHT sensor setup
sensor = Adafruit_DHT.DHT11

def get_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, TEMP_SENSOR_PIN)
    return temperature

try:
    while True:
        temp = get_temperature()
        if temp:
            print(f"Current Temperature: {temp}°C")
            
            if temp > TEMP_THRESHOLD:
                GPIO.output(FAN_PIN, GPIO.HIGH)
                print("Fan ON: Temperature exceeded threshold.")
            else:
                GPIO.output(FAN_PIN, GPIO.LOW)
                print("Fan OFF: Temperature below threshold.")
        
        time.sleep(10)  # Wait for 10 seconds before next check

except KeyboardInterrupt:
    print("Program terminated.")
    
finally:
    GPIO.cleanup()
