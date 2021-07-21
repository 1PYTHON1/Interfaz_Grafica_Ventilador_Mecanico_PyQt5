####### Diseño de Interfaz Grafica BY Jose ID ####

# Importamos las libreria

from diseño import *  # importamos el modulo de nuestro diseño en PyQt5
import serial  # Importamos serial para la comunicacion serial con arduino
import numpy as np  # Importamos numpy para manejar matrices de nuestros datos obtenidas de arduino
import qdarkstyle  # Para darle un estilo oscuro a nuestra interfaz graficas diseñada en PyQt5
import puerto_serial  # PARA ENVIAR Y RECIBIR DATOS DEL PUERTO SERIE
import signal_from_arduino  as signal_arduino
import variables_globales

if QtCore.qVersion() >= "5.":
	from matplotlib.backends.backend_qt5agg import (
		FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
# fin de la importacion de dependencias


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

		self.setupUi(self)
		#variables del ventana principal
		self.pase_on = 0  # condicionara que se debe conectar el puerto serie primero
		self.frecuencia_lcd = 15 # setea la frecuencia de inicio
		
		variables_globales.set_valor_frecuencia(self.frecuencia_lcd) #### escala frecuencia

		self.volumen_controlado = 480  # valor de ingreso para volumen control
		self.presion_controlado = 25  # valor de ingreso para presion control 
		variables_globales.set_valor_presion_control(self.presion_controlado)
		self.lcdNumber_presion_entrada.display(self.presion_controlado)
		self.frame_warning_presion.close()
		self.lcdNumber_volumen.display(self.volumen_controlado)
		self.lcdNumber_volumen_entrada.display(self.volumen_controlado)
		variables_globales.set_valor_volumen_control(self.volumen_controlado)
		# variables globales 
		self.posicion_com  = 0  # Posicion Index del combobox, COM del serial
		self.com_seleccionado = 0  # Puerto COM seleccionado start
		self.dato_lcd_peep = 5  # Comienza con el valor de PEEP en 5
		self.dato_lcd_peep_confirmado = 5  # Variable de confirmacion del PEEP comienza en 5
		self.sistema_activado = 0  # Toma dos valores verdadero o falso
		self.modo_de_control = "volumen_control"  # Guardamos el Modo de Control por default VC
		self.label_peep_actual.setText(str(self.dato_lcd_peep_confirmado))  # Setea la etiqueta con el valor de PEEP 
		self.lcdNumber_peep.display(self.dato_lcd_peep)  # Mostrara el VALOR de PEEP inicial que es 5
		variables_globales.set_dato_peep(self.dato_lcd_peep)
		################################

		#### se crean eventos para todos los botones de la interfaz Grafica ###
		self.lcdNumber_frecuencia.display(self.frecuencia_lcd)
		self.lcdNumber_flujo.display(self.frecuencia_lcd)
		self.setWindowTitle("INTERFAZ GRAFICA VENTILADOR MECANICO")
		self.mensaje = QtWidgets.QMessageBox(self)
		self.pushButton_desconectar_serial.clicked.connect(self.desconectar_puerto)
		self.pushButton_conectar_serial.clicked.connect(self.conectar_puerto)
		self.pushButton_frecuencia_up.clicked.connect(self.incrementar_frecuencia)
		self.pushButton_frecuencia_down.clicked.connect(self.decrementar_frecuencia)
		self.pushButton_incrementar_peep.clicked.connect(self.incrementar_peep_funcion)
		self.pushButton_decrementar_peep.clicked.connect(self.decrementar_peep_funcion)
		self.pushButton_encender_vm.clicked.connect(self.activar_sistema)
		self.pushButton_apagar_vm.clicked.connect(self.desactivar_sistema)
		self.pushButton_vc.clicked.connect(self.modo_volumen_control)
		self.pushButton_pc.clicked.connect(self.modo_presion_control)
		self.pushButton_incrementar_volumen.clicked.connect(self.incrementar_volumen)
		self.pushButton_decrementar_volumen.clicked.connect(self.decrementar_volumen)
		self.pushButton_incrementar_presion.clicked.connect(self.incrementar_presion)
		self.pushButton_decrementar_presion.clicked.connect(self.decrementar_presion)
		#### se crearon eventos para todos los botones de la interfaz Grafica ###
		
		# se inicializa en Volumen Control
		self.modo_volumen_control()
	   
		self.verticalLayout_signal_1.addWidget(signal_arduino.all_signal(self))


		dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))  #para inicializar time para actualizacion de datos de la Interfaz grafica
		self._timer = dynamic_canvas.new_timer(400)
		self._timer.add_callback(self.eventos_gui)
		self._timer.start()

		self.counter_warning = 0

	def eventos_gui(self):  # funcion para actualizar los eventos dentro de la interfaz grafica
		self.lcdNumber_presion.display(variables_globales.get_valor_max_presion())
		if variables_globales.get_valor_max_presion()>35:
			self.counter_warning += 1
			if self.counter_warning==1:
				self.frame_warning_presion.show()
			if self.counter_warning==2:
				self.frame_warning_presion.close()
				self.counter_warning = 0
		else:
			self.frame_warning_presion.close()

	def incrementar_presion(self):
		if self.presion_controlado<40:
			self.presion_controlado += 1
			self.lcdNumber_presion_entrada.display(self.presion_controlado)
			variables_globales.set_valor_presion_control(self.presion_controlado)



	def decrementar_presion(self):
		if self.presion_controlado>10:
			self.presion_controlado -= 1
			self.lcdNumber_presion_entrada.display(self.presion_controlado)
			variables_globales.set_valor_presion_control(self.presion_controlado)



	def incrementar_volumen(self):
		if self.volumen_controlado < 800:
			self.volumen_controlado += 10
			self.lcdNumber_volumen_entrada.display(self.volumen_controlado)
			self.lcdNumber_volumen.display(self.volumen_controlado)
			variables_globales.set_valor_volumen_control(self.volumen_controlado)
	def decrementar_volumen(self):
		if self.volumen_controlado > 0:
			self.volumen_controlado -= 10
			self.lcdNumber_volumen.display(self.volumen_controlado)
			self.lcdNumber_volumen_entrada.display(self.volumen_controlado)
			variables_globales.set_valor_volumen_control(self.volumen_controlado)
	def modo_volumen_control(self):
		puerto_serial.enviar_datos("volumen_control")
		self.label_modo.setText("VOLUMEN CONTROL")
		self.label_10.setText("ml")

		self.led_vc_on.show()
		self.led_vc_off.close()
		self.led_pc_off.show()
		self.led_pc_on.close()

		self.lcdNumber_volumen_entrada.show()
		self.lcdNumber_presion_entrada.close()
		self.pushButton_decrementar_volumen.show()
		self.pushButton_incrementar_volumen.show()
		self.pushButton_decrementar_presion.close()
		self.pushButton_incrementar_presion.close()


	def modo_presion_control(self):
		puerto_serial.enviar_datos("presion_control")
		self.label_modo.setText("PRESION CONTROL")
		self.label_10.setText("cmH2O")


		self.led_vc_off.show()
		self.led_vc_on.close()
		self.led_pc_on.show()
		self.led_pc_off.close()

		self.lcdNumber_volumen_entrada.close()
		self.lcdNumber_presion_entrada.show()
		self.pushButton_decrementar_volumen.close()
		self.pushButton_incrementar_volumen.close()
		self.pushButton_decrementar_presion.show()
		self.pushButton_incrementar_presion.show()




	def activar_sistema(self):
		if self.pase_on==1:
			puerto_serial.enviar_datos("activar_sistema")
			puerto_serial.enviar_datos("recibir_señal")
			variables_globales.activar_signal(True)
			self.mostrar_mensaje("Sistema Activado")
			self.sistema_activado = 1
			### Comienza a recibir las señales y activa al timer
		if self.pase_on==0:
			self.mostrar_mensaje("Conectar el Puerto Serie")


	def desactivar_sistema(self):
		if self.pase_on == 1:
			puerto_serial.enviar_datos("desactivar_sistema")
			puerto_serial.enviar_datos("no_recibir_señal")
			variables_globales.activar_signal(False)
			puerto_serial.cerrar_puerto()
			self.pase_on = 0
			self.contador  = 0
			self.sistema_activado = 0
			self.mostrar_mensaje("Se Apaga el Sistema")

	def desconectar_puerto(self):
		if self.pase_on == 1:
			puerto_serial.enviar_datos("desactivar_sistema")
			variables_globales.activar_signal(False)
			puerto_serial.cerrar_puerto()
			self.pase_on = 0
			self.contador  = 0
			self.sistema_activado = 0
			self.mostrar_mensaje("Se Desconecto del Puerto COM")

	def conectar_puerto(self):

		if self.pase_on==1:
			self.comboBox.setCurrentIndex(self.posicion_com)
			self.mostrar_mensaje(f"Ya esta conectado el puerto serie {self.com_seleccionado}")

		if self.pase_on==0:
			self.com_seleccionado = self.comboBox.currentText()
			self.posicion_com = self.comboBox.currentIndex()


			if puerto_serial.conectar_puerto(self.com_seleccionado):  # Conecta a puerto serie y retorna True or False
				self.pase_on = 1
				self.mostrar_mensaje(f"Se a Conectado al puerto Serial {self.com_seleccionado}")

			elif self.posicion_com == 0:
				self.mostrar_mensaje("Escoger un Puerto COM")
			else:
				self.mostrar_mensaje("Error al Conectar el Puerto Seleccionado")

	def incrementar_frecuencia(self):
		if self.pase_on == 1:
			if self.frecuencia_lcd<30:  # Condiciona que la frecunecia respiratora no supere los 30 rpm
				self.frecuencia_lcd += 1  # Incrementa la frecuencia en uno
				puerto_serial.enviar_datos("incrementar_frecuencia")
				variables_globales.set_valor_frecuencia(self.frecuencia_lcd)  # mandamos el  valor de la frecuencia 
			self.lcdNumber_frecuencia.display(self.frecuencia_lcd)  # Muesta la frecuencia actual en LCD_FRECUENCIA
			self.lcdNumber_flujo.display(self.frecuencia_lcd)

	def decrementar_frecuencia(self):
		if self.pase_on == 1:
			if self.frecuencia_lcd>10:  # Condiciona que la frecunecia respiratora no baje las 10 rpm
				self.frecuencia_lcd -= 1  # Decrementa la frecuencia en uno
				puerto_serial.enviar_datos("decrementar_frecuencia")
				variables_globales.set_valor_frecuencia(self.frecuencia_lcd)  # mandamos el  valor de la frecuencia 
			self.lcdNumber_frecuencia.display(self.frecuencia_lcd)  # Muesta la frecuencia actual en LCD_FRECUENCIA
			self.lcdNumber_flujo.display(self.frecuencia_lcd)

	def incrementar_peep_funcion(self):
		if self.pase_on == 1:
			if self.dato_lcd_peep < 20:  # Condiciona que el maximo valor de peep ingresado sea 20
				self.dato_lcd_peep += 1  # Incrementa en uno el valor de peep
				self.lcdNumber_peep.display(self.dato_lcd_peep)  # Muestra los datos al LCD_PEEP
				self.label_peep_actual.setText(str(self.dato_lcd_peep))
				variables_globales.set_dato_peep(self.dato_lcd_peep)

	def decrementar_peep_funcion(self):
		if self.pase_on == 1:
			if self.dato_lcd_peep>=6:  # Condiciona que el minimo valor de peep ingresado sea 5
				self.dato_lcd_peep -= 1  # Decrementa en uno el valor de peep
				self.lcdNumber_peep.display(self.dato_lcd_peep)  # Muestra los datos al LCD_PEEP
				self.label_peep_actual.setText(str(self.dato_lcd_peep))
				variables_globales.set_dato_peep(self.dato_lcd_peep)

	def mostrar_mensaje(self,mensaje):  # Funcion para Mostrar mensajes de alerta 
		self.mensaje.setWindowTitle("Mensaje")  # Titulo del Mensaje
		self.mensaje.setText(mensaje)  # Se muestra el texto de mensaje recibido por la funcion
		self.mensaje.move(self.pos().x()+500, self.pos().y()+400)   # Pocision donde aparecera el mensaje y el tamaño de este
		self.mensaje.exec_()  # Para cerrar el mensaje         

if __name__ == "__main__":

	app = QtWidgets.QApplication([])
	app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
	window = MainWindow()
	window.show()
	app.exec_()
	try:
		puerto_serial.enviar_datos("desactivar_sistema")
		puerto_serial.enviar_datos("volumen_control")
		puerto_serial.enviar_datos("no_recibir_señal")
		puerto_serial.cerrar_puerto()
	except:
		None