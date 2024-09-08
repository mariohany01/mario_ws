cmake_minimum_required(VERSION 3.0.2)
project(preception)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

# Find catkin and system dependencies
find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

find_package(OpenCV REQUIRED)


# Declare catkin package
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES preception
  CATKIN_DEPENDS cv_bridge image_transport roscpp rospy sensor_msgs std_msgs
  DEPENDS system_lib
)

# Include directories
include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)



## Add folders to be run by python nosetests
# catkin_add_nosetests(test)


find_package(OpenCV)

# Executable for reading video
add_executable(read_video_cpp src/read_video.cpp)
target_link_libraries(read_video_cpp ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})

# Executable for opening and copying an image
add_executable(open_copy_cpp src/open_copy.cpp)
target_link_libraries(open_copy_cpp ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})

# Executable for image publisher/subscriber
add_executable(image_pub_sub_cpp src/image_pub_sub.cpp)
target_link_libraries(image_pub_sub_cpp ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})



# Ensure the package is installed properly
install(TARGETS read_video_cpp open_copy_cpp image_pub_sub_cpp
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Install header files
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
)







