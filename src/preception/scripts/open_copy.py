#!/usr/bin/env python3

#####################################################################################
#
#   THIS CODE USED TO COPY IMAGE FROM SPECFIC DIRECTION TO ANOTHER ONE
#
#####################################################################################




#import numpy: the data structure that will handle an image
import numpy as np

#import openCV
import cv2

image_name = input("Enter Image Name :  ")
#image_name="tree"

image_path = "/home/mario/mario_ws/src/preception/images/"+image_name+".jpg"
copy_folder = "/home/mario/mario_ws/src/preception/images/copy/"


print ('read an image from file')

img = cv2.imread(image_path)

print ('create a window holder for the image')
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

print ('display the image')
cv2.imshow("Image", img)

print ('press a key inside the image to make a copy')
cv2.waitKey(0)

print ('image copied to folder images/copy/')
cv2.imwrite(copy_folder + image_name+"_copy.jpg", img)


