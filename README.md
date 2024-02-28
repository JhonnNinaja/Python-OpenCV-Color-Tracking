
# Python OpenCV Color Tracking

## Overview

This repository contains Python scripts using OpenCV for color tracking and object centroid detection. The scripts utilize techniques like color masking, contour finding, and moment calculations to identify and track colored objects in video.

## Scripts

- `robot_centroid_jh.py` - Tracks red and green objects and sends directional commands over serial to control a robot.

- `robot_centroid_jh_V2.py` - Improved version of robot control script with better object tracking.

- `secont_test.py` - Detects red, yellow, and blue objects in segmented areas of video frame. Prints object positions. 

- `trackbar.py` - Demo of OpenCV trackbar controls to dynamically configure HSV color masking.

- `video_capture.py` - Captures video from camera or stream and converts to grayscale.

## Usage

The scripts require OpenCV Python bindings. Use pip to install `opencv-python`. Some scripts utilize serial communication and may require PySerial.

Run the individual scripts to see color tracking and object detection on sample videos or camera/stream input. The robot control scripts are designed to connect to an Arduino or other microcontroller over serial.

Adjust color masking and other parameters in the code to customize for different lighting conditions and objects.

## Key Code Samples

Color masking to isolate colors:

```python
# Isolate red objects
red = cv.inRange(frame_HSV, (0, 162, 232), (7, 230, 255)) 

# Isolate green objects
green = cv.inRange(frame_HSV, (51, 89, 129), (78, 89, 178))
```

Find object contours and centroids:

```python 
# Find contours and get moments for red
M = cv.moments(red)

# Get centroid coordinates
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
```

Draw centroids and text on frame:

```python
# Draw circle and text at centroid
cv.circle(frame, (cX, cY), 5, (255, 255, 255), -1) 
cv.putText(frame, "Red centroid", (cX - 25, cY - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
```

Trackbar controls for HSV masking:

```python
# Create trackbars for HSV boundaries
cv.createTrackbar("Low H", "Controls", 0, 179, on_low_h_change)  
cv.createTrackbar("High H", "Controls", 179, 179, on_high_h_change)

# Get trackbar positions    
low_h = cv.getTrackbarPos("Low H", "Controls")
high_h = cv.getTrackbarPos("High H", "Controls")
```
