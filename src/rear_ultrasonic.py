#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

class Rear():
    def __init__(self):
        # initiliaze
        rospy.init_node('rear_sensor', anonymous=False)

        # What to do you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
     
	# 5 HZ
        r = rospy.Rate(5);

	# create one Twist() variables for moving backwards.
        move_cmd = Twist()
	# let's go backwards at 0.2 m/s
        move_cmd.linear.x = 0.2

        sub = rospy.Subscriber('/ultrasound', range_msg, callback)

	

	#Go backwards for 2 seconds (10 x 5 HZ)
        while not rospy.is_shutdown():
	    rospy.loginfo("Going Straight")
            self.cmd_vel.publish(move_cmd)
            r.sleep()
        
    def callback(msg):
	distance = msg.range
	if distance < 20:
	    shutdown()

    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        Rear()
    except:
        rospy.loginfo("node terminated.")
