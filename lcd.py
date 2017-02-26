# coding:utf-8

import lcddriver
import socket
from time import *

# Usage
# 1. Load i2c_lib.py
# 2. Load lcddriver.py
# 3. Load lcd.py

lcd = lcddriver.lcd()

addr = socket.gethostname()
ipaddr = socket.gethostbyname(socket.gethostname())

print(addr)
print(ipaddr)

lcd.lcd_display_string("NAME:" + addr, 1)
lcd.lcd_display_string("IP:"+ ipaddr, 2)

