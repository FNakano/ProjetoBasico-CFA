# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
# import startsystem # when script is started here, could not interrupt its execution
# see warning about placing user code in boot.py
# in https://docs.micropython.org/en/latest/reference/reset_boot.html#id4
# 