import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import math
from termCol import *
import VWUtils
import VisionEngine

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#######################################
# Display Initialization. DO NOT ALTER!
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
width = disp.width
height = disp.height
padding = -2
top = padding
bottom = height=padding
x = 0
font = ImageFont.load_default()
#
#######################################

##################################################
# Button input board initialization. DO NOT ALTER!
GPIO.setmode(GPIO.BCM)
leftb = 17
homeb = 27
rightb = 22
screenb = 4
GPIO.setup(leftb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(homeb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(screenb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
##################################################

def weather(debugStatus):
    print("Starting live weather stream...")
    TempDisp = 1
    HumidDisp = 0
    while GPIO.input(homeb) == True:
        font = ImageFont.load_default()        
        url = "http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=6d711345f94972e7ac62fc8f43cc648c&lat=24.19&lon=55.76"
        fetched_data = requests.get(url)
        fetched_data_json = fetched_data.json()
        main_data = fetched_data_json.get('main')
        current_tempK = main_data.get('temp')
        current_humidity = main_data.get('humidity')
        current_temp = round(current_tempK - 273, 1)
        CurrTemp = int(current_temp)
        FinalTemp = "Temperature: " + (str(current_temp))
        FinalHumid = "Humidity: " + (str(current_humidity))

        VisionEngine.disptext(FinalTemp, FinalHumid, " ", " ",0,0,0,0, 0, 12,24,36, debugStatus, '0')
