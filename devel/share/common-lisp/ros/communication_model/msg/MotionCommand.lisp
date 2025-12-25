; Auto-generated. Do not edit!


(cl:in-package communication_model-msg)


;//! \htmlinclude MotionCommand.msg.html

(cl:defclass <MotionCommand> (roslisp-msg-protocol:ros-message)
  ((source
    :reader source
    :initarg :source
    :type cl:string
    :initform "")
   (linear_speed
    :reader linear_speed
    :initarg :linear_speed
    :type cl:float
    :initform 0.0)
   (angular_speed
    :reader angular_speed
    :initarg :angular_speed
    :type cl:float
    :initform 0.0)
   (acceleration
    :reader acceleration
    :initarg :acceleration
    :type cl:float
    :initform 0.0)
   (deceleration
    :reader deceleration
    :initarg :deceleration
    :type cl:float
    :initform 0.0)
   (enable_motion
    :reader enable_motion
    :initarg :enable_motion
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MotionCommand (<MotionCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotionCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotionCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name communication_model-msg:<MotionCommand> is deprecated: use communication_model-msg:MotionCommand instead.")))

(cl:ensure-generic-function 'source-val :lambda-list '(m))
(cl:defmethod source-val ((m <MotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader communication_model-msg:source-val is deprecated.  Use communication_model-msg:source instead.")
  (source m))

(cl:ensure-generic-function 'linear_speed-val :lambda-list '(m))
(cl:defmethod linear_speed-val ((m <MotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader communication_model-msg:linear_speed-val is deprecated.  Use communication_model-msg:linear_speed instead.")
  (linear_speed m))

(cl:ensure-generic-function 'angular_speed-val :lambda-list '(m))
(cl:defmethod angular_speed-val ((m <MotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader communication_model-msg:angular_speed-val is deprecated.  Use communication_model-msg:angular_speed instead.")
  (angular_speed m))

(cl:ensure-generic-function 'acceleration-val :lambda-list '(m))
(cl:defmethod acceleration-val ((m <MotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader communication_model-msg:acceleration-val is deprecated.  Use communication_model-msg:acceleration instead.")
  (acceleration m))

(cl:ensure-generic-function 'deceleration-val :lambda-list '(m))
(cl:defmethod deceleration-val ((m <MotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader communication_model-msg:deceleration-val is deprecated.  Use communication_model-msg:deceleration instead.")
  (deceleration m))

(cl:ensure-generic-function 'enable_motion-val :lambda-list '(m))
(cl:defmethod enable_motion-val ((m <MotionCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader communication_model-msg:enable_motion-val is deprecated.  Use communication_model-msg:enable_motion instead.")
  (enable_motion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotionCommand>) ostream)
  "Serializes a message object of type '<MotionCommand>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'source))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'source))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'linear_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angular_speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'deceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enable_motion) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotionCommand>) istream)
  "Deserializes a message object of type '<MotionCommand>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'source) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'source) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'linear_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular_speed) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'acceleration) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'deceleration) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'enable_motion) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotionCommand>)))
  "Returns string type for a message object of type '<MotionCommand>"
  "communication_model/MotionCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotionCommand)))
  "Returns string type for a message object of type 'MotionCommand"
  "communication_model/MotionCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotionCommand>)))
  "Returns md5sum for a message object of type '<MotionCommand>"
  "9bfb8733eb8119d340ffa42ca50b6814")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotionCommand)))
  "Returns md5sum for a message object of type 'MotionCommand"
  "9bfb8733eb8119d340ffa42ca50b6814")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotionCommand>)))
  "Returns full string definition for message of type '<MotionCommand>"
  (cl:format cl:nil "string source        # who sent this message~%float32 linear_speed~%float32 angular_speed~%float32 acceleration~%float32 deceleration~%bool    enable_motion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotionCommand)))
  "Returns full string definition for message of type 'MotionCommand"
  (cl:format cl:nil "string source        # who sent this message~%float32 linear_speed~%float32 angular_speed~%float32 acceleration~%float32 deceleration~%bool    enable_motion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotionCommand>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'source))
     4
     4
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotionCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'MotionCommand
    (cl:cons ':source (source msg))
    (cl:cons ':linear_speed (linear_speed msg))
    (cl:cons ':angular_speed (angular_speed msg))
    (cl:cons ':acceleration (acceleration msg))
    (cl:cons ':deceleration (deceleration msg))
    (cl:cons ':enable_motion (enable_motion msg))
))
