import dht
import machine
from machine import Pin, I2C
import ssd1306
import time



def temp_sensor():
    d = dht.DHT11(machine.Pin(4))
    d.measure()
    data = [d.temperature(), d.humidity()]
    return data

def oled(input):
    # using default address 0x3C
    i2c = I2C(sda=Pin(23), scl=Pin(22))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.text(f"Temp: {input[0]} C", 0, 0, 1)
    display.text(f"Humidity: {input[1]} %", 0, 8, 1)
    display.show()


if __name__ == "__main__":
    while True:
        climate_data = temp_sensor()
        oled(climate_data)
        time.sleep(5)