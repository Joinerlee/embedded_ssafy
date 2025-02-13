import RPi.GPIO as GPIO
import asyncio

# GPIO 설정 초기화
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

async def control_leds():
    while True:
        print("LED ON")
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        await asyncio.sleep(1)
        
        print("LED OFF")
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        await asyncio.sleep(1)

async def main():
    try:
        await control_leds()
    except KeyboardInterrupt:
        print("프로그램 종료")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    asyncio.run(main())