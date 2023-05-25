
(cl:in-package :asdf)

(defsystem "msg_custom-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Iotsensor" :depends-on ("_package_Iotsensor"))
    (:file "_package_Iotsensor" :depends-on ("_package"))
  ))