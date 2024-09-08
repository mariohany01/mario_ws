#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include <iostream>
#include <cmath>

ros::Publisher velocity_publisher;
turtlesim::Pose turtlesim_pose;

double getDistance(double x1, double y1, double x2, double y2) {
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
}

void moveGoal(turtlesim::Pose goal_pose, double distance_tolerance) {
    geometry_msgs::Twist vel_msg;
    ros::Rate loop_rate(100);
    double E = 0.0;  // Integral error initialization

    do {
        // Proportional Controller
        double Kp = 1.0;        //liner velocity gain
        double Ki = 0.02;       //angular velocity gain

        double e = getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y);
        E += e;  // Integral term

        // Linear velocity in the x-axis
        vel_msg.linear.x = Kp * e;
        vel_msg.linear.y = 0;
        vel_msg.linear.z = 0;

        // Angular velocity in the z-axis
        vel_msg.angular.x = 0;
        vel_msg.angular.y = 0;
        vel_msg.angular.z = 4 * (atan2(goal_pose.y - turtlesim_pose.y, goal_pose.x - turtlesim_pose.x) - turtlesim_pose.theta);

        velocity_publisher.publish(vel_msg);

        ros::spinOnce();
        loop_rate.sleep();

    } while (getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_pose.x, goal_pose.y) > distance_tolerance);

    // Stop the turtle after reaching the goal
    vel_msg.linear.x = 0;
    vel_msg.angular.z = 0;
    velocity_publisher.publish(vel_msg);

    std::cout << "Goal Reached!" << std::endl;
}

void poseCallback(const turtlesim::Pose::ConstPtr& pose_message) {
    turtlesim_pose.x = pose_message->x;
    turtlesim_pose.y = pose_message->y;
    turtlesim_pose.theta = pose_message->theta;
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "go_to_goal");
    ros::NodeHandle n;

    velocity_publisher = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
    ros::Subscriber pose_subscriber = n.subscribe("/turtle1/pose", 10, poseCallback);

    ROS_INFO("\n\n\n******START TESTING************\n");

    turtlesim::Pose pose;
    pose.x = 1;
    pose.y = 1;
    pose.theta = 0;

    moveGoal(pose, 0.01);

    return 0;
}
