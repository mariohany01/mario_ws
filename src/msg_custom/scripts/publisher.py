#!/usr/bin/env python3
# license removed for brevity
import rospy
from msg_custom.msg import custommsg
import random

#create a new publisher. we specify the topic name, then type of message then the queue size
pub = rospy.Publisher('custom_msg_topic_py', custommsg, queue_size=10)

#we need to initialize the node
rospy.init_node('custom_msg_publisher_node', anonymous=True)

#set the loop rate
rate = rospy.Rate(1) # 1hz
#keep publishing until a Ctrl-C is pressed
i = 0
while not rospy.is_shutdown():
    custom_msg = custommsg()
    custom_msg.id = 1
    custom_msg.name="data_01"
    custom_msg.temperature = 24.33 + (random.random()*2)
    custom_msg.humidity = 33.41+ (random.random()*2)
    rospy.loginfo("I publish:")
    rospy.loginfo(custom_msg)
    pub.publish(custom_msg)
    rate.sleep()
    i=i+1