#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range
cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

def callback(data):
    distance = data.range
    print(distance)

    twist  = Twist()
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0

    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0

	if distance > 20:
	    twist.linear.x = -0.25
    elif distance < 20 AND distance > 10:
        twist.linear.x = distance*(-1)
    else:
        twist.linear.x = 0.0

if __name__ == '__main__':
    try:
        # initiliaze
        rospy.init_node('rear_sensor', anonymous=False)
        # What to do you ctrl + c
        rospy.on_shutdown(self.shutdown)
        #subcriber ultrasound
        rospy.Subscriber('/ultrasound', range_msg, callback)

    except:
        rospy.loginfo("node terminated.")
