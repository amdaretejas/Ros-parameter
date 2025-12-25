#!/usr/bin/env python3
from quickdata import ParamStore
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from dynamic_reconfigure.server import Server
from rqt_param_demo.cfg import VisionConfig

from ultralytics import YOLO
from vision_msgs.msg import Detection2DArray, Detection2D, ObjectHypothesisWithPose
from geometry_msgs.msg import Pose2D

class YoloVisionNode:

    def __init__(self):
        rospy.init_node("yolo_vision_node")

        self.bridge = CvBridge()

        self.conf_thresh = 0
        self.iou_thresh = 0
        self.enabled = True

        self.store = ParamStore("params.db")
        if self.store.get("yolo.conf_threshold") != None: 
            self.conf_thresh = self.store.get("yolo.conf_threshold")
        
        if self.store.get("yolo.iou_threshold") != None:
            self.iou_thresh = self.store.get("yolo.iou_threshold")

        if self.store.get("yolo.enable_detection") != None:
            self.enabled = self.store.get("yolo.enable_detection")


        self.model = YOLO("yolov8n.pt")  # change if needed

        # self.server = Server(VisionConfig, self.reconfig_cb)

        self.sub = rospy.Subscriber(
            "/camera/image_raw",
            Image,
            self.image_cb,
            queue_size=1
        )
        self.pub = rospy.Publisher(
            "/yolo/detections",
            Detection2DArray,
            queue_size=10
        )

        rospy.loginfo("YOLO Vision Node started")
        rospy.spin()

    def reconfig_cb(self, config, level):
        self.conf_thresh = config.conf_threshold
        self.iou_thresh = config.iou_threshold
        self.enabled = config.enable_detection
        self.store.set("yolo.conf_threshold", config.conf_threshold)
        self.store.set("yolo.iou_threshold", config.iou_threshold)
        self.store.set("yolo.enable_detection", config.enable_detection)
        return config

        # self.conf_thresh = config.conf_threshold
        # self.iou_thresh = config.iou_threshold
        # self.enabled = config.enable_detection

        # rospy.loginfo(
        #     f"[RECONF] conf={self.conf_thresh}, iou={self.iou_thresh}, enabled={self.enabled}"
        # )
        # return config

    def image_cb(self, msg, results):

        detections_msg = Detection2DArray()
        detections_msg.header = msg.header

        for box in results[0].boxes:
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])

            x1, y1, x2, y2 = box.xyxy[0]
            cx = float((x1 + x2) / 2.0)
            cy = float((y1 + y2) / 2.0)
            w = float(x2 - x1)
            h = float(y2 - y1)

            det = Detection2D()
            det.bbox.center.x = cx
            det.bbox.center.y = cy
            det.bbox.size_x = w
            det.bbox.size_y = h

            hyp = ObjectHypothesisWithPose()
            hyp.id = cls_id
            hyp.score = conf

            det.results.append(hyp)
            detections_msg.detections.append(det)

        self.pub.publish(detections_msg)

        # if not self.enabled:
        #     return

        # frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        # results = self.model(
        #     frame,
        #     conf=self.conf_thresh,
        #     iou=self.iou_thresh,
        #     verbose=False
        # )

        # annotated = results[0].plot()
        # cv2.imshow("YOLO Detection", annotated)
        # cv2.waitKey(1)


if __name__ == "__main__":
    YoloVisionNode()

