import rospy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def q_info(parent: QWidget, msg: str) -> None:
    rospy.loginfo(msg)
    QMessageBox.information(parent, "INFO", msg)


def q_warn(parent: QWidget, msg: str) -> None:
    rospy.logwarn(msg)
    QMessageBox.warning(parent, "WARN", msg)


def q_error(parent: QWidget, msg: str) -> None:
    rospy.logerr(msg)
    QMessageBox.critical(parent, "ERROR", msg)
