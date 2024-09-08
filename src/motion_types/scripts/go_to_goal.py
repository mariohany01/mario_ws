#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time 

def go_to_goal (velocity_publisher , x_goal , y_goal):
    global x 
    global y , yaw

    velocity_message = Twist()

    while(True):
        k_liner = 0.5                   #Proportional controller 
        distance = abs(math.sqrt(((x - x_goal)**2) + ((y - y_goal)**2)))

        liner_speed= distance * k_liner  #hena 3asahn el speed tebaa proportional lel distance  , this part is made for smoothnesss
    

        k_angular= 4.0                  #proportional 

        desired_angle_goal=math.atan2(y_goal-y , x_goal- x)
       
       # print ("desired_angle_goal = " , desired_angle_goal)
        #print ('YAW = ', yaw)

        angular_speed = (desired_angle_goal-yaw)* k_angular 
        print ('el sor3a ele haylef beha hawalein nafso = ', angular_speed)

        velocity_message.linear.x = liner_speed
        velocity_message.angular.z=angular_speed

        velocity_publisher.publish(velocity_message)
        print ('x=',x,'y=',y,'distance to goal= ', distance )

        if (distance < 0.01):
            break


def poseCallback(pose_message):
    global x, y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

if __name__ == '__main__':        
    rospy.init_node('go_to_goal', anonymous=True)

    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    position_topic = "/turtle1/pose"
    pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
    time.sleep(2)

    go_to_goal(velocity_publisher, 5.5 ,8)