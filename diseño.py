# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diseño_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setPointSize(5)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signal_1 = QtWidgets.QWidget(self.centralwidget)
        self.signal_1.setGeometry(QtCore.QRect(300, 60, 600, 200))
        self.signal_1.setObjectName("signal_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.signal_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_signal_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_signal_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_signal_1.setObjectName("verticalLayout_signal_1")
        self.signal_2 = QtWidgets.QWidget(self.centralwidget)
        self.signal_2.setGeometry(QtCore.QRect(300, 260, 600, 200))
        self.signal_2.setObjectName("signal_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.signal_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 591, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_signal_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_signal_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_signal_2.setObjectName("verticalLayout_signal_2")
        self.pushButton_pc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pc.setGeometry(QtCore.QRect(970, 90, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_pc.setFont(font)
        self.pushButton_pc.setObjectName("pushButton_pc")
        self.signal_3 = QtWidgets.QWidget(self.centralwidget)
        self.signal_3.setGeometry(QtCore.QRect(300, 460, 600, 200))
        self.signal_3.setObjectName("signal_3")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.signal_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 591, 191))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_signal_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_signal_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_signal_3.setObjectName("verticalLayout_signal_3")
        self.pushButton__vc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__vc.setGeometry(QtCore.QRect(970, 310, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton__vc.setFont(font)
        self.pushButton__vc.setObjectName("pushButton__vc")
        self.pushButton_frecuencia_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_frecuencia_up.setGeometry(QtCore.QRect(950, 600, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_frecuencia_up.setFont(font)
        self.pushButton_frecuencia_up.setObjectName("pushButton_frecuencia_up")
        self.pushButton_frecuencia_down = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_frecuencia_down.setGeometry(QtCore.QRect(950, 670, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_frecuencia_down.setFont(font)
        self.pushButton_frecuencia_down.setObjectName("pushButton_frecuencia_down")
        self.lcdNumber_presion = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_presion.setGeometry(QtCore.QRect(110, 60, 180, 100))
        self.lcdNumber_presion.setObjectName("lcdNumber_presion")
        self.lcdNumber_flujo = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_flujo.setGeometry(QtCore.QRect(110, 260, 180, 100))
        self.lcdNumber_flujo.setObjectName("lcdNumber_flujo")
        self.lcdNumber_volumen = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_volumen.setGeometry(QtCore.QRect(110, 460, 180, 100))
        self.lcdNumber_volumen.setObjectName("lcdNumber_volumen")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 190, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 390, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 560, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 590, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lcdNumber_frecuencia = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_frecuencia.setGeometry(QtCore.QRect(960, 490, 180, 100))
        self.lcdNumber_frecuencia.setObjectName("lcdNumber_frecuencia")
        self.pushButton_conectar_serial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conectar_serial.setGeometry(QtCore.QRect(20, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_conectar_serial.setFont(font)
        self.pushButton_conectar_serial.setObjectName("pushButton_conectar_serial")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 710, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_desconectar_serial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_desconectar_serial.setGeometry(QtCore.QRect(330, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_desconectar_serial.setFont(font)
        self.pushButton_desconectar_serial.setObjectName("pushButton_desconectar_serial")
        self.pushButton_sincronizar_datos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sincronizar_datos.setGeometry(QtCore.QRect(20, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_sincronizar_datos.setFont(font)
        self.pushButton_sincronizar_datos.setObjectName("pushButton_sincronizar_datos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 16))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_pc.setText(_translate("MainWindow", "PC"))
        self.pushButton__vc.setText(_translate("MainWindow", "VC"))
        self.pushButton_frecuencia_up.setText(_translate("MainWindow", "AUMENTAR FRECUENCIA"))
        self.pushButton_frecuencia_down.setText(_translate("MainWindow", "DISMINUIR FRECUENCIA"))
        self.label.setText(_translate("MainWindow", "Ppico"))
        self.label_2.setText(_translate("MainWindow", "cmH2O"))
        self.label_3.setText(_translate("MainWindow", "l/min"))
        self.label_4.setText(_translate("MainWindow", "VolMinEsp"))
        self.label_5.setText(_translate("MainWindow", "fTotal"))
        self.label_6.setText(_translate("MainWindow", "c/min"))
        self.pushButton_conectar_serial.setText(_translate("MainWindow", "CONECTAR"))
        self.comboBox.setItemText(0, _translate("MainWindow", "PUERTO"))
        self.comboBox.setItemText(1, _translate("MainWindow", "COM1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "COM2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "COM3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "COM4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "COM5"))
        self.pushButton_desconectar_serial.setText(_translate("MainWindow", "DESCONECTAR"))
        self.pushButton_sincronizar_datos.setText(_translate("MainWindow", "PLOTER ON"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
