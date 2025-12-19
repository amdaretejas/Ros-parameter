#!/usr/bin/env python3

import rospy
import time
from dynamic_reconfigure.server import Server
from rqt_param_demo.cfg import PIDConfig

class PIDController:

    def __init__(self):
        rospy.init_node("pid_controller")

        self.kp = 1.0
        self.ki = 0.0
        self.kd = 0.0
        self.target = 10.0

        self.current = 0.0
        self.prev_error = 0.0
        self.integral = 0.0
        self.last_time = time.time()

        self.server = Server(PIDConfig, self.reconfigure_cb)

        rospy.loginfo("PID Controller started")
        self.loop()

    def reconfigure_cb(self, config, level):
        self.kp = config.kp
        self.ki = config.ki
        self.kd = config.kd
        self.target = config.target

        rospy.loginfo(
            f"[PID RECONF] Kp={self.kp}, Ki={self.ki}, Kd={self.kd}, Target={self.target}"
        )

        return config

    def loop(self):
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            now = time.time()
            dt = now - self.last_time
            self.last_time = now

            error = self.target - self.current
            self.integral += error * dt
            derivative = (error - self.prev_error) / dt if dt > 0 else 0.0

            output = (
                self.kp * error +
                self.ki * self.integral +
                self.kd * derivative
            )

            # Simulated plant
            self.current += output * dt

            rospy.loginfo(
                f"pos={self.current:.2f} err={error:.2f} out={output:.2f}"
            )

            self.prev_error = error
            rate.sleep()


if __name__ == "__main__":
    PIDController()

