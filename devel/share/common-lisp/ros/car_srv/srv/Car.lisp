; Auto-generated. Do not edit!


(cl:in-package car_srv-srv)


;//! \htmlinclude Car-request.msg.html

(cl:defclass <Car-request> (roslisp-msg-protocol:ros-message)
  ((range
    :reader range
    :initarg :range
    :type cl:float
    :initform 0.0))
)

(cl:defclass Car-request (<Car-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Car-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Car-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name car_srv-srv:<Car-request> is deprecated: use car_srv-srv:Car-request instead.")))

(cl:ensure-generic-function 'range-val :lambda-list '(m))
(cl:defmethod range-val ((m <Car-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader car_srv-srv:range-val is deprecated.  Use car_srv-srv:range instead.")
  (range m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Car-request>) ostream)
  "Serializes a message object of type '<Car-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'range))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Car-request>) istream)
  "Deserializes a message object of type '<Car-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'range) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Car-request>)))
  "Returns string type for a service object of type '<Car-request>"
  "car_srv/CarRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Car-request)))
  "Returns string type for a service object of type 'Car-request"
  "car_srv/CarRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Car-request>)))
  "Returns md5sum for a message object of type '<Car-request>"
  "54ccab5727cf288228188cbb99fe7680")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Car-request)))
  "Returns md5sum for a message object of type 'Car-request"
  "54ccab5727cf288228188cbb99fe7680")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Car-request>)))
  "Returns full string definition for message of type '<Car-request>"
  (cl:format cl:nil "float32 range~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Car-request)))
  "Returns full string definition for message of type 'Car-request"
  (cl:format cl:nil "float32 range~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Car-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Car-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Car-request
    (cl:cons ':range (range msg))
))
;//! \htmlinclude Car-response.msg.html

(cl:defclass <Car-response> (roslisp-msg-protocol:ros-message)
  ((direction
    :reader direction
    :initarg :direction
    :type cl:string
    :initform ""))
)

(cl:defclass Car-response (<Car-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Car-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Car-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name car_srv-srv:<Car-response> is deprecated: use car_srv-srv:Car-response instead.")))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <Car-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader car_srv-srv:direction-val is deprecated.  Use car_srv-srv:direction instead.")
  (direction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Car-response>) ostream)
  "Serializes a message object of type '<Car-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'direction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'direction))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Car-response>) istream)
  "Deserializes a message object of type '<Car-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'direction) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'direction) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Car-response>)))
  "Returns string type for a service object of type '<Car-response>"
  "car_srv/CarResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Car-response)))
  "Returns string type for a service object of type 'Car-response"
  "car_srv/CarResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Car-response>)))
  "Returns md5sum for a message object of type '<Car-response>"
  "54ccab5727cf288228188cbb99fe7680")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Car-response)))
  "Returns md5sum for a message object of type 'Car-response"
  "54ccab5727cf288228188cbb99fe7680")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Car-response>)))
  "Returns full string definition for message of type '<Car-response>"
  (cl:format cl:nil "string direction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Car-response)))
  "Returns full string definition for message of type 'Car-response"
  (cl:format cl:nil "string direction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Car-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'direction))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Car-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Car-response
    (cl:cons ':direction (direction msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Car)))
  'Car-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Car)))
  'Car-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Car)))
  "Returns string type for a service object of type '<Car>"
  "car_srv/Car")