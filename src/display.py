# específico para display 72x40 no ESP32 supermini com display embutido
import config
from machine import Pin, I2C
i2c=I2C(0, scl=Pin(6), sda=Pin(5)) # ok, neste ESP os pinos são 5 e 6

print('Scan i2c bus...')
devices = i2c.scan()  # ok, ele acha o display em 0x3c

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))

import ssd1306
config.disp=ssd1306.SSD1306_I2C(128, 64, i2c) # https://goldenmorninglcd.com/pt/exibi%C3%A7%C3%A3o-oled/0.42-polegadas-oled-72x40-ssd1306-branco-gme7240-01/

# mess is a string
def message(mess) :
  config.messages=mess
  try:
    config.disp.fill(0)
    lin=0
    lenM=len(mess)
    for i in range(0,lenM,9) :
      config.disp.text(mess[i:i+9], 27, 24+lin,1)
      lin=(lin+8)%40
    config.disp.show()
  except AttributeError as e:
    print(f"{e} ocurred when trying to message display. Probably display is not attached to devboard.")

config.disp.text("DDDDDDDDDD", 27, 24, 1)
config.disp.text("ABCDEFGHIJ", 27, 32, 1)
config.disp.text("DDDDDDDDDD", 27, 40, 1)
config.disp.text("MMMMMMMMMM", 27, 48, 1)
config.disp.text("DDDDDDDDDD", 27, 56, 1)
config.disp.show()
