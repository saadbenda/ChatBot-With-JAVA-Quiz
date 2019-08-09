# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 554)
        self.human = QtWidgets.QPlainTextEdit(Dialog)
        self.human.setGeometry(QtCore.QRect(90, 80, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(11)
        self.human.setFont(font)
        self.human.setObjectName("human")
        self.robot = QtWidgets.QPlainTextEdit(Dialog)
        self.robot.setGeometry(QtCore.QRect(10, 190, 511, 341))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        self.robot.setFont(font)
        self.robot.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard)
        self.robot.setObjectName("robot")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.GitHub = QtWidgets.QPushButton(Dialog)
        self.GitHub.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.GitHub.setObjectName("GitHub")
        self.Admin = QtWidgets.QPushButton(Dialog)
        self.Admin.setGeometry(QtCore.QRect(540, 30, 75, 23))
        self.Admin.setObjectName("Admin")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("view/human.png"))
        self.label_2.setObjectName("label_2")
        self.robotLogo = QtWidgets.QLabel(Dialog)
        self.robotLogo.setGeometry(QtCore.QRect(530, 190, 81, 91))
        self.robotLogo.setText("")
        self.robotLogo.setPixmap(QtGui.QPixmap("view/robot.png"))
        self.robotLogo.setObjectName("robotLogo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ChatBot Accenture"))
        self.GitHub.setText(_translate("Dialog", "Github"))
        self.Admin.setText(_translate("Dialog", "Admin"))

