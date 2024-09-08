cmake_minimum_required(VERSION 3.0.2)
project(motion_types)

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

#Move Straight Line
add_executable(move_straight_line src/straight_line.cpp)
target_link_libraries (move_straight_line ${catkin_LIBRARIES})

#Move Rotation
add_executable(move_rotation src/rotation.cpp)
target_link_libraries (move_rotation ${catkin_LIBRARIES}) 

#GoalToGoal
add_executable(go_to_goal src/go_to_goal.cpp)
target_link_libraries (go_to_goal ${catkin_LIBRARIES}) 