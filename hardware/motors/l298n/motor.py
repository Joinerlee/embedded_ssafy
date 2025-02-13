# hardware/motors/l298n/motor.py
import RPi.GPIO as GPIO
import time

class L298NMotor:
    def __init__(self, ena=12, in1=17, in2=18):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.ena, 100)  # 100Hz PWM 주파수
        self.pwm.start(0)
        
    def set_speed(self, speed):
        # speed: -100 to 100
        speed = max(-100, min(100, speed))  # 속도 범위 제한
        
        if speed > 0:
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)
            self.pwm.ChangeDutyCycle(speed)
        elif speed < 0:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)
            self.pwm.ChangeDutyCycle(abs(speed))
        else:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.LOW)
            self.pwm.ChangeDutyCycle(0)
            
    def stop(self):
        self.set_speed(0)
