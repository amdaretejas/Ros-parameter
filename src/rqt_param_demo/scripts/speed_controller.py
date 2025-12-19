#!/usr/bin/env python3

import rospy

def main():
    rospy.init_node("speed_controller")

    rospy.set_param("robot_speed", 0.5)
    rospy.set_param("max_speed", 2.0)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        speed = rospy.get_param("robot_speed")
        max_speed = rospy.get_param("max_speed")

        if speed > max_speed:
            rospy.logwarn("Speed exceeds max! Limiting it.")
            speed = max_speed

        rospy.loginfo(f"Robot speed = {speed}")
        rate.sleep()

if __name__ == "__main__":
    main()
