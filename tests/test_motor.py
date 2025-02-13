# main.py
from hardware.motors.l298n.motor import L298NMotor
import time
import RPi.GPIO as GPIO

def test_motor():
    motor = L298NMotor()
    try:
        print("모터 테스트를 시작합니다...")
        
        # 정방향 테스트
        print("정방향 회전 (0% -> 100%)")
        for speed in range(0, 101, 10):
            motor.set_speed(speed)
            print(f"속도: {speed}%")
            time.sleep(1)
            
        # 정지
        print("정지")
        motor.stop()
        time.sleep(2)
        
        # 역방향 테스트
        print("역방향 회전 (0% -> -100%)")
        for speed in range(0, -101, -10):
            motor.set_speed(speed)
            print(f"속도: {speed}%")
            time.sleep(1)
            
        # 정지
        print("정지")
        motor.stop()
        
    except KeyboardInterrupt:
        motor.stop()
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    test_motor()
