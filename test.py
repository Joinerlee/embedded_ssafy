from gpiozero import LED
import asyncio

# LED 설정
led1 = LED(23)
led2 = LED(24)

async def control_leds():
    while True:
        print("LED ON")
        led1.on()
        led2.on()
        await asyncio.sleep(1)
        
        print("LED OFF")
        led1.off()
        led2.off()
        await asyncio.sleep(1)

async def main():
    try:
        await control_leds()
    except KeyboardInterrupt:
        print("프로그램 종료")

if __name__ == "__main__":
    asyncio.run(main())