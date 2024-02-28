from __future__ import print_function
from unittest import result
import cv2 as cv
import argparse

window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
window_mask = 'color_mask'

cap = cv.VideoCapture('second_test.mp4')

red_bool = False
blue_bool = False
yellow_bool = False

while True:

    ret, frame = cap.read()
    frame = cv.resize(frame,(300,300))
    result = frame.copy()
    frame = cv.blur(frame,(10,10))
    if frame is None:
        break

    #dibujando lineas
    cv.line(result,(100,0),(100,300),(255,0,0),4)
    cv.line(result,(200,0),(200,300),(255,0,0),4)


    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    red = cv.inRange(frame_HSV,(2,211,241),(11,255,255))
    yellow = cv.inRange(frame_HSV,(14,231,250),(34,255,255))
    blue = cv.inRange(frame_HSV,(92,175,218),(114,242,234))

    try:
        M = cv.moments(red)
        cX_r = int(M["m10"]/M["m00"])
        cY_r = int(M["m01"]/M['m00'])
 
        # put text and highlight the center
        #cv.circle(frame, (cX, cY), 5, (255,255,255), -1)
        #cv.putText(frame, "centroid", (cX - 25, cY - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
        red_bool = True
    except:
        red_bool = False


    
    try:
        M = cv.moments(yellow)
        cX_y = int(M["m10"]/M["m00"])
        cY_y = int(M["m01"]/M['m00'])
 
        # put text and highlight the center
        #cv.circle(frame, (cX, cY), 5, (255,255,255), -1)
        #cv.putText(frame, "centroid", (cX - 25, cY - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
        yellow_bool = True
    except:
        yellow_bool = False


    try:
        M = cv.moments(blue)
        cX_b = int(M["m10"]/M["m00"])
        cY_b = int(M["m01"]/M['m00'])
 
        # put text and highlight the center
        #cv.circle(frame, (cX, cY), 5, (255,255,255), -1)
        #cv.putText(frame, "centroid", (cX - 25, cY - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
        blue_bool = True
    except:
        blue_bool = False

    if(cX_r > 0 and cX_r <= 100 and red_bool):
        print("Red: left")
        cv.putText(result, "Red", (20,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif(cX_r > 100 and cX_r <= 200 and red_bool):
        print("Red: Middle")
        cv.putText(result, "Red", (120,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif(cX_r > 200 and cX_r <= 300 and red_bool):
        cv.putText(result, "Red", (220,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
        print("Red: right")
    else:
        print("")
    if(cX_y > 0 and cX_y <= 100 and yellow_bool):
        print("Yellow: left")
        cv.putText(result, "Yellow", (20,40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

    elif(cX_y > 100 and cX_y <= 200 and yellow_bool):
        print("Yellow: Middle")
        cv.putText(result, "Yellow", (120,40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif(cX_y > 200 and cX_y <= 300 and yellow_bool):
        print("Yellow: right")
        cv.putText(result, "Yellow", (220,40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    else:
        print("")

    if(cX_b > 0 and cX_b <= 100 and blue_bool):
        print("Blue: left")
        cv.putText(result, "Blue", (20,60), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif(cX_b > 100 and cX_b <= 200 and blue_bool):
        print("Blue: Middle")
        cv.putText(result, "Blue", (120,60), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif(cX_b > 200 and cX_b <= 300 and blue_bool):
        print("Blue: right")
        cv.putText(result, "Blue", (220,60), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    else:
        print("")
    print("------------------------------------")
    cv.imshow(window_detection_name, result)
    key = cv.waitKey(20)
    if key == ord('q') or key == 27:
        break