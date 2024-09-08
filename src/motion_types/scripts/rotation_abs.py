#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time 

yaw = 0

def setDesiredOrientation(publisher ,speed_degree , desired_angle_degree):
    relative_angle_radians = math.radians(desired_angle_degree) - yaw
    clockwise = 0
    if relative_angle_radians < 0 :
        clockwise = 1
    else:
        clockwise = 0

    print ("relative angle radians : " , math.degrees(relative_angle_radians))
    print ("desired angle degree : ", desired_angle_degree)
    rotate (publisher , speed_degree,math.degrees(abs(relative_angle_radians)),clockwise)

def rotate (velocity_publisher , angular_speed_degree , relative_angle_degree , clockwise) :
    velocity_message = Twist()

    angular_speed=math.radians(abs(angular_speed_degree))

    if(clockwise):
        velocity_message.angular.z= -abs(angular_speed)
    else:
        velocity_message.angular.z= abs(angular_speed)

    loop_rate=rospy.Rate(10)
    t0 = rospy.Time.now().to_sec()

    while True : 
        rospy.loginfo("Robot Rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0) * angular_speed_degree
        loop_rate.sleep()

        if (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break
    velocity_message.angular.z=0
    velocity_publisher.publish(velocity_message)

def poseCallback(pose_message):
    global x, y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta


if __name__ == '__main__':        
    rospy.init_node('Robot_rotate_abs', anonymous=True)

    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    position_topic = "/turtle1/pose"
    pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
    time.sleep(2)

    setDesiredOrientation(velocity_publisher, 10.0, 90.0 )