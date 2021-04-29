
# -*- coding: utf-8 -*-
from os import path, environ

from PyQt5 import QtCore, QtWidgets
import GLWidget
from wiatrak import obliczMoc
from gui import Ui_MainWindow
import strzalka

#plot
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot



class MyMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)


        self.windSpeed = 0.0
        self.windAnglePitch = 0.0
        self.windAngleYaw = 0.0

        self.power = 0.0
        self.RPM = 0.0
        self.pitchAngle = 0.0
        self.yawAngle = 0.0
        self.hamulec = 0.0

        #plot
        self.yDataPower = [0]*50
        self.yDataRPM = [0]*50
        self.yDataYaw = [0]*50
        self.yDataPitch = [0]*50
        self.xData = [i for i in range(50)]
        self.plotRefPower = None
        self.plotRefRPM = None
        self.plotRefYaw = None
        self.plotRefPitch = None

        self.figurePower = matplotlib.pyplot.figure()
        self.canvasPower = FigureCanvasQTAgg(self.figurePower)
        layoutPower = QtWidgets.QVBoxLayout()
        layoutPower.addWidget(self.canvasPower)
        self.widget.setLayout(layoutPower)

        self.figureRPM = matplotlib.pyplot.figure()
        self.canvasRPM = FigureCanvasQTAgg(self.figureRPM)
        layoutRPM = QtWidgets.QVBoxLayout()
        layoutRPM.addWidget(self.canvasRPM)
        self.RPMplot.setLayout(layoutRPM)

        self.figurePitch = matplotlib.pyplot.figure()
        self.canvasPitch = FigureCanvasQTAgg(self.figurePitch)
        layoutPitch = QtWidgets.QVBoxLayout()
        layoutPitch.addWidget(self.canvasPitch)
        self.PitchAnglePlot.setLayout(layoutPitch)

        self.figureYaw = matplotlib.pyplot.figure()
        self.canvasYaw = FigureCanvasQTAgg(self.figureYaw)
        layoutYaw = QtWidgets.QVBoxLayout()
        layoutYaw.addWidget(self.canvasYaw)
        self.YawAnglePlot.setLayout(layoutYaw)

        #others
        glWidth = 570
        glHeight = 690
        self.openGLWidget = GLWidget.GLWidget(glWidth, glHeight, self.frame)
        self.openGLWidget.setGeometry(QtCore.QRect(400, 20, glWidth, glHeight))
        self.openGLWidget.setObjectName("openGLWidget")

        strzalkaWidth = 201
        strzalkaHeight = 131
        self.openGLWidget_2 = strzalka.GLWidget(strzalkaWidth, strzalkaHeight, self.frame_2)
        self.openGLWidget_2.setGeometry(QtCore.QRect(10, 30, strzalkaWidth, strzalkaHeight))
        self.openGLWidget.setObjectName("strzalka")

        self.pushButton_2.clicked.connect(self.startClicked)
        self.verticalSlider.valueChanged.connect(self.sliderChanged)
        self.Obrot.valueChanged.connect(self.sliderChanged)
        self.PrzodTyl.valueChanged.connect(self.sliderChanged)

        timer = QtCore.QTimer(self.centralwidget)
        timer.setInterval(20)  # period in milliseconds
        timer.timeout.connect(self.openGLWidget.updateRot)
        timer.timeout.connect(self.openGLWidget.updateGL)
        timer.timeout.connect(self.obliczenia)

        timer2 = QtCore.QTimer(self.centralwidget)
        timer2.setInterval(1000)
        timer2.timeout.connect(self.plotPower)
        timer2.timeout.connect(self.plotRPM)
        timer2.timeout.connect(self.plotYaw)
        timer2.timeout.connect(self.plotPitch)

        timer.start()
        timer2.start()



    #plot
    def plotPitch(self):
        self.yDataPitch = self.yDataPitch[1:] + [self.pitchAngle]

        if self.plotRefPitch is None:
            self.figurePitch.clear()
            ax = self.figurePitch.add_subplot(111)
            ax.set_ylim([-3, 45])
            plotRefs = ax.plot(self.xData, self.yDataPitch, '-')
            self.plotRefPitch = plotRefs[0]
        else:
            self.plotRefPitch.set_ydata(self.yDataPitch)
        self.canvasPitch.draw()

    def plotYaw(self):
        self.yDataYaw = self.yDataYaw[1:] + [self.yawAngle]

        if self.plotRefYaw is None:
            self.figureYaw.clear()
            ax = self.figureYaw.add_subplot(111)
            ax.set_ylim([-180, 180])
            plotRefs = ax.plot(self.xData, self.yDataYaw, '-')
            self.plotRefYaw = plotRefs[0]
        else:
            self.plotRefYaw.set_ydata(self.yDataYaw)
        self.canvasYaw.draw()

    def plotRPM(self):
        self.yDataRPM = self.yDataRPM[1:] + [self.RPM]

        if self.plotRefRPM is None:
            self.figureRPM.clear()
            ax = self.figureRPM.add_subplot(111)
            ax.set_ylim([0, 17])
            plotRefs = ax.plot(self.xData, self.yDataRPM, '-')
            self.plotRefRPM = plotRefs[0]
        else:
            self.plotRefRPM.set_ydata(self.yDataRPM)
        self.canvasRPM.draw()

    def plotPower(self):
        self.yDataPower = self.yDataPower[1:] + [self.power]

        if self.plotRefPower is None:
            self.figurePower.clear()
            ax = self.figurePower.add_subplot(111)
            ax.set_ylim([0, 2.5])
            plotRefs = ax.plot(self.xData, self.yDataPower, '-')
            self.plotRefPower = plotRefs[0]
        else:
            self.plotRefPower.set_ydata(self.yDataPower)
        self.canvasPower.draw()


    def sliderChanged(self):
        self.openGLWidget.setView(-self.PrzodTyl.value(), self.Obrot.value(), self.verticalSlider.value())

    def startClicked(self):
        self.windSpeed = float(self.WindSpeedEdit.text())
        self.windAngleYaw = float(self.WindAngleHorizontalEdit.text())
        self.windAnglePitch = float(self.WindAngleVerticalEdit.text())

        self.openGLWidget_2.setYawAngle(self.windAngleYaw)
        self.openGLWidget_2.updateGL()

    def obliczenia(self):

        tab = obliczMoc(self.windSpeed, self.windAnglePitch, self.windAngleYaw)
        # przyjmuje predkoscWiatru, katPitchWiatru, katYawWiatru
        # zwraca tablice o rozmiarze 6
        # [P, RPM, CzolowaPredkoscWiatru, KatPitchWzgledemPunktuStartowego, KatYawWzgledemPunktuStartowego, procentHamulec]

        self.openGLWidget.setRot(tab[1], tab[4], tab[3])

        self.power = round(tab[0]/1000000, 2)
        self.RPM = round(tab[1], 2)
        self.pitchAngle = round(tab[3], 2)
        self.yawAngle = round(tab[4], 2)
        self.hamulec = round(tab[5], 2)


        self.PowerValue.setText(str(self.power)+"MW")
        self.RPMValue.setText(str(self.RPM)+"rpm")
        self.PitchAngleValue.setText(str(self.pitchAngle)+u"\N{DEGREE SIGN}")
        self.YawAngleValue.setText(str(self.yawAngle)+u"\N{DEGREE SIGN}")
        self.HamulecValue.setText(str(self.hamulec)+"%")
        self.FrontWindValue.setText(str(round(tab[2], 2)) + "m/s")

        if tab[2] < 2:
            self.lampkaWarning.setStyleSheet("""QFrame{
            border-radius:10px;
            background-color:rgb(255, 255, 0);
            }""")
            self.InfoWarning.setText("Wind speed too low")
            self.lampkaWarning.setVisible(True)
            self.InfoWarning.setVisible(True)
            self.NapisWarning.setVisible(True)
        elif tab[2] > 25:
            self.lampkaWarning.setStyleSheet("""QFrame{
                        border-radius:10px;
                        background-color:rgb(255, 0, 0);
                        }""")
            self.InfoWarning.setText("Breaks engaged. Wind speed too high.")
            self.lampkaWarning.setVisible(True)
            self.InfoWarning.setVisible(True)
            self.NapisWarning.setVisible(True)
        else:
            self.lampkaWarning.setVisible(False)
            self.InfoWarning.setVisible(False)
            self.NapisWarning.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
