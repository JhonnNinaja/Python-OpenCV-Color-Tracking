
from __future__ import print_function
import cv2 as cv
import argparse
import serial
from time import sleep, time
import time 
ser = serial.Serial('/dev/ttyACM0', 115200)
ser.timeout=0.3
max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
window_mask = 'Color Mask'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'
def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)
def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)
def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)
def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)
parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(0)

height = cap.get(4)

#cap = cv.VideoCapture('Red_Rabbit_Green_Gorilla.mp4')
cv.namedWindow(window_capture_name)

cont_red= False #contador para reconocer color
cont_green = False
while True:
    
    ret, frame = cap.read()
    #frame = cv.resize(frame,(800,800))
    frame = cv.blur(frame,(15,15))
    result = frame.copy()

    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    frame_threshold_1 = cv.inRange(frame_HSV, (32,88,97), (70,165,255))
    red = cv.inRange(frame_HSV,(0,162,232),(7,230,255))
    green = cv.inRange(frame_HSV,(51,89,129),(78,89,178))
    flag_red = 0
    flag_green = 0
    try:
        # calculate moments of binary image
        M = cv.moments(frame_threshold_1)
    
        # calculate x,y coordinate of center
        cX_r = int(M["m10"] / M["m00"])
        cY_r = int(M["m01"] / M["m00"])
    
        # put text and highlight the center
        cv.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
        cv.putText(frame, "centroid 1", (cX - 25, cY - 25),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        flag_red = 1
    except:
        pass
    try:
        # calculate moments of binary image
        M = cv.moments(green)
    
        # calculate x,y coordinate of center
        cX_g = int(M["m10"] / M["m00"])
        cY_g = int(M["m01"] / M["m00"])
    
        # put text and highlight the center
        cv.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
        cv.putText(frame, "centroid 1", (cX - 25, cY - 25),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        flag_green = 1
    except:
        pass

    #modificar
    
    if flag_red==0 or flag_green == 0:
        ser.write('RIGTH'.encode())
        time.sleep(500)
        ser.write('STOP'.encode())
        time.sleep(500)
    

        



    if(flag_red==1):
	
        cv.putText(frame, "DETECTION_RED", (10,10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        if cX_r < height/2*(1-45/100):
            ser.write('RIGTH'.encode())
        elif cX_r > height/2*(1+45/100):
            ser.write('LEFT'.encode())
        else:
            ser.write('UP'.encode())
    elif(flag_green == 1):
        cv.putText(frame, "DETECTION_GREEN", (10,10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        if cX_g < height/2*(1-45/100):
            ser.write('RIGTH'.encode())
        elif cX_g > height/2*(1+45/100):
            ser.write('LEFT'.encode())
        else:
            ser.write('UP'.encode())
    else:
        cv.putText(frame, "NONE", (10,30),cv.FONT_HERSHEY_SIMPLEX, 0.5, (57, 143, 0), 2)
        ser.write('STOP'.encode())
    
    mask = frame_threshold_1
    result = cv.bitwise_and(result,result,mask=mask)
    cv.imshow(window_capture_name, frame)
    key = cv.waitKey(5)
    if key == ord('q') or key == 27:
        break
ser.close()
