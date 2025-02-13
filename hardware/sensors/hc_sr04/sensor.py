import RPi.GPIO as GPIO
import time

class HCSR04:
    def __init__(self, trigger_pin=23, echo_pin=24):
        """
        HC-SR04 초음파 센서 초기화
        :param trigger_pin: 트리거 신호 핀 번호 (기본값: 23)
        :param echo_pin: 에코 신호 핀 번호 (기본값: 24)
        """
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        
        # GPIO 모드 설정
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        
        # 초기 상태 설정
        GPIO.output(self.trigger_pin, False)
        time.sleep(0.5)  # 센서 안정화 대기
        
    def measure_distance(self):
        """
        거리 측정 함수
        :return: 측정된 거리(cm) 또는 측정 실패시 None
        """
        try:
            # 트리거 신호 초기화
            GPIO.output(self.trigger_pin, False)
            time.sleep(0.1)  # 안정화를 위한 대기
            
            # 트리거 신호 발생 (10마이크로초)
            GPIO.output(self.trigger_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trigger_pin, False)
            
            timeout_start = time.time()
            
            # 에코 신호 시작 대기
            while GPIO.input(self.echo_pin) == 0:
                if time.time() - timeout_start > 0.1:  # 100ms 타임아웃
                    return None
                start_time = time.time()
            
            # 에코 신호 종료 대기
            while GPIO.input(self.echo_pin) == 1:
                if time.time() - timeout_start > 0.1:  # 100ms 타임아웃
                    return None
                stop_time = time.time()
            
            # 거리 계산
            time_elapsed = stop_time - start_time
            distance = (time_elapsed * 34300) / 2  # 음속(343m/s)을 사용하여 거리 계산
            
            # 유효 범위 확인 (2cm ~ 400cm)
            if 2 <= distance <= 400:
                return round(distance, 2)
            else:
                return None
                
        except Exception as e:
            print(f"측정 중 오류 발생: {e}")
            return None
            
    def cleanup(self):
        """
        GPIO 핀 정리
        """
        GPIO.cleanup()
