#!/usr/bin/env python3

#####################################################################################
#
#   THIS CODE USED TO DRAW LINES RECTANGLES ... ETC
#
#####################################################################################

import numpy as np
import cv2

image = np.zeros((512,512,3), np.uint8)

###cv2.circle(image, (image.shape[0]/2, image.shape[1]/2),63, (255,255,255), 5)   ###### WRONGGGG
cv2.line(image,(0,0),(511,511),(255,255,255),5)  #(image , starting point , ending point , color , thickness)

cv2.rectangle(image,(0,0),(511,511),(0,255,0),3)   #(image , starting point , ending point , color , thickness)
cv2.ellipse(image,(256,256),(100,50),0,0,270,(255,186,129),-1) #(image , center coordinates , axis length ,angle of rotation, starting angle , ending angle , color , thickness -1  means filled )



#draw shape
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'OpenCV'      ,(10,500), font, 4,(255,255,255),2,cv2.LINE_AA) # (image , displated text , start of bottom corner , font type , scale , color  , smoother)
cv2.putText(image,'OpenCV'      ,(10,300), font, 4,(255,255,255),2)


cv2.imshow("Image Panel",image)

cv2.waitKey(0)
cv2.destroyAllWindows()