# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diseño_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(5)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signal_1 = QtWidgets.QWidget(self.centralwidget)
        self.signal_1.setGeometry(QtCore.QRect(269, 60, 631, 200))
        self.signal_1.setObjectName("signal_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.signal_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_signal_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_signal_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_signal_1.setObjectName("verticalLayout_signal_1")
        self.signal_2 = QtWidgets.QWidget(self.centralwidget)
        self.signal_2.setGeometry(QtCore.QRect(269, 260, 631, 200))
        self.signal_2.setObjectName("signal_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.signal_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 631, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_signal_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_signal_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_signal_2.setObjectName("verticalLayout_signal_2")
        self.pushButton_pc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pc.setGeometry(QtCore.QRect(1060, 60, 120, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_pc.setFont(font)
        self.pushButton_pc.setObjectName("pushButton_pc")
        self.signal_3 = QtWidgets.QWidget(self.centralwidget)
        self.signal_3.setGeometry(QtCore.QRect(269, 460, 631, 200))
        self.signal_3.setObjectName("signal_3")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.signal_3)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 631, 191))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_signal_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_signal_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_signal_3.setObjectName("verticalLayout_signal_3")
        self.pushButton_vc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vc.setGeometry(QtCore.QRect(920, 60, 120, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_vc.setFont(font)
        self.pushButton_vc.setObjectName("pushButton_vc")
        self.pushButton_frecuencia_up = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_frecuencia_up.setGeometry(QtCore.QRect(1050, 340, 53, 53))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_frecuencia_up.setFont(font)
        self.pushButton_frecuencia_up.setStyleSheet("#pushButton_frecuencia_up\n"
"{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (1).png);\n"
"}\n"
"#pushButton_frecuencia_up:hover\n"
"{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (2).png);\n"
"}")
        self.pushButton_frecuencia_up.setText("")
        self.pushButton_frecuencia_up.setObjectName("pushButton_frecuencia_up")
        self.pushButton_frecuencia_down = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_frecuencia_down.setGeometry(QtCore.QRect(1120, 340, 53, 53))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_frecuencia_down.setFont(font)
        self.pushButton_frecuencia_down.setStyleSheet("#pushButton_frecuencia_down{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill.png);\n"
"}\n"
"#pushButton_frecuencia_down:hover{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (3).png);\n"
"}\n"
"")
        self.pushButton_frecuencia_down.setText("")
        self.pushButton_frecuencia_down.setObjectName("pushButton_frecuencia_down")
        self.lcdNumber_presion = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_presion.setGeometry(QtCore.QRect(69, 60, 181, 100))
        self.lcdNumber_presion.setObjectName("lcdNumber_presion")
        self.lcdNumber_flujo = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_flujo.setGeometry(QtCore.QRect(70, 260, 180, 100))
        self.lcdNumber_flujo.setObjectName("lcdNumber_flujo")
        self.lcdNumber_volumen = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_volumen.setGeometry(QtCore.QRect(70, 460, 180, 100))
        self.lcdNumber_volumen.setObjectName("lcdNumber_volumen")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 190, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 560, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 590, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lcdNumber_frecuencia = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_frecuencia.setGeometry(QtCore.QRect(920, 340, 121, 51))
        self.lcdNumber_frecuencia.setStyleSheet("#lcdNumber_frecuencia{\n"
"\n"
"border: 2px solid rgb(72, 72, 72);\n"
"\n"
"\n"
"}\n"
"#lcdNumber_frecuencia:hover{\n"
"\n"
"border: 2px solid  rgb(190, 190, 190);\n"
"\n"
"}\n"
"")
        self.lcdNumber_frecuencia.setObjectName("lcdNumber_frecuencia")
        self.pushButton_conectar_serial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conectar_serial.setGeometry(QtCore.QRect(20, 710, 141, 41))
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
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_desconectar_serial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_desconectar_serial.setGeometry(QtCore.QRect(330, 710, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_desconectar_serial.setFont(font)
        self.pushButton_desconectar_serial.setObjectName("pushButton_desconectar_serial")
        self.lcdNumber_peep = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_peep.setGeometry(QtCore.QRect(920, 455, 121, 51))
        self.lcdNumber_peep.setStyleSheet("#lcdNumber_peep{\n"
"\n"
"border: 2px solid rgb(72, 72, 72);\n"
"\n"
"\n"
"}\n"
"#lcdNumber_peep:hover{\n"
"\n"
"border: 2px solid  rgb(190, 190, 190);\n"
"\n"
"}\n"
"")
        self.lcdNumber_peep.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_peep.setObjectName("lcdNumber_peep")
        self.pushButton_incrementar_peep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_incrementar_peep.setGeometry(QtCore.QRect(1050, 455, 53, 53))
        self.pushButton_incrementar_peep.setStyleSheet("#pushButton_incrementar_peep\n"
"{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (1).png);\n"
"}\n"
"#pushButton_incrementar_peep:hover\n"
"{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (2).png);\n"
"}")
        self.pushButton_incrementar_peep.setText("")
        self.pushButton_incrementar_peep.setObjectName("pushButton_incrementar_peep")
        self.pushButton_decrementar_peep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrementar_peep.setGeometry(QtCore.QRect(1120, 455, 53, 53))
        self.pushButton_decrementar_peep.setStyleSheet("#pushButton_decrementar_peep{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill.png);\n"
"}\n"
"#pushButton_decrementar_peep:hover{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (3).png);\n"
"}\n"
"")
        self.pushButton_decrementar_peep.setText("")
        self.pushButton_decrementar_peep.setObjectName("pushButton_decrementar_peep")
        self.pushButton_confirmar_peep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirmar_peep.setGeometry(QtCore.QRect(1050, 525, 122, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_confirmar_peep.setFont(font)
        self.pushButton_confirmar_peep.setStyleSheet("#pushButton_confirmar_peep{\n"
"\n"
"}\n"
"#pushButton_confirmar_peep:hover{\n"
"color: rgb(170, 255, 255);\n"
"}")
        self.pushButton_confirmar_peep.setObjectName("pushButton_confirmar_peep")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(920, 510, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 220, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_peep_actual = QtWidgets.QLabel(self.centralwidget)
        self.label_peep_actual.setGeometry(QtCore.QRect(100, 220, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_peep_actual.setFont(font)
        self.label_peep_actual.setText("")
        self.label_peep_actual.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_peep_actual.setObjectName("label_peep_actual")
        self.pushButton_encender_vm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_encender_vm.setGeometry(QtCore.QRect(530, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_encender_vm.setFont(font)
        self.pushButton_encender_vm.setStyleSheet("#pushButton_encender_vm{\n"
"background: #0FC62C;\n"
"border: 2px solid #000000;}\n"
"\n"
"#pushButton_encender_vm:hover\n"
"{\n"
"background-color: rgb(78, 234, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_encender_vm.setObjectName("pushButton_encender_vm")
        self.pushButton_apagar_vm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_apagar_vm.setGeometry(QtCore.QRect(680, 710, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_apagar_vm.setFont(font)
        self.pushButton_apagar_vm.setStyleSheet("#pushButton_apagar_vm{\n"
"background: #F13535;\n"
"border: 2px solid #000000;}\n"
"\n"
"#pushButton_apagar_vm:hover\n"
"{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_apagar_vm.setObjectName("pushButton_apagar_vm")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(920, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lcdNumber_volumen_entrada = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_volumen_entrada.setGeometry(QtCore.QRect(920, 230, 121, 51))
        self.lcdNumber_volumen_entrada.setStyleSheet("#lcdNumber_volumen_entrada{\n"
"\n"
"border: 2px solid rgb(72, 72, 72);\n"
"\n"
"\n"
"}\n"
"#lcdNumber_volumen_entrada:hover{\n"
"\n"
"border: 2px solid  rgb(190, 190, 190);\n"
"\n"
"}\n"
"")
        self.lcdNumber_volumen_entrada.setObjectName("lcdNumber_volumen_entrada")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(920, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_decrementar_volumen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decrementar_volumen.setGeometry(QtCore.QRect(1120, 230, 53, 53))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_decrementar_volumen.setFont(font)
        self.pushButton_decrementar_volumen.setStyleSheet("#pushButton_decrementar_volumen{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill.png);\n"
"}\n"
"#pushButton_decrementar_volumen:hover{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (3).png);\n"
"}\n"
"")
        self.pushButton_decrementar_volumen.setText("")
        self.pushButton_decrementar_volumen.setObjectName("pushButton_decrementar_volumen")
        self.pushButton_incrementar_volumen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_incrementar_volumen.setGeometry(QtCore.QRect(1050, 230, 53, 53))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_incrementar_volumen.setFont(font)
        self.pushButton_incrementar_volumen.setStyleSheet("#pushButton_incrementar_volumen\n"
"{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (1).png);\n"
"}\n"
"#pushButton_incrementar_volumen:hover\n"
"{\n"
"background-image: url(:/design/iconos/akar-icons_circle-chevron-down-fill (2).png);\n"
"}")
        self.pushButton_incrementar_volumen.setText("")
        self.pushButton_incrementar_volumen.setObjectName("pushButton_incrementar_volumen")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_modo = QtWidgets.QLabel(self.centralwidget)
        self.label_modo.setGeometry(QtCore.QRect(470, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_modo.setFont(font)
        self.label_modo.setStyleSheet("#label_modo{\n"
"font: 16pt \"Montserrat\";\n"
"border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.label_modo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modo.setObjectName("label_modo")
        self.led_vc_on = QtWidgets.QFrame(self.centralwidget)
        self.led_vc_on.setGeometry(QtCore.QRect(950, 110, 53, 53))
        self.led_vc_on.setStyleSheet("#led_vc_on{\n"
"background-image: url(:/design/iconos/mdi_led-on.png);\n"
"}")
        self.led_vc_on.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.led_vc_on.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_vc_on.setObjectName("led_vc_on")
        self.led_pc_on = QtWidgets.QFrame(self.centralwidget)
        self.led_pc_on.setGeometry(QtCore.QRect(1090, 110, 53, 53))
        self.led_pc_on.setStyleSheet("#led_pc_on{\n"
"background-image: url(:/design/iconos/mdi_led-on.png);\n"
"}")
        self.led_pc_on.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.led_pc_on.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_pc_on.setObjectName("led_pc_on")
        self.led_vc_off = QtWidgets.QFrame(self.centralwidget)
        self.led_vc_off.setGeometry(QtCore.QRect(950, 110, 53, 53))
        self.led_vc_off.setStyleSheet("#led_vc_off\n"
"{\n"
"background-image: url(:/design/iconos/Vector.png);\n"
"}")
        self.led_vc_off.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.led_vc_off.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_vc_off.setObjectName("led_vc_off")
        self.led_pc_off = QtWidgets.QFrame(self.centralwidget)
        self.led_pc_off.setGeometry(QtCore.QRect(1090, 110, 53, 53))
        self.led_pc_off.setStyleSheet("#led_pc_off{\n"
"background-image: url(:/design/iconos/Vector.png);\n"
"}")
        self.led_pc_off.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.led_pc_off.setFrameShadow(QtWidgets.QFrame.Raised)
        self.led_pc_off.setObjectName("led_pc_off")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_pc.setText(_translate("MainWindow", "PC"))
        self.pushButton_vc.setText(_translate("MainWindow", "VC"))
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
        self.pushButton_confirmar_peep.setText(_translate("MainWindow", "CONFIRMAR PEEP"))
        self.label_8.setText(_translate("MainWindow", "PEEP "))
        self.label_7.setText(_translate("MainWindow", "PEEP"))
        self.pushButton_encender_vm.setText(_translate("MainWindow", "ENCENDIDO"))
        self.pushButton_apagar_vm.setText(_translate("MainWindow", "APAGADO"))
        self.label_9.setText(_translate("MainWindow", "FR "))
        self.label_10.setText(_translate("MainWindow", "l/min"))
        self.label_11.setText(_translate("MainWindow", "MODO"))
        self.label_modo.setText(_translate("MainWindow", "VOLUMEN CONTROL"))

import diseño_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

