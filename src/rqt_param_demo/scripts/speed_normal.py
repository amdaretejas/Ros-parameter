#!/usr/bin/env python3

import rospy

def main():
    rospy.init_node("speed_controller")

    # Default parameter
    rospy.set_param("robot_speed", 1.0)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        speed = rospy.get_param("robot_speed")
        rospy.loginfo(f"Robot moving at speed: {speed}")
        rate.sleep()

if __name__ == "__main__":
    main()
