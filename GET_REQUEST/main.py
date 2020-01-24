from machine import Pin, I2C
import ssd1306
from time import sleep
import network
import urequests as requests

import json

with open('config.json') as config_file:
    credentials = json.load(config_file)






# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(4), sda=Pin(5))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#--------------------------------



def draw_circle( x0, y0, radius):
    x = radius
    y = 0
    err = 0

    while x >= y:
        oled.pixel(x0 + x, y0 + y, 1)
        oled.pixel(x0 + y, y0 + x, 1)
        oled.pixel(x0 - y, y0 + x, 1)
        oled.pixel(x0 - x, y0 + y, 1)
        oled.pixel(x0 - x, y0 - y, 1)
        oled.pixel(x0 - y, y0 - x, 1)
        oled.pixel(x0 + y, y0 - x, 1)
        oled.pixel(x0 + x, y0 - y, 1)

        y += 1
        err += 1 + 2*y
        if 2*(err-x) + 1 > 0:
            x -= 1
            err += 1 - 2*x
        oled.show()


oled.fill(0)
oled.show()

for i in range(63):
    oled.pixel(0,i,1)
    oled.show
    sleep(0.002)

for i in range(127):
    oled.pixel(i,63,1)
    oled.show
    sleep(0.002)

for i in range(63):
    oled.pixel(127,i,1)
    oled.show
    sleep(0.002)

for i in range(127):
    oled.pixel(i,0,1)
    oled.show
    sleep(0.002)

for r in range(15):
    draw_circle(64, 32 , r*2)
    sleep(0.02)






sleep(2)
oled.fill(0)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(False)
sta_if.active(True)
sta_if.connect(credentials['ssid'],credentials['ssid_password'])

if not sta_if.isconnected():
    oled.text('CONNECTING TO  ',0,0)
    oled.text('WIFI',40,10)
    oled.text('PLEASE WAIT ',10,50)
    oled.show()
    
    progress = 0
    while not sta_if.isconnected():
        pass
        

        

       

oled.fill(0)
oled.show()



network_data = sta_if.ifconfig()
print(str(network_data))
oled.text('NETWORK DATA',10,0)
oled.show()
oled.text ('IP : ',30,10)
oled.show()
oled.text(network_data[0],0,20)
oled.show()
oled.text('MAC : ',30,30)
oled.show()
oled.text(network_data[1],0,40)
oled.show()

sleep(2)
oled.fill(0)
oled.show()

while (True):
    response = requests.get(url ="https://tukdata.herokuapp.com/data/real-time")
    data = json.loads(response.text)
    Temp = data['temperature']
    Humidity = data['humidity']
    AirQuality = data['airQuality']
    oled.fill(0)
    oled.show()
    oled.text("IOT DASHBOARD",10,0)
    oled.text("TEMPERATURE :",0,20)
    oled.text(str(Temp),100,20)
    oled.text("HUMIDITY :",0,30)
    oled.text(str(Humidity),100,30)
    oled.text("AIR QUALITY : ",0,40)
    oled.text(str(AirQuality),100,40)
    
    oled.show()
    
    













