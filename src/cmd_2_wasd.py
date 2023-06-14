#! /usr/bin/env python3
import rospy 
from std_msgs.msg import String, Bool
from geometry_msgs.msg import Twist

rospy.init_node("controller")

rover_speed = 5

rover = rospy.Publisher("/rover_control", String, queue_size=10)
logger = rospy.Publisher("/log", String, queue_size=10)

def joy_callback(msg:Twist):
    rover_msg = ""
    if abs(msg.linear.x) > abs(msg.angular.z):
        if msg.linear.x > 1.8:
            rover_msg = "w"
        elif msg.linear.x < -1.8:
            rover_msg = "s"
        else:
            rover_msg = "-"

    elif abs(msg.angular.z) > abs(msg.linear.x):
        if msg.angular.z > 1.8:
            rover_msg = "a"
        elif msg.angular.z < -1.8:
            rover_msg = "d"
        else:
            rover_msg = "-"
    rospy.loginfo(rover_msg)
    rover.publish(rover_msg)

def neg_speed_callback(msg:Bool):
    global rover_speed
    if msg.data == True:
        if rover_speed <= 1:
            rospy.loginfo("Lowest speed")
            rover_speed = 1
        else:
            rover_speed -= 1
    rover.publish(str(rover_speed))
    logger.publish(str(rover_speed))
    rospy.loginfo(str(rover_speed))

def pos_speed_callback(msg:Bool):
    global rover_speed
    if msg.data == True:
        if rover_speed >= 10:
            rospy.loginfo("Highest speed")
            rover_speed = 10
        else:
            rover_speed += 1
    rover.publish(str(rover_speed))
    logger.publish(str(rover_speed))
    rospy.loginfo(str(rover_speed))

rospy.Subscriber("/cmd_vel", Twist, joy_callback)
rospy.Subscriber("/speed_decrease", Bool, neg_speed_callback)
rospy.Subscriber("/speed_increase", Bool, pos_speed_callback)
rospy.spin()
