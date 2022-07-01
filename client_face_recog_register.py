from http.client import responses
import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket
import json


host = socket.gethostname()
# WIT-yolov5 = 10002
# Face-recog = 10006
# Person-tracker = 11000
# Object-tracker = 10008
port = 11000

c = CustomSocket(host,port)
c.clientConnect()

image = cv2.imread("elon.jpeg")
status = c.register(image, "elon") #hide this
print(status)


