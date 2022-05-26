#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def degree():
   pub = rospy.Publisher("/deg_topic", Float32,  queue_size=10)
   rospy.init_node('deg2rad', anonymous=True)
   rate = rospy.Rate(0.2)

   while not rospy.is_shutdown():
       msg = Float32()
       msg.data = rospy.get_param("/degrees")
       rospy.loginfo(msg)
       pub.publish(msg)
       rate.sleep()

if __name__ == '__main__':
   try:
       degree()
   except rospy.ROSInterruptException:
       pass

