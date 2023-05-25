#!/usr/bin/env python

from turtle import distance
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x=0
y=0
yaw=0

def poseCallback(pose_message):
    global x
    global y, yaw
    x= pose_message.x
    y= pose_message.y
    yaw = pose_message.theta

    #print "pose callback"
    #print ('x = {}'.format(pose_message.x)) #new in python 3
    #print ('y = %f' %pose_message.y) #used in python 2
    #print ('yaw = {}'.format(pose_message.theta)) #new in python 3


def move(velocity_publisher, speed, distance, is_forward):
        #declare a Twist message to send velocity commands
        velocity_message = Twist()
        #get current location
        global x, y
        x0=x #save the initial location x-coordinate
        y0=y #save the initial location y-coordinate

        if (is_forward):
            velocity_message. linear.x =abs (speed)
        else:
            velocity_message. linear.x =-abs (speed)        
        
        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
        #cmd_vel_topic='/turtle1/cmd_vel'
        #velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        while True :
                rospy.loginfo("Turtlesim moves forwards")
                velocity_publisher.publish(velocity_message)

                loop_rate.sleep()
                
                #rospy.Duration(1.0)
                
                distance_moved = abs(math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
                print  (distance_moved)     
                print (x)         
                if  (distance_moved>distance):
                    rospy.loginfo("reached")
                    break
        
        #finally, stop the robot when the distance is moved
        velocity_message.linear.x =0
        velocity_publisher.publish(velocity_message)
    


if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        #declare velocity publisher
        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback) 
        time.sleep(2)

        #elrakam ele fel awel da houa el speed in meter per second
        #elrakam el tany da el masafa elle hatmsheha
        move(velocity_publisher, 1.0 , 4.0 , False)
        
        #move(1.0, 2.0, False)
        #rotate(30, 90, True)
        #go_to_goal(1.0, 1.0)
        #setDesiredOrientation(math.radians(90))
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")