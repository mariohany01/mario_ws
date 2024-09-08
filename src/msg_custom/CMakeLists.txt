cmake_minimum_required(VERSION 3.0.2)
project(msg_custom)


find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
)



## Generate messages in the 'msg' folder
add_message_files(
  FILES
  custommsg.msg 
)


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES msg_custom
  CATKIN_DEPENDS  roscpp rospy std_msgs message_runtime
  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)



add_executable(custom_msg_publisher_node src/publisher.cpp)
target_link_libraries (custom_msg_publisher_node ${catkin_LIBRARIES})
add_dependencies(custom_msg_publisher_node msg_custom_gencpp)

add_executable(custom_msg_subscriber_node src/subscriber.cpp)
target_link_libraries (custom_msg_subscriber_node ${catkin_LIBRARIES})
add_dependencies(custom_msg_subscriber_node msg_custom_gencpp)