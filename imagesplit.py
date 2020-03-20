import numpy as np
import cv2
from os import walk
import os, os.path




img=cv2.imread('1.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgTestingNumbers = img.copy()

img=cv2.GaussianBlur(img, (5,5), 0)
img = cv2.bitwise_not(img)
imgThreshCopy = img.copy()        # make a copy of the thresh image, this in necessary b/c findContours modifies the image

imgContours, contours, hierarchy = cv2.findContours(imgThreshCopy,             # input image, make sure to use a copy since the function will modify this image in the course of finding contours
                                                cv2.RETR_EXTERNAL,         # retrieve the outermost contours only
                                                cv2.CHAIN_APPROX_SIMPLE)   # compress horizontal, vertical, and diagonal segments and leave only their end points
hierarchy = hierarchy[0] # get the actual inner list of hierarchy descriptions
filecount = 0
# For each contour, find the bounding rectangle and draw it
for component in zip(contours, hierarchy):
    currentContour = component[0]
    currentHierarchy = component[1]
    x,y,w,h = cv2.boundingRect(currentContour)
    if currentHierarchy[2] < 0:
        # these are the innermost child components
        print('currentHierarchy[2]', currentHierarchy[2], x, y, w, h)
        if w > 15 and h > 20:
            
            cv2.imwrite("temp\\Image" + str(filecount) + str(x) + "-" + str(y) + "-" + str(w) + "-" + str(h) + ".jpg",imgTestingNumbers[y:y+h, x:x+w])
    elif currentHierarchy[3] < 0:
        # these are the outermost parent components
        print('currentHierarchy[3]', currentHierarchy[3])
        cv2.rectangle(imgTestingNumbers,(x,y),(x+w,y+h),(0,255,0),3)