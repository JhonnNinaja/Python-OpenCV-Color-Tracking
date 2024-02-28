import numpy as np
import cv2 as cv
#cap = cv.VideoCapture(0)
cap = cv.VideoCapture('gst-launch-1.0 tcpclientsrc host=192.168.43.250 port=5002 ! jpegdec ! videoconvert ! appsink',cv.CAP_GSTREAMER)
#cap = cv.VideoCapture('0')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    cv.imshow('original frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
