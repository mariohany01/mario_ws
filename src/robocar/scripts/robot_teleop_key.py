#!/usr/bin/env python3
import rospy

#Defines the message type for robot commands, including linear and angular velocities.
#geometry_msgs/Vector3 linear
#geometry_msgs/Vector3 angular
from geometry_msgs.msg import Twist

#sys Provides system-specific parameters and functions.
#Handles I/O operations on multiple file descriptors.
#Manipulates terminal attributes.
#Provides functions for controlling terminal I/O.
import sys, select, termios, tty

msg = """
Control     #          #####        #        #        # 
           # #         #      #     #        #       # #
          #   #        #      #     #    #   #      #   #
         #######       ######       #   # #  #     #######
        #        #     ##           #  #   # #    #       #
       #          #    #  #         # #     ##   #         #
      #            #   #    #       #        #  #           #
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop aw ehbed 3al keyboard 3ashan yo2af
anything else : stop smoothly

CTRL-C to quit
"""


moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }


def getKey():
    # Set the terminal to raw mode. This allows us to read individual keystrokes without having to press Enter.
    tty.setraw(sys.stdin.fileno())
           
    # Check if there is any input available from the user.
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
           
    # If there is input available, read the next character from the input stream.
    if rlist:
        key = sys.stdin.read(1)
    # Otherwise, return an empty string.
    else:
        key = ''
    # Restore the terminal to cooked mode. This will prevent future keystrokes from being interpreted as raw input.
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

#speed = .2
#hena da el starting speed bta3 el 3arabeya
speed   = 1
turn    = 1

def vels(speed,turn):
    #Format the speed and turn values as strings.
    #hena bykhaly el fomat bta3 el speed ele dakhla btebaa bel 0.00 rakamein decimal 
    speed_str = "{:.2f}".format(speed)
    turn_str = "{:.2f}".format(turn)
    # Return a string that shows the current speed and turn.
    return "currently:\t speed {} \t turn {}".format(speed_str, turn_str)
    
    #bido's code
    #return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    
    #byshof el char eih w bakhazeno f kelmet settings
    settings = termios.tcgetattr(sys.stdin)
    
    #node init
    rospy.init_node('BoB_teleop')

    #topic name     ---> /cmd_vel
    #Message Type   ---> Twist

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) 

    x = 0       #liner Motion
    th = 0      #Angular Motion

    status = 0  #3adad el stor el maktoub
    count = 0   #3adad laffat el code
    #acc = 0.05
    target_speed = 0    #Liner speed ele ana 3ayezha say 30 40 50 etc w maktoba fo2 1 
    target_turn = 0     #angular speed ele ana 3ayezha say 30 40 50 etc w maktoba fo2 1
    control_speed = 0   #liner speed ele bykaren beha ashan ykhaly el acc smooth
    control_turn = 0    #angular speed ele bykaren beha ashan ykhaly el acc smooth

    try:
        print (msg)
        print (vels(speed,turn))
        while(1):
            key = getKey()
     
            if key in moveBindings.keys(): 
            #'u':(1,1)      'i':(1,0)  'o':(1,-1)
            #'j':(0,1)      'k':(0,0)  'l':(0,-1),
            #'m':(-1,-1)    ',':(-1,0) '.':(-1,1),
            #Hena haykhazen bas el kema ele feh fel x wel th sawa2 1 aw 0 aw -1
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
                #to show what is printing ins X and Th 
                #print ("X= " , x )
                #print ("Th=" , th)
                #print("---------------")

           
            elif key in speedBindings.keys():
                #Hena haykhazen ele fel harf f  heteten b3dein yedrabo fel speed w fel turn awel wahda 
                #heya ele btthakem fel speed w tany wahda fel turn anhy wahda sor3etha tezed w anhy te2el 
		        #Modified for mobile robot
                #all            Liner             Angular
                #'q':(1.1,1.1), 'w':(1.1,1),    'e':(1,1.1),   
                #'z':(.9,.9),   'x':(.9,1),     'c':(1,.9), 
              
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                count = 0
                print (vels(speed,turn)) #di el asaseya


                if (status == 10):
                    print (msg)
                status = (status + 1) % 15

            elif key == 'k' :
                x = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 2:       #lau habadt 3al keyboard el robot yo2af
                    x = 0
                    th = 0
                    #speed= 1
                    #turn = 1
                if (key == '\x03'): #ASCII ctrl+c
                    break
  
            target_speed = speed * x   # ex dost I = (1,0) Fa hayedrab el speed f x ele heya b 1    --30*1=1
            target_turn = turn * th     # w hayedrab el th ele heya b zero f el turn                --30*0=0
            
            #for smoooooothhhhhhnesssssss Lel turn
            
            if target_speed > control_speed:    #30>0
                control_speed = min( target_speed, control_speed + 0.1 )
                                #30 , 0+0.1 

            elif target_speed < control_speed:  
                control_speed = max( target_speed, control_speed - 0.1 )

            else:
                control_speed = target_speed

            #for smoooooothhhhhhnesssssss Lel turn

            if target_turn > control_turn:
                control_turn = min( target_turn, control_turn + 0.5 )

            elif target_turn < control_turn:
                control_turn = max( target_turn, control_turn - 0.5 )

            else:
                control_turn = target_turn

            twist = Twist()
            twist.linear.x = control_speed; 
            twist.linear.y = 0; 
            twist.linear.z = 0
            twist.angular.x = 0; 
            twist.angular.y = 0; 
            twist.angular.z = control_turn
            pub.publish(twist)


    except:
        rospy.logwarn("Fi haga Ghalat, Help!!!!")

    finally:
        twist = Twist()
        twist.linear.x = 0; 
        twist.linear.y = 0; 
        twist.linear.z = 0
        twist.angular.x = 0; 
        twist.angular.y = 0; 
        twist.angular.z = 0
        pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

