#!/usr/bin/env python3

import rospy
from communication_model.msg import MotionCommand


class RobotNode:

    def __init__(self):
        rospy.init_node("robot_node")

        self.pub = rospy.Publisher(
            "/motion_bus",
            MotionCommand,
            queue_size=10
        )

        rospy.Subscriber(
            "/motion_bus",
            MotionCommand,
            self.callback
        )

        rospy.loginfo("Robot node started")
        rospy.spin()

    def callback(self, msg: MotionCommand):
        if msg.source == "robot":
            return

        rospy.loginfo(
            f"""
            [ROBOT RECEIVED]
            Linear Speed : {msg.linear_speed}
            Angular Speed: {msg.angular_speed}
            Acceleration : {msg.acceleration}
            Deceleration : {msg.deceleration}
            Enable       : {msg.enable_motion}
            """
        )

        # Optional feedback
        feedback = MotionCommand()
        feedback.source = "robot"
        feedback.linear_speed = msg.linear_speed
        feedback.angular_speed = msg.angular_speed
        feedback.acceleration = msg.acceleration
        feedback.deceleration = msg.deceleration
        feedback.enable_motion = msg.enable_motion

        self.pub.publish(feedback)

if __name__ == "__main__":
    RobotNode()
