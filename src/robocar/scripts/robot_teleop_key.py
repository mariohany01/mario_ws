#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Control #####      @@@    #####
        #    #    @   @   #    #
        #####    @     @  #####
        #    #    @   @   #    #
        #####      @@@    #####
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
speed   = 30
turn    = 30

def vels(speed,turn):
    #ChatGPT Modification
    # Format the speed and turn values as strings.
    speed_str = "{:.2f}".format(speed)
    turn_str = "{:.2f}".format(turn)
    # Return a string that shows the current speed and turn.
    return "currently:\tspeed {} \tturn {}".format(speed_str, turn_str)
    
    #bido's code
    #return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('BoB_teleop')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    x = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    try:
        print (msg)
        print (vels(speed,turn))
        while(1):
            key = getKey()

            if key in moveBindings.keys():
            #Hena haykhazen bas el kema ele feh fel x wel th sawa2 1 aw 0 aw -1
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
            
            elif key in speedBindings.keys():
                #Hena haykhazen ele fel harf f  heteten b3dein yedrabo fel speed w fel turn awel wahda 
                #heya ele btthakem fel speed w tany wahda fel turn anhy wahda sor3etha tezed w anhy te2el 
		        #Modified for mobile robot
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                #speed = speed 
                #turn = turn 
                count = 0
                print (vels(speed,turn))
                if (status == 10):
                    print (msg)
                status = (status + 1) % 15

            elif key == ' ' or key == 'k' :
                x = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 4:       #lau habadt 3al keyboard el robot yo2af
                    x = 0
                    th = 0
                    speed= 30
                    turn = 30
                if (key == '\x03'): #ASCII ctrl+c
                    break

            target_speed = speed * x
            target_turn = turn * th

            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 0.1 )
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 0.1 )
            else:
                control_speed = target_speed

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

