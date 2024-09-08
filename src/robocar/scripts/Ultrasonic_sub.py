#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range

def ultrasonic_callback(msg):
     print("Range:", msg.range)

def ultrasonic_subscriber():
    sub = rospy.Subscriber("/ultrasound", Range, ultrasonic_callback)
    rospy.spin()


if __name__ == "__main__":
    rospy.init_node("ultrasonic_subscriber")
    ultrasonic_subscriber()
