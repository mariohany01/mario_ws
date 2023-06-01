
(cl:in-package :asdf)

(defsystem "car_srv-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Car" :depends-on ("_package_Car"))
    (:file "_package_Car" :depends-on ("_package"))
  ))