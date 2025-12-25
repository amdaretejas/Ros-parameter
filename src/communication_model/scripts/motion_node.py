#!/usr/bin/env python3

import rospy
from communication_model.msg import MotionCommand

class MotionNode:

    def __init__(self, node_id):
        self.node_id = node_id

        rospy.init_node(node_id)

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

        self.rate = rospy.Rate(5)
        rospy.loginfo(f"{node_id} started")

        self.run()

    def run(self):
        while not rospy.is_shutdown():
            msg = MotionCommand()
            msg.source = self.node_id
            msg.linear_speed = 1.5
            msg.angular_speed = 0.5
            msg.acceleration = 2.0
            msg.deceleration = 2.0
            msg.enable_motion = True

            self.pub.publish(msg)
            rospy.loginfo(f"[{self.node_id}] Published")

            self.rate.sleep()

    def callback(self, msg: MotionCommand):
        if msg.source == self.node_id:
            return

        rospy.loginfo(
            f"""
            [{self.node_id}] Received from {msg.source}
            Linear Speed : {msg.linear_speed}
            Angular Speed: {msg.angular_speed}
            Acceleration : {msg.acceleration}
            Deceleration : {msg.deceleration}
            Enable       : {msg.enable_motion}   
            """
        )

if __name__ == "__main__":
    import sys
    node_name = sys.argv[1] if len(sys.argv) > 1 else "motion_node"
    MotionNode(node_name)
