#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from dynamic_reconfigure.server import Server
from rqt_param_demo.cfg import VisionConfig

from ultralytics import YOLO

class YoloVisionNode:

    def __init__(self):
        rospy.init_node("yolo_vision_node")

        self.bridge = CvBridge()

        self.conf_thresh = 0.5
        self.iou_thresh = 0.45
        self.enabled = True

        self.model = YOLO("yolov8n.pt")  # change if needed

        self.server = Server(VisionConfig, self.reconfig_cb)

        self.sub = rospy.Subscriber(
            "/camera/image_raw",
            Image,
            self.image_cb,
            queue_size=1
        )

        rospy.loginfo("YOLO Vision Node started")
        rospy.spin()

    def reconfig_cb(self, config, level):
        self.conf_thresh = config.conf_threshold
        self.iou_thresh = config.iou_threshold
        self.enabled = config.enable_detection

        rospy.loginfo(
            f"[RECONF] conf={self.conf_thresh}, iou={self.iou_thresh}, enabled={self.enabled}"
        )
        return config

    def image_cb(self, msg):
        if not self.enabled:
            return

        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        results = self.model(
            frame,
            conf=self.conf_thresh,
            iou=self.iou_thresh,
            verbose=False
        )

        annotated = results[0].plot()
        cv2.imshow("YOLO Detection", annotated)
        cv2.waitKey(1)


if __name__ == "__main__":
    YoloVisionNode()

