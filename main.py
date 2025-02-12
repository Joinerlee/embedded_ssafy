# main.py
from hardware.sensors.hx711.sensor import HX711
import time

def calibrate_sensor():
    sensor = HX711()
    try:
        print("영점 조정을 시작합니다. 로드셀에 아무것도 올려놓지 마세요.")
        time.sleep(3)
        sensor.tare()
        print("영점 조정 완료")
        
        print("\n알고 있는 무게의 물체를 올려주세요 (예: 100g)")
        input("물체를 올린 후 Enter를 눌러주세요...")
        
        raw_value = sensor.get_weight()
        known_weight = float(input("올려놓은 물체의 실제 무게(g)를 입력하세요: "))
        
        reference_unit = raw_value / known_weight
        sensor.set_reference_unit(reference_unit)
        print(f"캘리브레이션 완료: reference_unit = {reference_unit}")
        
        while True:
            weight = sensor.get_weight()
            print(f"측정 무게: {weight}g")
            time.sleep(1)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        
if __name__ == "__main__":
    calibrate_sensor()
