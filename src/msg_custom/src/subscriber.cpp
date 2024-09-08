#include <ros/ros.h>
#include "msg_custom/custommsg.h"

void custommsg_callback(const msg_custom::custommsg::ConstPtr& custommsg_message)
{
  ROS_INFO("new custommsg received: (%d, %s, %.2f, %.2f)",
           custommsg_message->id, 
           custommsg_message->name.c_str(),
           custommsg_message->temperature, 
           custommsg_message->humidity);
}

int main(int argc, char** argv)
{
  // Initialize the ROS node
  ros::init(argc, argv, "custom_msg_subscriber_node");
  ros::NodeHandle nh;

  // Create a subscriber for the custommsg_topic
  ros::Subscriber sub = nh.subscribe("custom_msg_topic_cpp", 10, custommsg_callback);

  // Spin to receive messages
  ros::spin();

  return 0;
}



