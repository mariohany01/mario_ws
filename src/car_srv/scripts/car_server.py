#!/usr/bin/env python

from car_srv.srv import Car
from car_srv.srv import CarRequest
from car_srv.srv import CarResponse
import time
import rospy


def car_server():
    rospy.init_node('car_server')
    s = rospy.Service('car_data', Car, handle_car)
    print ("ready to take action")
    rospy.spin()
    
def handle_car(req):
    
    if range < 5:
        bedo = "Stop"
        print ("%s",bedo)
    else :
        bedo = "Forward"
        print ("%s",bedo)

    time.sleep(5)
    car_response = CarResponse("%s",bedo)
    return car_response


    
if __name__ == "__main__":
    car_server()