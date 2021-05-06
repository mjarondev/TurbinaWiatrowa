# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 993)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1681, 1091))
        self.frame.setMinimumSize(QtCore.QSize(1681, 1091))
        self.frame.setMaximumSize(QtCore.QSize(1681, 1091))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 45);\n"
"    color: rgb(85, 85, 255);\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 300, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 390, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1130, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PowerValue = QtWidgets.QLineEdit(self.frame)
        self.PowerValue.setGeometry(QtCore.QRect(1070, 240, 161, 31))
        self.PowerValue.setStyleSheet("QLineEdit{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(0, 0, 59);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solidrgbrgb(85, 170, 255);\n"
"    background-color: rgb(0, 0, 34);\n"
"}")
        self.PowerValue.setText("")
        self.PowerValue.setReadOnly(True)
        self.PowerValue.setPlaceholderText("")
        self.PowerValue.setObjectName("PowerValue")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(1140, 210, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.RPMValue = QtWidgets.QLineEdit(self.frame)
        self.RPMValue.setGeometry(QtCore.QRect(1070, 310, 161, 31))
        self.RPMValue.setStyleSheet("QLineEdit{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(0, 0, 59);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solidrgbrgb(85, 170, 255);\n"
"    background-color: rgb(0, 0, 34);\n"
"}")
        self.RPMValue.setText("")
        self.RPMValue.setReadOnly(True)
        self.RPMValue.setPlaceholderText("")
        self.RPMValue.setObjectName("RPMValue")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(1080, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.PitchAngleValue = QtWidgets.QLineEdit(self.frame)
        self.PitchAngleValue.setGeometry(QtCore.QRect(1070, 380, 161, 31))
        self.PitchAngleValue.setStyleSheet("QLineEdit{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(0, 0, 59);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solidrgbrgb(85, 170, 255);\n"
"    background-color: rgb(0, 0, 34);\n"
"}")
        self.PitchAngleValue.setText("")
        self.PitchAngleValue.setReadOnly(True)
        self.PitchAngleValue.setPlaceholderText("")
        self.PitchAngleValue.setObjectName("PitchAngleValue")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(1090, 420, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.YawAngleValue = QtWidgets.QLineEdit(self.frame)
        self.YawAngleValue.setGeometry(QtCore.QRect(1070, 450, 161, 31))
        self.YawAngleValue.setStyleSheet("QLineEdit{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(0, 0, 59);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solidrgbrgb(85, 170, 255);\n"
"    background-color: rgb(0, 0, 34);\n"
"}")
        self.YawAngleValue.setText("")
        self.YawAngleValue.setReadOnly(True)
        self.YawAngleValue.setPlaceholderText("")
        self.YawAngleValue.setObjectName("YawAngleValue")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.frame)
        self.openGLWidget.setGeometry(QtCore.QRect(400, 20, 570, 680))
        self.openGLWidget.setObjectName("openGLWidget")
        self.WindSpeedEdit = QtWidgets.QSpinBox(self.frame)
        self.WindSpeedEdit.setGeometry(QtCore.QRect(110, 250, 181, 31))
        self.WindSpeedEdit.setStyleSheet("QSpinBox{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
" \n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}")
        self.WindSpeedEdit.setMaximum(45)
        self.WindSpeedEdit.setObjectName("WindSpeedEdit")
        self.WindAngleHorizontalEdit = QtWidgets.QSpinBox(self.frame)
        self.WindAngleHorizontalEdit.setGeometry(QtCore.QRect(110, 340, 181, 31))
        self.WindAngleHorizontalEdit.setStyleSheet("QSpinBox{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}")
        self.WindAngleHorizontalEdit.setMinimum(-180)
        self.WindAngleHorizontalEdit.setMaximum(180)
        self.WindAngleHorizontalEdit.setObjectName("WindAngleHorizontalEdit")
        self.WindAngleVerticalEdit = QtWidgets.QSpinBox(self.frame)
        self.WindAngleVerticalEdit.setGeometry(QtCore.QRect(110, 430, 181, 31))
        self.WindAngleVerticalEdit.setStyleSheet("QSpinBox{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}")
        self.WindAngleVerticalEdit.setMinimum(-3)
        self.WindAngleVerticalEdit.setMaximum(45)
        self.WindAngleVerticalEdit.setObjectName("WindAngleVerticalEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 480, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color: rgb(85, 85, 255);\n"
"background-color:rgb(0, 0, 34);\n"
"border: none;\n"
"border-left: 1px solid rgb(0, 0, 121);\n"
"border-right: 1px solid rgb(0, 0, 121);\n"
"border-bottom: 5px solid rgb(0, 0, 121)\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 0, 66);\n"
"border-left: 1px solid rgb(0, 0, 121);\n"
"border-right: 1px solid rgb(0, 0, 121);\n"
"border-bottom: 5px solid rgb(0, 0, 121)\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(0, 0, 17);\n"
"border-left: 1px solid rgb(0, 0, 121);\n"
"border-right: 1px solid rgb(0, 0, 121);\n"
"border-bottom: 3px solid rgb(0, 0, 121)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalSlider = QtWidgets.QSlider(self.frame)
        self.verticalSlider.setGeometry(QtCore.QRect(370, 20, 22, 690))
        self.verticalSlider.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: black;\n"
"    border: 0px solid #424242; \n"
"    height: 10px; \n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: red; \n"
"    border: 2px solid red; \n"
"    width: 16px; \n"
"    height: 20px; \n"
"    line-height: 20px; \n"
"    margin-top: -5px; \n"
"    margin-bottom: -5px; \n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"    border-radius: 10px;\n"
"}")
        self.verticalSlider.setMinimum(5)
        self.verticalSlider.setMaximum(85)
        self.verticalSlider.setProperty("value", 60)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.Obrot = QtWidgets.QSlider(self.frame)
        self.Obrot.setGeometry(QtCore.QRect(400, 700, 571, 22))
        self.Obrot.setMinimum(-314)
        self.Obrot.setMaximum(314)
        self.Obrot.setOrientation(QtCore.Qt.Horizontal)
        self.Obrot.setObjectName("Obrot")
        self.PrzodTyl = QtWidgets.QDial(self.frame)
        self.PrzodTyl.setGeometry(QtCore.QRect(1040, 580, 231, 131))
        self.PrzodTyl.setStyleSheet("QDial{\n"
"color: rgb(85, 255, 255);\n"
"}")
        self.PrzodTyl.setMinimum(-80)
        self.PrzodTyl.setMaximum(-5)
        self.PrzodTyl.setProperty("value", -45)
        self.PrzodTyl.setObjectName("PrzodTyl")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(1120, 550, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.RPMplot = QtWidgets.QWidget(self.frame)
        self.RPMplot.setGeometry(QtCore.QRect(340, 720, 320, 250))
        self.RPMplot.setObjectName("RPMplot")
        self.PitchAnglePlot = QtWidgets.QWidget(self.frame)
        self.PitchAnglePlot.setGeometry(QtCore.QRect(670, 720, 320, 250))
        self.PitchAnglePlot.setObjectName("PitchAnglePlot")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(90, 30, 221, 171))
        self.frame_2.setStyleSheet("QFrame{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"color:rgb(0, 0, 121);\n"
"background-color:rgb(0, 0, 121)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(20, 0, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"color:rgb(0, 0, 231)\n"
"}")
        self.label_9.setObjectName("label_9")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.frame_2)
        self.openGLWidget_2.setGeometry(QtCore.QRect(10, 30, 201, 131))
        self.openGLWidget_2.setStyleSheet("")
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1120, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.HamulecValue = QtWidgets.QLineEdit(self.frame)
        self.HamulecValue.setGeometry(QtCore.QRect(1070, 170, 161, 31))
        self.HamulecValue.setStyleSheet("QLineEdit{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(0, 0, 59);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solidrgbrgb(85, 170, 255);\n"
"    background-color: rgb(0, 0, 34);\n"
"}")
        self.HamulecValue.setText("")
        self.HamulecValue.setReadOnly(True)
        self.HamulecValue.setPlaceholderText("")
        self.HamulecValue.setObjectName("HamulecValue")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 720, 320, 250))
        self.widget.setObjectName("widget")
        self.YawAnglePlot = QtWidgets.QWidget(self.frame)
        self.YawAnglePlot.setGeometry(QtCore.QRect(1000, 720, 320, 250))
        self.YawAnglePlot.setObjectName("YawAnglePlot")
        self.NapisWarning = QtWidgets.QLabel(self.frame)
        self.NapisWarning.setGeometry(QtCore.QRect(1050, 30, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.NapisWarning.setFont(font)
        self.NapisWarning.setObjectName("NapisWarning")
        self.lampkaWarning = QtWidgets.QFrame(self.frame)
        self.lampkaWarning.setGeometry(QtCore.QRect(1020, 30, 21, 21))
        self.lampkaWarning.setStyleSheet("QFrame{\n"
"\n"
"border-radius:10px;\n"
"background-color:rgb(255, 0, 0);\n"
"\n"
"}")
        self.lampkaWarning.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lampkaWarning.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lampkaWarning.setObjectName("lampkaWarning")
        self.InfoWarning = QtWidgets.QLineEdit(self.frame)
        self.InfoWarning.setGeometry(QtCore.QRect(1030, 70, 261, 61))
        self.InfoWarning.setStyleSheet("QLineEdit{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(0, 0, 59);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solidrgbrgb(85, 170, 255);\n"
"    background-color: rgb(0, 0, 34);\n"
"}")
        self.InfoWarning.setText("")
        self.InfoWarning.setReadOnly(True)
        self.InfoWarning.setPlaceholderText("")
        self.InfoWarning.setObjectName("InfoWarning")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(130, 960, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(480, 960, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(770, 960, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(1100, 960, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.FrontWindValue = QtWidgets.QLineEdit(self.frame)
        self.FrontWindValue.setGeometry(QtCore.QRect(1070, 520, 161, 31))
        self.FrontWindValue.setStyleSheet("QLineEdit{\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"border: 1px solid rgb(0, 0, 121);\n"
"\n"
"color: #FFF;\n"
"background-color: rgb(0, 0, 34);\n"
"padding-left: 20 px ;\n"
"padding - right: 20 px ;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(0, 0, 59);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solidrgbrgb(85, 170, 255);\n"
"    background-color: rgb(0, 0, 34);\n"
"}")
        self.FrontWindValue.setText("")
        self.FrontWindValue.setReadOnly(True)
        self.FrontWindValue.setPlaceholderText("")
        self.FrontWindValue.setObjectName("FrontWindValue")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(1040, 490, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WIND ANGLE(YAW):"))
        self.label_2.setText(_translate("MainWindow", "WIND SPEED:"))
        self.label_3.setText(_translate("MainWindow", "WIND ANGLE(PITCH):"))
        self.label_4.setText(_translate("MainWindow", "RPM:"))
        self.label_5.setText(_translate("MainWindow", "P :"))
        self.label_6.setText(_translate("MainWindow", "PITCH ANGLE:"))
        self.label_7.setText(_translate("MainWindow", "YAW ANGLE:"))
        self.pushButton_2.setText(_translate("MainWindow", "CHANGE WIND"))
        self.label_8.setText(_translate("MainWindow", "ZOOM:"))
        self.label_9.setText(_translate("MainWindow", "WIND DIRECTION:"))
        self.label_10.setText(_translate("MainWindow", "BRAKE:"))
        self.NapisWarning.setText(_translate("MainWindow", "WARNING:"))
        self.label_12.setText(_translate("MainWindow", "POWER"))
        self.label_13.setText(_translate("MainWindow", "RPM"))
        self.label_14.setText(_translate("MainWindow", "PITCH ANGLE"))
        self.label_15.setText(_translate("MainWindow", "YAW ANGLE"))
        self.label_16.setText(_translate("MainWindow", "ACTUAL FRONT WIND:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

