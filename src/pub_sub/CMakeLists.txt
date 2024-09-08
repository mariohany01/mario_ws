cmake_minimum_required(VERSION 3.0.2)
project(pub_sub)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}  
)

#Pub
add_executable(publisher_node_cpp src/publisher.cpp)
target_link_libraries (publisher_node_cpp ${catkin_LIBRARIES})

#Subs
add_executable(subscriber_node_cpp src/subscriber.cpp)
target_link_libraries (subscriber_node_cpp ${catkin_LIBRARIES})
