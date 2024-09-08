#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def left_ticks_callback(msg):
  print("Left ticks:", msg.data)


def left_ticks_subscriber():
    sub = rospy.Subscriber("/left_ticks", Int32, left_ticks_callback)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node("left_ticks_subscriber")
    left_ticks_subscriber()
