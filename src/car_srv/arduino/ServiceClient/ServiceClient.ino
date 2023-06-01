/*
 rosserial Service Client
 */

// Import the necessary libraries
#include <ros.h>
#include <car_srv/Car.h>
#include <std_msgs/String.h>



// Create a ROS node
ros::NodeHandle  nh;

// Create a client object for the `Car` service
using car_srv::Car;
ros::ServiceClient<Car::Request, Car::Response> client("Car_srv");

// Create a publisher for the `car_data` topic
std_msgs::String str_msg;
ros::Publisher car_data("car_data", &str_msg);

// Create a string containing the message to send to the server
char hello[13] = "hello world!";

// Initialize the ROS node
void setup()
{
  // Initialize the ROS node
  nh.initNode();

  // Create a client object for the `Car` service
  nh.serviceClient(client);

  // Create a publisher for the `car_data` topic
  nh.advertise(car_data);

  // Wait until the ROS node is connected to the master
  while(!nh.connected()) nh.spinOnce();

  // Log a message to the console
  nh.loginfo("Car Ready");
}

// Loop forever
void loop()
{
  // Create a `Car::Request` message
  Car::Request req;

  // Set the input of the request message
  req.input = hello;

  // Call the `Car` service
  client.call(req, res);

  // Get the output of the response message
  str_msg.data = res.output;

  // Publish the `car_data` message
  car_data.publish( &str_msg );

  // Spin the ROS event loop
  nh.spinOnce();

  // Delay for 100 milliseconds
  delay(100);
}
