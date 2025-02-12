# main.py
from hardware.sensors.hx711.sensor import HX711
import time
import RPi.GPIO as GPIO

def monitor_weight():
    sensor = HX711()
    try:
        print("영점 조정을 시작합니다. 로드셀에 아무것도 올려놓지 마세요.")
        time.sleep(3)
        sensor.tare()
        print("영점 조정 완료")
        
        print("\n실시간 무게 측정을 시작합니다...")
        while True:
            weight = sensor.get_weight()
            print(f"측정 무게: {weight}g")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
        
if __name__ == "__main__":
    monitor_weight()
