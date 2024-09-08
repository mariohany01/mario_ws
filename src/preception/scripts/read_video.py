#!/usr/bin/env python3

import cv2

#####################################################################################
#
#   THIS CODE USED PREVIREW VIDEO OR A CAMERA
#
#####################################################################################



# Connect 3al camera
video_capture = cv2.VideoCapture(0)   

#video_name=input("Enter Video Name :  ")
#video_path ="/home/mario/mario_ws/src/preception/video/"+video_name+".mp4"
#video_capture = cv2.VideoCapture(video_path)

while(True):  #while to read frames comming from the video stream 
	ret, frame = video_capture.read()	#return 1 image from the video string and return them one by one 
	
	#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)		#convert video to greyscale
	frame = cv2.resize(frame, (0,0), fx=((2*4)/3),fy=2)				#resize the frame size
	#cv2.line(frame,(0,0),(511,511),(255,0,0),5)			#draw aline on video
	cv2.imshow("Frame",frame)								#show the frame
	if cv2.waitKey(1) & 0xFF == ord('q'):					#wait for pressing q on keybard to stop
		break

video_capture.release()
cv2.destroyAllWindows()