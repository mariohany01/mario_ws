#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32, Int32, Bool
from geometry_msgs.msg import Twist 
    
#Mapping -1 - 1 to -255 to 255
from numpy import interp
#############################################################
#############################################################
class TwistToMotors():
#############################################################
#############################################################

    #############################################################
    def __init__(self):
        # Initialize ROS node
        rospy.init_node("twist_to_motors")
        nodename = rospy.get_name()
        
        # Log a message to the console indicating that the node has started.
        rospy.loginfo("%s started" % nodename)

        # Set up shutdown callback
        rospy.on_shutdown(self.shutdown_cb)

        # Define helper function for sign determination
        # The function returns 1 if a is positive, -1 if a is negative, and 0 if a is 0. This is a concise way to implement a sign function.
        self.sign = lambda a: (a>0) - (a<0)
        #print("The value of a is:", a)

        # Initialize motor speed messages
        self.left_speed = Int32()
        self.right_speed = Int32()

        # Get robot parameters from ROS parameters server
        #this uset to configure base = 0.125 meter 
        #this used to confugure speed 180 rpm
        self.w = rospy.get_param("~base_width", 0.125)
        self.fixed_speed = rospy.get_param("~fixed_speed", 180)
    
        # Initialize motor speed publishers
        self.pub_lmotor = rospy.Publisher('set_left_speed', Int32,queue_size=1)
        self.pub_rmotor = rospy.Publisher('set_right_speed', Int32,queue_size=1)

        # Initialize reset publisher
        self.reset = rospy.Publisher('reset', Bool,queue_size=1)

        # Subscribe to `/cmd_vel` topic for Twist messages
        rospy.Subscriber('/cmd_vel', Twist, self.twistCallback)
    
        # Get ROS parameters for loop rate and timeout
        self.rate = rospy.get_param("~rate", 50)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)
        
        # Initialize internal variables for motor speeds
        self.left = 0
        self.right = 0
    #############################################################
    def shutdown_cb(self):
        # Reset motors on shutdown
        rospy.logwarn("Resetting board")
        self.pub_lmotor.publish(0)
        self.pub_rmotor.publish(0)
        self.reset.publish(0)
        pass
    #############################################################
    def spin(self):    
        # Create rate objects for main loop and idle loop
        r = rospy.Rate(self.rate)   # Main loop rate (Hz) 50
        idle = rospy.Rate(10)       # Idle loop rate (Hz)

        # Initialize time reference for timeout
        then = rospy.Time.now()
            
        # Initialize timeout counter
        self.ticks_since_target = self.timeout_ticks
    
        ###### main loop  ######
        while not rospy.is_shutdown():  # Continue until ROS shutdown
        # Active loop: process Twist messages
            while not rospy.is_shutdown() and self.ticks_since_target < self.timeout_ticks: 
                self.spinOnce()     # Process a Twist message and calculate motor speeds
                r.sleep()           # Sleep for the main loop rate (e.g., 50 Hz)
            
            # Idle loop: motors inactive or minimal actions
            idle.sleep()            # Sleep for the idle loop rate (e.g., 10 Hz)  
            self.ticks_since_target += 1     #ana ghayart makano kan taht f spin once    
    #############################################################
    def spinOnce(self):

        """
        Processes a single Twist message and calculates motor speeds.
        """
        # (Commented out lines: alternative calculation using linear and angular velocities)
        # dx = (l + r) / 2
        # dr = (r - l) / w
            
        # Calculate individual motor speeds based on linear and angular velocities
        self.right = 1.0 * self.dx + self.dr * self.w / 2 
        self.left = 1.0 * self.dx - self.dr * self.w / 2

        # Map speeds to fixed speed range (consider sign)
        self.left_mapped = self.sign(self.left)*self.fixed_speed
        self.right_mapped = self.sign(self.right)*self.fixed_speed

        # Convert to integer for motor commands and print for debugging (optional)
        self.left_speed.data = int(self.left_mapped)
        self.right_speed.data =int(self.right_mapped)
        
        print ("left  " , self.left_speed ,"Right " , self.right_speed  )

        
        #rospy.loginfo("Left")
        #rospy.loginfo()
        #rospy.loginfo("Right")
        #rospy.loginfo(self.right_speed)

        # Publish motor speed commands
        self.pub_lmotor.publish(self.left_speed)
        self.pub_rmotor.publish(self.right_speed)


    #############################################################
    def twistCallback(self,msg):
        # rospy.loginfo("-D- twistCallback: %s" % str(msg))
        self.ticks_since_target = 0
        self.dx = msg.linear.x
        self.dr = msg.angular.z
        self.dy = msg.linear.y
    
#############################################################
#############################################################
if __name__ == '__main__':
    """ main """
    twistToMotors = TwistToMotors()
    twistToMotors.spin()
