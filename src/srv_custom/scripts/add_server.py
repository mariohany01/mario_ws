#!/usr/bin/env python

from srv_custom.srv import AddTwoInts
from srv_custom.srv import AddTwoIntsRequest
from srv_custom.srv import AddTwoIntsResponse
import time
import rospy


def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print ("Ready to add two ints.")
    rospy.spin()
    
def handle_add_two_ints(req):
    print ("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    time.sleep(5)
    sum_response = AddTwoIntsResponse(req.a + req.b)
    return sum_response


    
if __name__ == "__main__":
    add_two_ints_server()