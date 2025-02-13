import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정 방식 지정 (BCM 또는 BOARD)
GPIO.setmode(GPIO.BCM)

# 사용할 GPIO 핀 번호 설정 (예: GPIO23)
LED_PIN = 23

# 핀 설정 (출력)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # LED 켜기
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # 1초 대기
        
        # LED 끄기
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # 1초 대기

except KeyboardInterrupt:
    # 프로그램 종료시 GPIO 설정 초기화
    print("프로그램을 종료합니다.")
    GPIO.cleanup()import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정 방식 지정 (BCM 또는 BOARD)
GPIO.setmode(GPIO.BCM)

# 사용할 GPIO 핀 번호 설정 (예: GPIO18)
LED_PIN = 18

# 핀 설정 (출력)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # LED 켜기
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # 1초 대기
        
        # LED 끄기
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # 1초 대기

except KeyboardInterrupt:
    # 프로그램 종료시 GPIO 설정 초기화
    print("프로그램을 종료합니다.")
    GPIO.cleanup()