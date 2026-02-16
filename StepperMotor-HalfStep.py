from machine import Pin
import time

sm1 = Pin(5, Pin.OUT)
sm2 = Pin(18, Pin.OUT)
sm3 = Pin(19, Pin.OUT)
sm4 = Pin(21, Pin.OUT)

while True:

    sm1.on()
    sm2.off()
    sm3.off()
    sm4.off()
    time.sleep(0.005)

    sm1.on()
    sm2.on()
    sm3.off()
    sm4.off()
    time.sleep(0.005)

    sm1.off()
    sm2.on()
    sm3.off()
    sm4.off()
    time.sleep(0.005)

    sm1.off()
    sm2.on()
    sm3.on()
    sm4.off()
    time.sleep(0.005)

    sm1.off()
    sm2.off()
    sm3.on()
    sm4.off()
    time.sleep(0.005)

    sm1.off()
    sm2.off()
    sm3.on()
    sm4.on()
    time.sleep(0.005)

    sm1.off()
    sm2.off()
    sm3.off()
    sm4.on()
    time.sleep(0.005)

    sm1.on()
    sm2.off()
    sm3.off()
    sm4.on()
    time.sleep(0.005)
