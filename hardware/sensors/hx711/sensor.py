# hardware/sensors/hx711/sensor.py
import RPi.GPIO as GPIO
import time
import statistics

class HX711:
    def __init__(self, dout_pin=5, pd_sck_pin=6):
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.reference_unit = 1
        self.offset = 0
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pd_sck_pin, GPIO.OUT)
        GPIO.setup(self.dout_pin, GPIO.IN)
        
        self.power_up()
        
    def power_up(self):
        GPIO.output(self.pd_sck_pin, False)
        time.sleep(0.1)
        
    def power_down(self):
        GPIO.output(self.pd_sck_pin, False)
        GPIO.output(self.pd_sck_pin, True)
        time.sleep(0.01)
        
    def read_raw_value(self):
        while GPIO.input(self.dout_pin):
            time.sleep(0.01)
            
        data = 0
        for _ in range(24):
            GPIO.output(self.pd_sck_pin, True)
            time.sleep(0.000001)
            GPIO.output(self.pd_sck_pin, False)
            time.sleep(0.000001)
            data = (data << 1) | GPIO.input(self.dout_pin)
            
        GPIO.output(self.pd_sck_pin, True)
        time.sleep(0.000001)
        GPIO.output(self.pd_sck_pin, False)
        
        if data & 0x800000:
            data = data - (1 << 24)
            
        return data
    
    def get_weight(self, num_readings=5):
        values = []
        for _ in range(num_readings):
            value = self.read_raw_value()
            values.append(value)
            time.sleep(0.1)
            
        average = statistics.mean(values)
        weight = (average - self.offset) / self.reference_unit
        return round(weight, 2)
    
    def tare(self, num_readings=20):
        values = []
        for _ in range(num_readings):
            values.append(self.read_raw_value())
            time.sleep(0.1)
        self.offset = statistics.mean(values)
        
    def set_reference_unit(self, reference_unit):
        self.reference_unit = reference_unit
