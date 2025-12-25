;; Auto-generated. Do not edit!


(when (boundp 'communication_model::MotionCommand)
  (if (not (find-package "COMMUNICATION_MODEL"))
    (make-package "COMMUNICATION_MODEL"))
  (shadow 'MotionCommand (find-package "COMMUNICATION_MODEL")))
(unless (find-package "COMMUNICATION_MODEL::MOTIONCOMMAND")
  (make-package "COMMUNICATION_MODEL::MOTIONCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude MotionCommand.msg.html


(defclass communication_model::MotionCommand
  :super ros::object
  :slots (_source _linear_speed _angular_speed _acceleration _deceleration _enable_motion ))

(defmethod communication_model::MotionCommand
  (:init
   (&key
    ((:source __source) "")
    ((:linear_speed __linear_speed) 0.0)
    ((:angular_speed __angular_speed) 0.0)
    ((:acceleration __acceleration) 0.0)
    ((:deceleration __deceleration) 0.0)
    ((:enable_motion __enable_motion) nil)
    )
   (send-super :init)
   (setq _source (string __source))
   (setq _linear_speed (float __linear_speed))
   (setq _angular_speed (float __angular_speed))
   (setq _acceleration (float __acceleration))
   (setq _deceleration (float __deceleration))
   (setq _enable_motion __enable_motion)
   self)
  (:source
   (&optional __source)
   (if __source (setq _source __source)) _source)
  (:linear_speed
   (&optional __linear_speed)
   (if __linear_speed (setq _linear_speed __linear_speed)) _linear_speed)
  (:angular_speed
   (&optional __angular_speed)
   (if __angular_speed (setq _angular_speed __angular_speed)) _angular_speed)
  (:acceleration
   (&optional __acceleration)
   (if __acceleration (setq _acceleration __acceleration)) _acceleration)
  (:deceleration
   (&optional __deceleration)
   (if __deceleration (setq _deceleration __deceleration)) _deceleration)
  (:enable_motion
   (&optional (__enable_motion :null))
   (if (not (eq __enable_motion :null)) (setq _enable_motion __enable_motion)) _enable_motion)
  (:serialization-length
   ()
   (+
    ;; string _source
    4 (length _source)
    ;; float32 _linear_speed
    4
    ;; float32 _angular_speed
    4
    ;; float32 _acceleration
    4
    ;; float32 _deceleration
    4
    ;; bool _enable_motion
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _source
       (write-long (length _source) s) (princ _source s)
     ;; float32 _linear_speed
       (sys::poke _linear_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angular_speed
       (sys::poke _angular_speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acceleration
       (sys::poke _acceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _deceleration
       (sys::poke _deceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _enable_motion
       (if _enable_motion (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _source
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _source (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _linear_speed
     (setq _linear_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angular_speed
     (setq _angular_speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acceleration
     (setq _acceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _deceleration
     (setq _deceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _enable_motion
     (setq _enable_motion (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get communication_model::MotionCommand :md5sum-) "9bfb8733eb8119d340ffa42ca50b6814")
(setf (get communication_model::MotionCommand :datatype-) "communication_model/MotionCommand")
(setf (get communication_model::MotionCommand :definition-)
      "string source        # who sent this message
float32 linear_speed
float32 angular_speed
float32 acceleration
float32 deceleration
bool    enable_motion

")



(provide :communication_model/MotionCommand "9bfb8733eb8119d340ffa42ca50b6814")


