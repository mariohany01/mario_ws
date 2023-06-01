;; Auto-generated. Do not edit!


(when (boundp 'car_srv::Car)
  (if (not (find-package "CAR_SRV"))
    (make-package "CAR_SRV"))
  (shadow 'Car (find-package "CAR_SRV")))
(unless (find-package "CAR_SRV::CAR")
  (make-package "CAR_SRV::CAR"))
(unless (find-package "CAR_SRV::CARREQUEST")
  (make-package "CAR_SRV::CARREQUEST"))
(unless (find-package "CAR_SRV::CARRESPONSE")
  (make-package "CAR_SRV::CARRESPONSE"))

(in-package "ROS")





(defclass car_srv::CarRequest
  :super ros::object
  :slots (_range ))

(defmethod car_srv::CarRequest
  (:init
   (&key
    ((:range __range) 0.0)
    )
   (send-super :init)
   (setq _range (float __range))
   self)
  (:range
   (&optional __range)
   (if __range (setq _range __range)) _range)
  (:serialization-length
   ()
   (+
    ;; float32 _range
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _range
       (sys::poke _range (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _range
     (setq _range (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass car_srv::CarResponse
  :super ros::object
  :slots (_direction ))

(defmethod car_srv::CarResponse
  (:init
   (&key
    ((:direction __direction) "")
    )
   (send-super :init)
   (setq _direction (string __direction))
   self)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:serialization-length
   ()
   (+
    ;; string _direction
    4 (length _direction)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _direction
       (write-long (length _direction) s) (princ _direction s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _direction
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _direction (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass car_srv::Car
  :super ros::object
  :slots ())

(setf (get car_srv::Car :md5sum-) "54ccab5727cf288228188cbb99fe7680")
(setf (get car_srv::Car :datatype-) "car_srv/Car")
(setf (get car_srv::Car :request) car_srv::CarRequest)
(setf (get car_srv::Car :response) car_srv::CarResponse)

(defmethod car_srv::CarRequest
  (:response () (instance car_srv::CarResponse :init)))

(setf (get car_srv::CarRequest :md5sum-) "54ccab5727cf288228188cbb99fe7680")
(setf (get car_srv::CarRequest :datatype-) "car_srv/CarRequest")
(setf (get car_srv::CarRequest :definition-)
      "float32 range
---
string direction
")

(setf (get car_srv::CarResponse :md5sum-) "54ccab5727cf288228188cbb99fe7680")
(setf (get car_srv::CarResponse :datatype-) "car_srv/CarResponse")
(setf (get car_srv::CarResponse :definition-)
      "float32 range
---
string direction
")



(provide :car_srv/Car "54ccab5727cf288228188cbb99fe7680")


