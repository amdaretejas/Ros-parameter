
(cl:in-package :asdf)

(defsystem "communication_model-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MotionCommand" :depends-on ("_package_MotionCommand"))
    (:file "_package_MotionCommand" :depends-on ("_package"))
  ))