from machine import Pin
import time

sm1 = Pin(5, Pin.OUT)
sm2 = Pin(18, Pin.OUT)
sm3 = Pin(19, Pin.OUT)
sm4 = Pin(21, Pin.OUT)

while True:

    for _ in range(500):   # 500 × 4 steps = 2000 steps = 360°

        # 1100
        sm1.on()
        sm2.on()
        sm3.off()
        sm4.off()
        time.sleep(0.005)

        # 0110
        sm1.off()
        sm2.on()
        sm3.on()
        sm4.off()
        time.sleep(0.005)

        # 0011
        sm1.off()
        sm2.off()
        sm3.on()
        sm4.on()
        time.sleep(0.005)

        # 1001
        sm1.on()
        sm2.off()
        sm3.off()
        sm4.on()
        time.sleep(0.005)

    time.sleep(1)


    for _ in range(500):

        # 1001
        sm1.on()
        sm2.off()
        sm3.off()
        sm4.on()
        time.sleep(0.005)

        # 0011
        sm1.off()
        sm2.off()
        sm3.on()
        sm4.on()
        time.sleep(0.005)

        # 0110
        sm1.off()
        sm2.on()
        sm3.on()
        sm4.off()
        time.sleep(0.005)

        # 1100
        sm1.on()
        sm2.on()
        sm3.off()
        sm4.off()
        time.sleep(0.005)

    time.sleep(1)
