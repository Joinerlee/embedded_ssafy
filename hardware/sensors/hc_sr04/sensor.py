# hardware/sensors/hc_sr04/sensor.py
import RPi.GPIO as GPIO
import time

class HCSR04:
    def __init__(self, trigger_pin=23, echo_pin=24):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        
    def measure_distance(self):
        # 트리거 신호 발생
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)  # 10마이크로초 대기
        GPIO.output(self.trigger_pin, False)
        
        start_time = time.time()
        stop_time = time.time()
        
        # 에코 신호 시작 시간 측정
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
            if time.time() - stop_time > 0.1:  # 타임아웃 처리
                return None
            
        # 에코 신호 종료 시간 측정
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()
            if stop_time - start_time > 0.1:  # 타임아웃 처리
                return None
            
        # 거리 계산
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2  # 음속(343m/s)을 사용하여 거리 계산
        
        return round(distance, 2)  # cm 단위로 반환
