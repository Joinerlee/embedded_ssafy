import asyncio
import RPi.GPIO as GPIO

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)  # 개별적으로 설정
GPIO.setup(24, GPIO.OUT)  # 개별적으로 설정

# LED 제어 코루틴
async def control_leds():
    while True:
        print("LED ON")
        GPIO.output([23, 24], GPIO.HIGH)  # LED 켜기
        await asyncio.sleep(1)            # 비동기 대기
        
        print("LED OFF")
        GPIO.output([23, 24], GPIO.LOW)   # LED 끄기
        await asyncio.sleep(1)            # 비동기 대기

# 시스템 모니터링 코루틴
async def monitor_system():
    while True:
        print("시스템 동작 중...")
        await asyncio.sleep(2)

# 메인 코루틴
async def main():
    try:
        # 두 코루틴을 동시에 실행
        await asyncio.gather(
            control_leds(),
            monitor_system()
        )
    except KeyboardInterrupt:
        print("프로그램 종료")
    finally:
        GPIO.cleanup()

# 프로그램 실행
asyncio.run(main())