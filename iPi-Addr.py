# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import shlex
import subprocess
import time

# How to wire
# https://cloud.githubusercontent.com/assets/7507701/23578924/e4e06080-0124-11e7-932e-c00e3bdaf5b1.png

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

def execute():
  objProc = subprocess.Popen(shlex.split("sudo python ./lib/i2c_lib.py"))
  objProc = subprocess.Popen(shlex.split("sudo python ./lib/lcddriver.py"))
  objProc = subprocess.Popen(shlex.split("sudo python ./lib/lcd.py"))

try:
  GPIO.wait_for_edge(25, GPIO.FALLING)
except:
  print "Error!"
finally:
  GPIO.cleanup()

execute()
