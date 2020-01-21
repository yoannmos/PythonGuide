from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='*IPadress*')

led = LED(18, pin_factory=factory)  # led on this Pi

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)