# main.py
from hardware.sensors.hc_sr04.sensor import HCSR04
import time

def test_sensor():
    sensor = HCSR04()
    try:
        while True:
            distance = sensor.measure_distance()
            if distance is not None:
                print(f"거리: {distance} cm")
            else:
                print("측정 실패")
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    test_sensor()
