# tests/test_sensors.py
import pytest
from hardware.sensors.hc_sr04.sensor import HCSR04
import time

def test_hcsr04_initialization():
    sensor = HCSR04(trigger_pin=23, echo_pin=24)
    assert sensor.trigger_pin == 23
    assert sensor.echo_pin == 24

def test_distance_measurement():
    sensor = HCSR04()
    distance = sensor.measure_distance()
    assert isinstance(distance, (float, type(None)))
    if distance is not None:
        assert 2 <= distance <= 400  # HC-SR04의 측정 범위는 2cm~400cm
