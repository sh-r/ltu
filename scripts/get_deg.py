#!/usr/bin/env python3
from cmath import pi
import rospy
from std_msgs.msg import Float32
rad=0

def receive_deg_cb(msg):    # call back function
   global rad
   rad = msg.data * (pi/180)
   rospy.loginfo(rad)

if __name__ == '__main__':
   rospy.init_node('get_deg')
   sub = rospy.Subscriber("deg_topic", Float32, receive_deg_cb)
   rospy.spin()