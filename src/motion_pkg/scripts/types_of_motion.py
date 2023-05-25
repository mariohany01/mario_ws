#!/usr/bin/env python

#############################################################################
#This code moves the turtlebot forward or backward for a specified distance.#
#############################################################################

#Import the required libraries
import  rospy
import  math
import  time
from    geometry_msgs.msg   import Twist
from    turtlesim.msg       import Pose
from    std_srvs.srv        import Empty

#Global variables
x = 0
y = 0
yaw = 0

#Callback function for the pose subscriber
def poseCallback(pose_message):
    global x
    global y, yaw

# Update the global variables with the latest pose information
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

#Function to move the turtlebot
    
def move(velocity_publisher, speed, distance, is_forward):
       #declare a Twist message to send velocity commands
        velocity_message = Twist()
        #get current location
        global x, y
        x0=x #save the initial location x-coordinate
        y0=y #save the initial location y-coordinate

        # Set the linear velocity
        if (is_forward):
            velocity_message.linear.x = abs(speed)
            #velocity_message.linear.y = abs(speed) #3asahn amashy y kaman
        else:
            velocity_message.linear.x = -abs(speed)
            #velocity_message.linear.y = -abs(speed) #3asahn amashy y kaman

        # Calculate the distance moved
        distance_moved = 0.0

        # Create a rate object to publish the velocity at 10 Hz
        loop_rate = rospy.Rate(10)

        # While the turtlebot has not reached the desired distance, publish the velocity and sleep for 1/10th of a second
        while True:
                rospy.loginfo("Turtlesim moves forwards")
                velocity_publisher.publish(velocity_message)
                #rospy.loginfo(x)
                #rospy.loginfo(y)
                #rospy.loginfo(x0)
                #rospy.loginfo(y0)

                loop_rate.sleep()

                # Calculate the distance moved
                distance_moved = abs(math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
                print(distance_moved)
                print(x)

                # If the turtlebot has reached the desired distance, break out of the loop
                if  (distance_moved>distance):
                    rospy.loginfo("reached")
                    break

        # Set the linear velocity to 0 to stop the turtlebot
        velocity_message.linear.x = 0
        velocity_publisher.publish(velocity_message)

def rotate (velocity_publisher, angular_speed_degree, relative_angle_degree, clockwise):
    

    velocity_message = Twist()
    velocity_message.linear.x=0
    velocity_message.linear.y=0
    velocity_message.linear.z=0
    velocity_message.angular.x=0
    velocity_message.angular.y=0
    velocity_message.angular.z=0

    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z =-abs(angular_speed)
    else:
        velocity_message.angular.z =abs(angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    #cmd_vel_topic='/cmd_vel_mux/input/teleop'
    #velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("Turtlesim rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()

        print ('current_angle_degree: ',current_angle_degree)
                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break

    #finally, stop the robot when the distance is moved
    velocity_message.angular.z =0
    velocity_publisher.publish(velocity_message)

def go_to_goal(x_goal, y_goal):
    global x
    global y, z, yaw

    velocity_message = Twist()
    cmd_vel_topic='/turtle1/cmd_vel'

    while (True):
        K_linear = 0.5 
        distance = abs(math.sqrt(((x_goal-x) ** 2) + ((y_goal-y) ** 2)))

        linear_speed = distance * K_linear

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal-yaw)*K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=',y)


        if (distance <0.01):
            break

def setDesiredOrientation(publisher,speed_in_degree,desired_angle_degree):
    relative_angle_radians = math.radians(desired_angle_degree) - yaw
    clockwise=0
    if relative_angle_radians < 0:
        clockwise = 1
    else:
        clockwise = 0
    print ("relative_angle_radians:",math.degrees(relative_angle_radians))
    print ("desired_angle_degree :",desired_angle_degree)
    rotate(publisher,speed_in_degree ,math.degrees(abs(relative_angle_radians)), clockwise)

def spiralClean(velocity_publisher,rk,wk):
    vel_msg = Twist()
    loop_rate = rospy.Rate(1)

    while((x<10.5) and (y<10.5)):
        rk=rk+0.5
        vel_msg.linear.x =rk
        vel_msg.linear.y =0
        vel_msg.linear.z =0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z =wk
        velocity_publisher.publish(vel_msg)
        loop_rate.sleep()
 
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)


def letter_M(publisher):
 

    setDesiredOrientation(velocity_publisher,20,135)
    move(velocity_publisher,2.0, 4.0, True)
    setDesiredOrientation(velocity_publisher,20,270)
    move(velocity_publisher,2.0, 5.0, True)
    move(velocity_publisher,2.0, 5.0, False)
    setDesiredOrientation(velocity_publisher,20,315)
    move(velocity_publisher,2.0, 4.0, True)
    setDesiredOrientation(velocity_publisher,20,45)
    move(velocity_publisher,2.0, 4.0, True)
    setDesiredOrientation(velocity_publisher,20,270)
    move(velocity_publisher,2.0, 5.0, True)



    pass

#Main function
if __name__ == '__main__':
    try:
        # Initialize the ROS node
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        # Hena ana ba3mel pubisher 3aashan a2dar abeat beeh velocity 3asahn el x temshy feha
        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        # Hena ana ba3mel subscriber 3ashan yakhod el position x y w y7otaha fel disrance between
        # two points equation w yekarenha bel distance elee ana medehalo foo2 fel function
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)

        # Wait for 2 seconds for the turtlebot to initialize
        time.sleep(2)

    #move(speed, distance, is_forward):
        #move(velocity_publisher, 1.0, 4.0, True)
    
    #rotate (angular_speed_degree, relative_angle_degree, clockwise):   #elfar2 ene di incremental
        #rotate(velocity_publisher, 90, 90, False)

    #go_to_goal(x_goal, y_goal):
        #go_to_goal(9,8)

    #setDesiredOrientation(speed_in_degree,desired_angle_degree):       #elfar2 benha ene di abslute
        #setDesiredOrientation(velocity_publisher,45,45)

    #def spiralClean(line_x,angular_z):
        #spiralClean(velocity_publisher,0,2)

        letter_M(velocity_publisher)


    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
