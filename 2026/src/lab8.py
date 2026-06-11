import config
import network
import time
from machine import Pin

config.wifi_if=network.WLAN(network.STA_IF)
config.wifi_if.active(True)
config.wifi_if.config(hostname=config.myhostname)
config.wifi_if.connect(config.wifi_id, config.wifi_password)
tries=0
while not (config.wifi_if.isconnected()) and tries<20 :
    config.led.on() # indicate that this program is being executed
    print('.') # no wifi
    time.sleep(2) # wait for 2 seconds to wifi to connect
    tries=tries+1
if config.wifi_if.isconnected() :
    config.led.off() # connected
    print ("wifi is connected")
    print (config.wifi_if.ifconfig())
else :
    print ("wifi is not connected")
    print ("connection process is running on background it might succeed later.")
