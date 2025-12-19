#!/usr/bin/env python3

import rospy
from dynamic_reconfigure.server import Server
from rqt_param_demo.cfg import MotionConfigConfig

class MotionController:

    def __init__(self):
        rospy.init_node("motion_controller")

        self.linear_speed = 0.0
        self.angular_speed = 0.0
        self.acc_limit = 0.0
        self.enabled = True

        self.server = Server(MotionConfigConfig, self.reconfig_callback)

        rospy.loginfo("Motion Controller Started")

        self.run()

    def reconfig_callback(self, config, level):
        self.linear_speed = config.linear_speed
        self.angular_speed = config.angular_speed
        self.acc_limit = config.acceleration_limit
        self.enabled = config.enable_motion

        rospy.loginfo(
            f"[Reconfigure] lin={self.linear_speed}, "
            f"ang={self.angular_speed}, "
            f"acc={self.acc_limit}, "
            f"enabled={self.enabled}"
        )

        return config

    def run(self):
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
            if self.enabled:
                rospy.loginfo(
                    f"Moving | v={self.linear_speed}, "
                    f"w={self.angular_speed}"
                )
            else:
                rospy.logwarn("Motion DISABLED")

            rate.sleep()


if __name__ == "__main__":
    MotionController()

