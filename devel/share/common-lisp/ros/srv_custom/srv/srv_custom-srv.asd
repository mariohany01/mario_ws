
(cl:in-package :asdf)

(defsystem "srv_custom-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "customsrv" :depends-on ("_package_customsrv"))
    (:file "_package_customsrv" :depends-on ("_package"))
  ))