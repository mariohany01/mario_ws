
(cl:in-package :asdf)

(defsystem "msg_custom-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "custommsg" :depends-on ("_package_custommsg"))
    (:file "_package_custommsg" :depends-on ("_package"))
  ))