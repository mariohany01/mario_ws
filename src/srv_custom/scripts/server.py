#!/usr/bin/env python3
# license removed for brevity

from srv_custom.srv import customsrv
from srv_custom.srv import customsrvRequest
from srv_custom.srv import customsrvResponse
import time
import rospy


def add_two_ints_server():
    rospy.init_node('add_two_ints_server_py')
    s = rospy.Service('add_two_ints', customsrv, handle_add_two_ints)
    print ("Ready to add two ints.")
    rospy.spin()
    
def handle_add_two_ints(req):
    print ("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    time.sleep(5)
    sum_response = customsrvResponse(req.a + req.b)
    return sum_response


    
if __name__ == "__main__":
    add_two_ints_server()