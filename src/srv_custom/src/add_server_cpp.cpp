#include "ros/ros.h"
#include "srv_custom/AddTwoInts.h"

bool add(srv_custom::AddTwoInts::Request  &req,
         srv_custom::AddTwoInts::Response &res)
{
  res.sum = req.a + req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_server");
  ros::NodeHandle n;
  //hena ana ba3mel el services w bakhaleha tedene el call back fu ele esmaha add
  ros::ServiceServer service = n.advertiseService("add_two_ints", add);
  //ROS_INFO di zai printf keda bas lel ros 3ashan tekhetb 3ala el terminal
  ROS_INFO("Ready to add two ints.");
  ros::spin();

  return 0;
}

