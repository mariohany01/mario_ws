#!/usr/bin/env python3
import rospy
from msg_custom.msg import custommsg

def custommsg_callback(custom_msg_message):
    rospy.loginfo("new data received: (%d, %s, %.2f ,%.2f)", 
        custom_msg_message.id,custom_msg_message.name,
        custom_msg_message.temperature,custom_msg_message.humidity)
    
rospy.init_node('custom_msg_subscriber_node', anonymous=True)

rospy.Subscriber("custom_msg_topic_py", custommsg, custommsg_callback)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()