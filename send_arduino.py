import numpy as np
import serial
import time
import requests
import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWebEngineWidgets import *
x = requests.get('https://possible-wheat-booth.glitch.me/',allow_redirects=True)

arduino = serial.Serial(port='COM10', baudrate=9600, timeout=0.1)
file_path = r'C:\Users\sudha\OneDrive\Desktop\main_code\yolov5\det_res.txt';
print(x.status_code)
print(x.url)
print(x.history)
app=QtWidgets.QApplication(sys.argv)

app.exec_()
while True:
    f1 = open(file_path,'r')
    Txt_Data = f1.read()
    if "disease" in Txt_Data:
        #arduino.write(bytes(1, 'utf-8'))
        arduino.write(b'1')
        print('Diseaase detected Pump On')
     
       
        
    else:
        #arduino.write(bytes(0, 'utf-8'))
        arduino.write(b'0')
        print('Pump Off, Healthy plant')
    arduino.flushInput()
    arduino.flushOutput()
    time.sleep(0.1)
