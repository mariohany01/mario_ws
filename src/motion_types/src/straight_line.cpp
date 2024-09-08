#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include <iostream>
#include <cmath>

ros::Publisher velocity_publisher;
turtlesim::Pose turtlesim_pose;

void move(double speed, double distance, bool isForward) {
    geometry_msgs::Twist vel_msg;

    // Set linear velocity
    if (isForward)
        vel_msg.linear.x = abs(speed);
    else
        vel_msg.linear.x = -abs(speed);

    // No movement in y, z directions or angular velocity
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;
    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;
    vel_msg.angular.z = 0;

    double t0 = ros::Time::now().toSec();
    double current_distance = 0.0;
    ros::Rate loop_rate(10);  // Control the loop speed

    do {
        velocity_publisher.publish(vel_msg);   // send x = speed 

        double t1 = ros::Time::now().toSec();

        current_distance = speed * (t1 - t0);  // Distance = velocity * time
        ros::spinOnce();
        loop_rate.sleep();
    } while (current_distance < distance);

    // Stop the turtle after reaching the desired distance
    vel_msg.linear.x = 0;
    velocity_publisher.publish(vel_msg);
}

void poseCallback(const turtlesim::Pose::ConstPtr &pose_message) {
    turtlesim_pose.x = pose_message->x;
    turtlesim_pose.y = pose_message->y;
    turtlesim_pose.theta = pose_message->theta;
}



int main(int argc, char **argv) {
    // Initiate new ROS node named "move_straight_line"
    ros::init(argc, argv, "move_straight_line");
    ros::NodeHandle n;

    //Initialize variables
    double speed, distance;
    bool isForward;

    // Define the publisher and subscriber
    velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
    ros::Subscriber pose_subscriber = n.subscribe("/turtle1/pose", 10, poseCallback);

    // Test the code
    ROS_INFO("\n\n\n******START TESTING************\n");
    std::cout << "Enter speed: ";
    std::cin >> speed;
    std::cout << "Enter distance: ";
    std::cin >> distance;
    std::cout << "Forward (1 for yes, 0 for no)?: ";
    std::cin >> isForward;

    move(speed, distance, isForward);

    return 0;
}
