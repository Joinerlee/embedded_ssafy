from hardware.sensors.hc_sr04.sensor import HCSR04
import time
import RPi.GPIO as GPIO

def main():
    # 센서 객체 생성
    sensor = HCSR04(trigger_pin=23, echo_pin=24)
    
    try:
        print("거리 측정을 시작합니다. 종료하려면 Ctrl+C를 누르세요.")
        while True:
            distance = sensor.measure_distance()
            
            if distance is not None:
                print(f"측정 거리: {distance} cm")
            else:
                print("측정 실패 - 센서 연결 상태를 확인하세요")
            
            time.sleep(1)  # 1초 대기
            
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
    finally:
        sensor.cleanup()

if __name__ == "__main__":
    main()