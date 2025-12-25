#!/usr/bin/env python3

import rospy
from dynamic_reconfigure.server import Server
from rqt_param_demo.cfg import MotionConfigConfig
from quickdata.store import ParamStore
# from lib import ParamStore

class MotionController:

    def __init__(self):
        rospy.init_node("motion_controller")

        # -----------------------------
        # 1️⃣ DATABASE (SOURCE OF TRUTH)
        # -----------------------------
        self.store = ParamStore("params.db")

        self.linear_speed = self.store.get("motion.linear_speed", 0.5)
        self.angular_speed = self.store.get("motion.angular_speed", 1.0)
        self.acceleration_limit = self.store.get("motion.acceleration_limit", 1.0)
        self.enable_motion = self.store.get("motion.enable_motion", True)

        # Load persisted values
        saved_values = {
            "linear_speed": self.linear_speed,
            "angular_speed": self.angular_speed,
            "acceleration_limit": self.acceleration_limit,
            "enable_motion": self.enable_motion
        }
        # -----------------------------
        # 2️⃣ DYNAMIC RECONFIGURE
        # -----------------------------
        self.server = Server(MotionConfigConfig, self.reconfig_callback)

        # 🔥 CRITICAL LINE — inject DB values
        self.server.update_configuration(saved_values)

        rospy.loginfo("Motion Controller started with persisted values")
        self.run()

    def reconfig_callback(self, config, level):
        # -----------------------------
        # 3️⃣ SAVE rqt CHANGES TO DB
        # -----------------------------
        self.store.set("motion.linear_speed", config.linear_speed)
        self.store.set("motion.angular_speed", config.angular_speed)
        self.store.set("motion.acceleration_limit", config.acceleration_limit)
        self.store.set("motion.enable_motion", config.enable_motion)
        print(config.tejas)
        rospy.loginfo(
            f"[Reconfigure] lin={config.linear_speed}, "
            f"ang={config.angular_speed}, "
            f"acc={config.acceleration_limit}, "
            f"enabled={config.enable_motion}"
        )

        return config

    def run(self):
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
            self.linear_speed = self.store.get("motion.linear_speed")
            self.angular_speed = self.store.get("motion.angular_speed")
            self.acceleration_limit = self.store.get("motion.acceleration_limit")
            self.enable_motion = self.store.get("motion.enable_motion")
            if self.enable_motion:
                rospy.loginfo(
                    f"Moving | v={self.linear_speed}, "
                    f"acc={self.acceleration_limit}, "
                    f"w={self.angular_speed}"
                )
            else:
                rospy.logwarn("Motion DISABLED")

            rate.sleep()


if __name__ == "__main__":
    MotionController()
