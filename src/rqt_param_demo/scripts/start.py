#!/usr/bin/env python3

import rospy
from dynamic_reconfigure.server import Server
from rqt_param_demo.cfg import MotionConfigConfig
from quickdata import ParamStore 


class MotionController:
    def __init__(self):
        # self.server = Server(MotionConfigConfig, self.reconfig_callback)
        self.store = ParamStore(MotionConfigConfig, "motion")
        self.run()
        
    def run(self):
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
            if self.store.config.enable_motion:
                rospy.loginfo(
                    f"Moving | v={self.store.config.linear_speed}, "
                    f"acc={self.store.config.acceleration_limit}, "
                    f"w={self.store.config.angular_speed}"
                )
            else:
                rospy.logwarn("Motion DISABLED")

            rate.sleep()
if __name__ == "__main__":
    rospy.init_node("motion_controller")
    MotionController()
    rospy.spin()
