;; Auto-generated. Do not edit!


(when (boundp 'msg_custom::custommsg)
  (if (not (find-package "MSG_CUSTOM"))
    (make-package "MSG_CUSTOM"))
  (shadow 'custommsg (find-package "MSG_CUSTOM")))
(unless (find-package "MSG_CUSTOM::CUSTOMMSG")
  (make-package "MSG_CUSTOM::CUSTOMMSG"))

(in-package "ROS")
;;//! \htmlinclude custommsg.msg.html


(defclass msg_custom::custommsg
  :super ros::object
  :slots (_id _name _temperature _humidity ))

(defmethod msg_custom::custommsg
  (:init
   (&key
    ((:id __id) 0)
    ((:name __name) "")
    ((:temperature __temperature) 0.0)
    ((:humidity __humidity) 0.0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _name (string __name))
   (setq _temperature (float __temperature))
   (setq _humidity (float __humidity))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:temperature
   (&optional __temperature)
   (if __temperature (setq _temperature __temperature)) _temperature)
  (:humidity
   (&optional __humidity)
   (if __humidity (setq _humidity __humidity)) _humidity)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; string _name
    4 (length _name)
    ;; float32 _temperature
    4
    ;; float32 _humidity
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; float32 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _humidity
       (sys::poke _humidity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _temperature
     (setq _temperature (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _humidity
     (setq _humidity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msg_custom::custommsg :md5sum-) "16767b4b63fd3551b69c6c06672a0bf6")
(setf (get msg_custom::custommsg :datatype-) "msg_custom/custommsg")
(setf (get msg_custom::custommsg :definition-)
      "int32 id
string name
float32 temperature
float32 humidity
")



(provide :msg_custom/custommsg "16767b4b63fd3551b69c6c06672a0bf6")


