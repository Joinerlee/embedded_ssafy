import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정 방식 지정 (BCM 또는 BOARD)
GPIO.setmode(GPIO.BCM)

# 사용할 GPIO 핀 번호 정의
LED_PIN = 18  # GPIO 18번 핀 사용
BUTTON_PIN = 23  # GPIO 23번 핀 사용

# 핀 설정
GPIO.setup(LED_PIN, GPIO.OUT)  # LED 핀을 출력으로 설정
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 버튼 핀을 입력으로 설정 (풀업 저항 사용)

try:
    while True:
        # 버튼 상태 읽기
        button_state = GPIO.input(BUTTON_PIN)
        
        # 버튼이 눌렸을 때 (풀업 저항으로 인해 눌렸을 때 0)
        if button_state == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH)  # LED 켜기
            print("LED ON")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)   # LED 끄기
            print("LED OFF")
            
        time.sleep(0.1)  # 디바운싱을 위한 짧은 대기 시간

except KeyboardInterrupt:
    print("프로그램 종료")
    
finally:
    # GPIO 설정 초기화
    GPIO.cleanup()