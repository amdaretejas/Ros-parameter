#!/usr/bin/env python3

import rospy
from dynamic_reconfigure.server import Server
from communication_model.msg import MotionCommand
from communication_model.cfg import MotionControlConfig
from quickdata import ParamStore


class ControllerNode:

    def __init__(self):
        rospy.init_node("motion_controller")

        self.pub = rospy.Publisher(
            "/motion_bus",
            MotionCommand,
            queue_size=10
        )

        self.current_cmd = MotionCommand()
        self.current_cmd.source = "controller"

        # self.server = Server(
        #     MotionControlConfig,
        #     self.reconfig_callback
        # )

        # self.server = ParamStore(MotionControlConfig, "motion", callback=self.reconfig_callback)
        self.server = ParamStore(
            package="communication_model",
            config_name="MotionControl",
            key="motion",
            callback=self.reconfig_callback
        )


        rospy.loginfo("Motion Controller with rqt started")
        rospy.spin()

    def reconfig_callback(self, config, level):
        # Update command from rqt
        self.current_cmd.linear_speed = config.linear_speed
        self.current_cmd.angular_speed = config.angular_speed
        self.current_cmd.acceleration = config.acceleration
        self.current_cmd.deceleration = config.deceleration
        self.current_cmd.enable_motion = config.enable_motion

        # Publish immediately on change
        self.pub.publish(self.current_cmd)

        rospy.loginfo("Published updated command from rqt")
        return config


if __name__ == "__main__":
    ControllerNode()