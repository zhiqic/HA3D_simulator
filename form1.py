# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1051, 729)
        self.label_frame1 = QtWidgets.QLabel(Form)
        self.label_frame1.setGeometry(QtCore.QRect(10, 10, 1024, 256))
        self.label_frame1.setObjectName("label_frame1")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(339, 270, 21, 231))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(700, 270, 21, 231))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(0, 260, 1041, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(720, 360, 51, 17))
        self.label_12.setObjectName("label_12")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(360, 270, 251, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_scanID = QtWidgets.QLabel(self.widget)
        self.label_scanID.setObjectName("label_scanID")
        self.horizontalLayout.addWidget(self.label_scanID)
        self.textBrowser_scanID = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_scanID.setObjectName("textBrowser_scanID")
        self.horizontalLayout.addWidget(self.textBrowser_scanID)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(360, 340, 331, 161))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.textBrowser_agentViewpointID = QtWidgets.QTextBrowser(self.widget1)
        self.textBrowser_agentViewpointID.setObjectName("textBrowser_agentViewpointID")
        self.horizontalLayout_7.addWidget(self.textBrowser_agentViewpointID)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.textBrowser_agentHeading = QtWidgets.QTextBrowser(self.widget1)
        self.textBrowser_agentHeading.setObjectName("textBrowser_agentHeading")
        self.horizontalLayout_8.addWidget(self.textBrowser_agentHeading)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.textBrowser_agentLocation = QtWidgets.QTextBrowser(self.widget1)
        self.textBrowser_agentLocation.setObjectName("textBrowser_agentLocation")
        self.horizontalLayout_9.addWidget(self.textBrowser_agentLocation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_agentPrevious = QtWidgets.QPushButton(self.widget1)
        self.pushButton_agentPrevious.setObjectName("pushButton_agentPrevious")
        self.horizontalLayout_12.addWidget(self.pushButton_agentPrevious)
        self.pushButton_agentNext = QtWidgets.QPushButton(self.widget1)
        self.pushButton_agentNext.setObjectName("pushButton_agentNext")
        self.horizontalLayout_12.addWidget(self.pushButton_agentNext)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(770, 270, 271, 231))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.widget2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.dial_humanHeading = QtWidgets.QDial(self.widget2)
        self.dial_humanHeading.setObjectName("dial_humanHeading")
        self.horizontalLayout_10.addWidget(self.dial_humanHeading)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.widget2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.dial_agentHeading = QtWidgets.QDial(self.widget2)
        self.dial_agentHeading.setObjectName("dial_agentHeading")
        self.horizontalLayout_11.addWidget(self.dial_agentHeading)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.pushButton_save = QtWidgets.QPushButton(self.widget2)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout_3.addWidget(self.pushButton_save)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(0, 270, 341, 231))
        self.widget3.setObjectName("widget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textBrowser_humanViewpointID = QtWidgets.QTextBrowser(self.widget3)
        self.textBrowser_humanViewpointID.setObjectName("textBrowser_humanViewpointID")
        self.horizontalLayout_2.addWidget(self.textBrowser_humanViewpointID)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.textBrowser_region = QtWidgets.QTextBrowser(self.widget3)
        self.textBrowser_region.setObjectName("textBrowser_region")
        self.horizontalLayout_3.addWidget(self.textBrowser_region)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.textBrowser_humanMotion = QtWidgets.QTextBrowser(self.widget3)
        self.textBrowser_humanMotion.setEnabled(True)
        self.textBrowser_humanMotion.setObjectName("textBrowser_humanMotion")
        self.horizontalLayout_4.addWidget(self.textBrowser_humanMotion)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.textBrowser_humanHeading = QtWidgets.QTextBrowser(self.widget3)
        self.textBrowser_humanHeading.setObjectName("textBrowser_humanHeading")
        self.horizontalLayout_5.addWidget(self.textBrowser_humanHeading)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.textBrowser_humanLocation = QtWidgets.QTextBrowser(self.widget3)
        self.textBrowser_humanLocation.setObjectName("textBrowser_humanLocation")
        self.horizontalLayout_6.addWidget(self.textBrowser_humanLocation)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_humanPrevious = QtWidgets.QPushButton(self.widget3)
        self.pushButton_humanPrevious.setObjectName("pushButton_humanPrevious")
        self.horizontalLayout_13.addWidget(self.pushButton_humanPrevious)
        self.pushButton_humanNext = QtWidgets.QPushButton(self.widget3)
        self.pushButton_humanNext.setObjectName("pushButton_humanNext")
        self.horizontalLayout_13.addWidget(self.pushButton_humanNext)
        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_frame1.setText(_translate("Form", "TextLabel"))
        self.label_12.setText(_translate("Form", "Adjust"))
        self.label_scanID.setText(_translate("Form", "Scan ID:"))
        self.label_8.setText(_translate("Form", "Agent Information"))
        self.label_9.setText(_translate("Form", "Viewpoint ID:"))
        self.label_10.setText(_translate("Form", "Heading Angle:"))
        self.label_11.setText(_translate("Form", "Agent Location:"))
        self.pushButton_agentPrevious.setText(_translate("Form", "Previous"))
        self.pushButton_agentNext.setText(_translate("Form", "Next"))
        self.label_13.setText(_translate("Form", "Human Heading Angle"))
        self.label_14.setText(_translate("Form", "Agent Heading Angle"))
        self.pushButton_save.setText(_translate("Form", "Save"))
        self.label_2.setText(_translate("Form", "Human Information"))
        self.label_3.setText(_translate("Form", "Viewpoint ID:"))
        self.label_5.setText(_translate("Form", "Region:"))
        self.label_6.setText(_translate("Form", "Human Motion:"))
        self.label_7.setText(_translate("Form", "Heading Angle:"))
        self.label_4.setText(_translate("Form", "Human Location:"))
        self.pushButton_humanPrevious.setText(_translate("Form", "Previous"))
        self.pushButton_humanNext.setText(_translate("Form", "Next"))
