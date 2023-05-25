cmake_minimum_required(VERSION 3.0.2)
project(srv_custom)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

## Generate services in the 'srv' folder
add_service_files(
  FILES 
  AddTwoInts.srv
  )

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ros_essentials_cpp
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(add_two_ints_server src/add_server_cpp.cpp)
target_link_libraries (add_two_ints_server ${catkin_LIBRARIES})
add_dependencies(add_two_ints_server srv_custom_gencpp)

add_executable(add_two_ints_client src/add_client_cpp.cpp)
target_link_libraries (add_two_ints_client ${catkin_LIBRARIES})
add_dependencies(add_two_ints_client srv_custom_gencpp)