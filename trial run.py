import numpy as np
import serial
import time
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWebEngineWidgets import *
import requests
import sys
arduino = serial.Serial(port='COM10', baudrate=9600, timeout=0.1)
file_path = r'C:\Users\sudha\OneDrive\Desktop\main_code\yolov5\det_res.txt';

app=QtWidgets.QApplication(sys.argv)
w=QWebEngineView()

while True:
    f1 = open(file_path,'r')
    Txt_Data = f1.read()
    if "disease" in Txt_Data:
        #arduino.write(bytes(1, 'utf-8'))
        arduino.write(b'1')
        print('Diseaase detected Pump On')
        w.load(QtCore.QUrl('file:///C:/Users/sudha/OneDrive/Desktop/brahadeesh/templatemo_478_accord/Untitled-1.html'))
        w.showMaximized()
        app.exec_()
        
    else:
        #arduino.write(bytes(0, 'utf-8'))
        arduino.write(b'0')
        print('Pump Off, Healthy plant')
    arduino.flushInput()
    arduino.flushOutput()
    time.sleep(0.1)
