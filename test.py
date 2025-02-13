from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
import time

# GPIO 핀 팩토리 설정
factory = PiGPIOFactory()

# LED 설정
led1 = LED(23, pin_factory=factory)
led2 = LED(24, pin_factory=factory)

try:
    while True:
        print("ON")
        led1.on()
        led2.on()
        time.sleep(1)
        
        print("OFF")
        led1.off()
        led2.off()
        time.sleep(1)

except KeyboardInterrupt:
    print("프로그램 종료")