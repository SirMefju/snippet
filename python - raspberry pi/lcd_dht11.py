import sys
import I2C_LCD_driver
import Adafruit_DHT
import time

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd.clear()
mylcd.lcd.display_string('ok',1)
mylcd.lcd.display_string('DHT11',2,1)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        
        if(temperature != None and humidity != None):
            mylcd.lcd_clear()
            mylcd.lcd.display_string('Temp:{0:0.1f} C '.format(temperature),1,2)
            mylcd.lcd.display_string('Humidity:{0:0.1f} %'.format(humidity),2,1)
        time.sleep(1)
except KeyboardInterrupt:
    mylcd.lcd.clear()
    mylcd.lcd.display_string('Thanks',1,5)
    mylcd.lcd.display_string('For All',2,2)
    time.sleep(5)
    mylcd.lcd_clear()

