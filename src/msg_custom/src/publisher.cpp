#include <ros/ros.h>
#include <cstdlib>
#include <ctime>
#include "msg_custom/custommsg.h"

int main(int argc, char **argv)
{
  // Initialize the ROS node
  ros::init(argc, argv, "custom_msg_publisher_node");
  ros::NodeHandle nh;

  // Create a publisher for the custom_msg_topic
  ros::Publisher pub = nh.advertise<msg_custom::custommsg>("custom_msg_topic_cpp", 10);

  // Set the loop rate to 1 Hz
  ros::Rate loop_rate(1);

  // Seed the random number generator
  std::srand(std::time(nullptr));

  // Publish messages until the node is shut down
  int i = 0;
  while (ros::ok())
  {
    // Create a new custommsg message
    msg_custom::custommsg custom_msg;
    custom_msg.id = 1;
    custom_msg.name = "iot_parking_01";
    custom_msg.temperature = 24.33 + (std::rand() % 100) / 50.0;
    custom_msg.humidity = 33.41 + (std::rand() % 100) / 50.0;

    // Log the message to the console
    ROS_INFO_STREAM("I publish: " << custom_msg);

    // Publish the message
    pub.publish(custom_msg);

    // Sleep to maintain the loop rate
    loop_rate.sleep();

    i++;
  }

  return 0;
}