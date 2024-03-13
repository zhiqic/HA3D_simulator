# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1046, 777)
        self.pointView_widget = QVideoWidget(Form)
        self.pointView_widget.setGeometry(QtCore.QRect(10, 10, 1024, 256))
        self.pointView_widget.setObjectName("pointView_widget")
        self.Image_label = QtWidgets.QLabel(self.pointView_widget)
        self.Image_label.setGeometry(QtCore.QRect(0, 0, 1024, 256))
        self.Image_label.setObjectName("Image_label")
        self.chart_1 = QChart()
        self.chart_view = QChartView(self.chart_1, Form)
        self.chart_view.setGeometry(QtCore.QRect(10, 270, 651, 500))
        self.chart_view.setObjectName("chart_1")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(670, 270, 368, 501))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ScanID_label = QtWidgets.QLabel(self.widget)
        self.ScanID_label.setObjectName("ScanID_label")
        self.horizontalLayout.addWidget(self.ScanID_label)
        self.ScanID_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.ScanID_textBrowser.setObjectName("ScanID_textBrowser")
        self.horizontalLayout.addWidget(self.ScanID_textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PathID_label = QtWidgets.QLabel(self.widget)
        self.PathID_label.setObjectName("PathID_label")
        self.horizontalLayout_2.addWidget(self.PathID_label)
        self.PathID_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.PathID_textBrowser.setObjectName("PathID_textBrowser")
        self.horizontalLayout_2.addWidget(self.PathID_textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Distance_label = QtWidgets.QLabel(self.widget)
        self.Distance_label.setObjectName("Distance_label")
        self.horizontalLayout_3.addWidget(self.Distance_label)
        self.Distance_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.Distance_textBrowser.setObjectName("Distance_textBrowser")
        self.horizontalLayout_3.addWidget(self.Distance_textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Heading_label = QtWidgets.QLabel(self.widget)
        self.Heading_label.setObjectName("Heading_label")
        self.horizontalLayout_4.addWidget(self.Heading_label)
        self.Heading_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.Heading_textBrowser.setObjectName("Heading_textBrowser")
        self.horizontalLayout_4.addWidget(self.Heading_textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Instruction1_label = QtWidgets.QLabel(self.widget)
        self.Instruction1_label.setObjectName("Instruction1_label")
        self.horizontalLayout_5.addWidget(self.Instruction1_label)
        self.Instruction1_textEdit = QtWidgets.QTextEdit(self.widget)
        self.Instruction1_textEdit.setObjectName("Instruction1_textEdit")
        self.horizontalLayout_5.addWidget(self.Instruction1_textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Instruction2_label = QtWidgets.QLabel(self.widget)
        self.Instruction2_label.setObjectName("Instruction2_label")
        self.horizontalLayout_6.addWidget(self.Instruction2_label)
        self.Instruction2_textEdit = QtWidgets.QTextEdit(self.widget)
        self.Instruction2_textEdit.setObjectName("Instruction2_textEdit")
        self.horizontalLayout_6.addWidget(self.Instruction2_textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Instruction3_label = QtWidgets.QLabel(self.widget)
        self.Instruction3_label.setObjectName("Instruction3_label")
        self.horizontalLayout_7.addWidget(self.Instruction3_label)
        self.Instruction3_textEdit = QtWidgets.QTextEdit(self.widget)
        self.Instruction3_textEdit.setObjectName("Instruction3_textEdit")
        self.horizontalLayout_7.addWidget(self.Instruction3_textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ViewpointID_label = QtWidgets.QLabel(self.widget)
        self.ViewpointID_label.setObjectName("ViewpointID_label")
        self.horizontalLayout_8.addWidget(self.ViewpointID_label)
        self.ViewpointID_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.ViewpointID_textBrowser.setObjectName("ViewpointID_textBrowser")
        self.horizontalLayout_8.addWidget(self.ViewpointID_textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Previous_pushButton = QtWidgets.QPushButton(self.widget)
        self.Previous_pushButton.setObjectName("Previous_pushButton")
        self.horizontalLayout_9.addWidget(self.Previous_pushButton)
        self.Next_pushButton = QtWidgets.QPushButton(self.widget)
        self.Next_pushButton.setObjectName("Next_pushButton")
        self.horizontalLayout_9.addWidget(self.Next_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.Insert_pushButton = QtWidgets.QPushButton(self.widget)
        self.Insert_pushButton.setObjectName("Insert_pushButton")
        self.verticalLayout.addWidget(self.Insert_pushButton)
        self.Delete_pushButton = QtWidgets.QPushButton(self.widget)
        self.Delete_pushButton.setObjectName("Delete_pushButton")
        self.verticalLayout.addWidget(self.Delete_pushButton)
        self.Save_pushButton = QtWidgets.QPushButton(self.widget)
        self.Save_pushButton.setObjectName("Save_pushButton")
        self.verticalLayout.addWidget(self.Save_pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Image_label.setText(_translate("Form", "ImageLabel"))
        self.ScanID_label.setText(_translate("Form", "Scan ID:"))
        self.PathID_label.setText(_translate("Form", "Path ID:"))
        self.Distance_label.setText(_translate("Form", "Distance:"))
        self.Heading_label.setText(_translate("Form", "Heading:"))
        self.Instruction1_label.setText(_translate("Form", "Instruction 1:"))
        self.Instruction2_label.setText(_translate("Form", "Instruction 2:"))
        self.Instruction3_label.setText(_translate("Form", "Instruction 3:"))
        self.ViewpointID_label.setText(_translate("Form", "Viewpoint ID:"))
        self.Previous_pushButton.setText(_translate("Form", "Previous Path"))
        self.Next_pushButton.setText(_translate("Form", "Next Path"))
        self.Insert_pushButton.setText(_translate("Form", "Insert"))
        self.Delete_pushButton.setText(_translate("Form", "Delete"))
        self.Save_pushButton.setText(_translate("Form", "SAVE"))
from PyQt5.QtChart import QChart, QChartView
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
