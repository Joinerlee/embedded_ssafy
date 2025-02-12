import RPi.GPIO as GPIO
from hardware.sensors.hc_sr04.sensor import HCSR04
import time

def test_sensor():
    try:
        sensor = HCSR04()
        while True:
            distance = sensor.measure_distance()
            if distance is not None:
                print(f"거리: {distance} cm")
            else:
                print("측정 실패")
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
