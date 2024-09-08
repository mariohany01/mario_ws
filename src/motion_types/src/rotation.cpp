#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include <iostream>
#include <cmath>

ros::Publisher velocity_publisher;
turtlesim::Pose turtlesim_pose;



void move(double angular_speed, double relative_angle, bool clockwise) {
    geometry_msgs::Twist vel_msg;

    // Set linear velocity
    if (clockwise)
        vel_msg.angular.z = abs(angular_speed);
    else
        vel_msg.angular.z = -abs(angular_speed);

    // No movement in y, z directions or angular velocity
    vel_msg.linear.x = 0;
    vel_msg.linear.y = 0;
    vel_msg.linear.z = 0;
    vel_msg.angular.x = 0;
    vel_msg.angular.y = 0;

    double current_angle = 0.0;
    double t0 = ros::Time::now().toSec();

    ros::Rate loop_rate(10);  // Control the loop angular_speed

    do {
        velocity_publisher.publish(vel_msg);   // send x = angular_speed 

        double t1 = ros::Time::now().toSec();

        current_angle = angular_speed * (t1 - t0);  // relative_angle = velocity * time
        ros::spinOnce();
        loop_rate.sleep();
    } while (current_angle < relative_angle);

    // Stop the turtle after reaching the desired relative_angle
    vel_msg.angular.z = 0;
    velocity_publisher.publish(vel_msg);
}

void poseCallback(const turtlesim::Pose::ConstPtr &pose_message) {
    turtlesim_pose.x = pose_message->x;
    turtlesim_pose.y = pose_message->y;
    turtlesim_pose.theta = pose_message->theta;
}



int main(int argc, char **argv) {
    // Initiate new ROS node named "move_straight_line"
    ros::init(argc, argv, "move_rotation");
    ros::NodeHandle n;

    //Initialize variables
    double angular_speed, relative_angle;
    bool clockwise;

    // Define the publisher and subscriber
    velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
    ros::Subscriber pose_subscriber = n.subscribe("/turtle1/pose", 10, poseCallback);

    // Test the code
    ROS_INFO("\n\n\n******START TESTING************\n");
    std::cout << "Enter angular_speed: ";
    std::cin >> angular_speed;
    std::cout << "Enter relative_angle: ";
    std::cin >> relative_angle;
    std::cout << "Forward (1 for yes, 0 for no)?: ";
    std::cin >> clockwise;

    move(angular_speed, relative_angle, clockwise);

    return 0;
}
