from http.client import responses
import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket
import json


# host = socket.gethostname()
host = "192.168.8.99"
# WIT-yolov5 = 10002
# Face-recog = 10006
# Person-tracker = 11000
# Object-tracker = 10008
port = 10008

c = CustomSocket(host,port)
c.clientConnect()

cap = cv2.VideoCapture(2) # camera id
if not cap.isOpened():
    print("camera not found: try another camera id")

cap.set(4,720)
cap.set(3,1280)

while cap.isOpened():
	
    ret, frame = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue
    
    cv2.imshow('test', frame)

    print("Send")

    # WIT yolov5 person-tracker, object-tracker
    msg = c.req(frame)
    print(msg)


    # Face-recog
    # image = cv2.imread("elon.jpeg")
    # c.register(image, "elon") #hide this
    # c.detect(frame)

    if cv2.waitKey(1) == ord("q"):
        cap.release()

cv2.destroyAllWindows()

