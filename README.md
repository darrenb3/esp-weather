# ESP Weather

This is a repository for esp-weather, a basic weather station based on the ESP32-WROOM. It uses a DHT11 sensor and a 1306 I2C display. Your ESP32 will need to be flashed with micropython for code to execute.

Below is a brief discription of how to wire the project up.

ESP32:

    Tie 3v3 Out to + rail
    Tie GND to - rail

DHT11:

    VCC on + rail
    Data to GPIO4
    GND on - rail

OLED1306:

    GND on - rail
    VCC on + rail
    SDA on GPIO23
    SCL on GPIO22

