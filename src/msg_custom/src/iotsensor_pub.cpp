#include <ros/ros.h>
#include <cstdlib>
#include <ctime>
#include "msg_custom/Iotsensor.h"

int main(int argc, char **argv)
{
  // Initialize the ROS node
  ros::init(argc, argv, "iot_sensor_publisher_node");
  ros::NodeHandle nh;

  // Create a publisher for the iot_sensor_topic
  ros::Publisher pub = nh.advertise<msg_custom::Iotsensor>("iot_sensor_topic", 10);

  // Set the loop rate to 1 Hz
  ros::Rate loop_rate(1);

  // Seed the random number generator
  std::srand(std::time(nullptr));

  // Publish messages until the node is shut down
  int i = 0;
  while (ros::ok())
  {
    // Create a new Iotsensor message
    msg_custom::Iotsensor iot_sensor;
    iot_sensor.id = 1;
    iot_sensor.name = "iot_parking_01";
    iot_sensor.temperature = 24.33 + (std::rand() % 100) / 50.0;
    iot_sensor.humidity = 33.41 + (std::rand() % 100) / 50.0;

    // Log the message to the console
    ROS_INFO_STREAM("I publish: " << iot_sensor);

    // Publish the message
    pub.publish(iot_sensor);

    // Sleep to maintain the loop rate
    loop_rate.sleep();

    i++;
  }

  return 0;
}