#include <ros/ros.h>
#include "msg_custom/Iotsensor.h"

void iot_sensor_callback(const msg_custom::Iotsensor::ConstPtr& iot_sensor_message)
{
  ROS_INFO("new IoT data received: (%d, %s, %.2f, %.2f)",
           iot_sensor_message->id, 
           iot_sensor_message->name.c_str(),
           iot_sensor_message->temperature, 
           iot_sensor_message->humidity);
}

int main(int argc, char** argv)
{
  // Initialize the ROS node
  ros::init(argc, argv, "iot_sensor_subscriber_node");
  ros::NodeHandle nh;

  // Create a subscriber for the iot_sensor_topic
  ros::Subscriber sub = nh.subscribe("iot_sensor_topic", 10, iot_sensor_callback);

  // Spin to receive messages
  ros::spin();

  return 0;
}




