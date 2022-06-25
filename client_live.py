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
port = 11000

c = CustomSocket(host,port)
c.clientConnect()

cap = cv2.VideoCapture(2)
cap.set(4,720)
cap.set(3,1280)

while cap.isOpened():
	
    ret, frame = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue
    
    cv2.imshow('test', frame)

    print("Send")

    # WIT yolov5 and Person-tracker
    msg = c.req(frame)
    print(msg)


    # Face-recog
    # c.register(image,test_name) #hide this
    # c.detect(frame)

    if cv2.waitKey(1) == ord("q"):
        cap.release()

cv2.destroyAllWindows()

