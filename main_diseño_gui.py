####### Diseño de Interfaz Grafica BY Jose ID ####

# Importamos las libreria
from diseño import *
import serial  # Importamos serial para la comunicacion serial con arduino
import matplotlib.pyplot as plt  # Importamos matplotlib para mostrar las graficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np  # Importamos numpy para manejar matrices de nuestros datos obtenidas de arduino
import qdarkstyle  # Para darle un estilo oscuro a nuestra interfaz graficas diseñada en PyQt5

# fin de la importacion de dependencias

def abrir_puerto(self,com_puerto):
    global ser  # variable global ser 
    try:
        ser = serial.Serial(com_puerto,9600)
        return True
    except:
        return False

def recibir_datos(self):
    try:
        lista = []
        for i in range(3):

            dato = ser.readline()  # Lee el la cadena de byte del puerto serial
            dato = str(dato.decode()).replace('\r','')  # decodifica el byte a str y quita el retorno "\r"
            dato = dato.replace('\n','')  # Quita del str el salto de linea "\n"
            if len(dato) > 0 :  # Verifica que cadena de texto (str) no este vacio
                lista.append(int(dato))  # Convierte el str a un int (entero)
            else:
                lista.append(0)
        return lista  # retorna los datos en una lista 
    except:
        dato = [0,0,0]  # En caso que haya falsa lectura se enviara 0 para no generar errore
        return dato  # Retorn a la lista de datos [0,0,0]

def enviar_datos(self,dato):
    if dato == "activar_sistema":
        ser.write(b'2\r\n')
    if dato == "desactivar_sistema":
        ser.write(b'3\r\n')
    if dato == "enviar_frecuencia":
        ser.write(b'0\r\n')  # POR DEFINIR 
    if dato == "incrementar_frecuencia":
        ser.write(b'1')
    if dato == "decrementar_frecuencia":
        ser.write(b'0')
def deconectar_puerto(self):
    ser.close()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)
        #variables del ventana principal
        self.pase_on = 0  # condicionara que se debe conectar el puerto serie primero
        self.frecuencia_lcd = 15 # setea la frecuencia de inicio
        self.volumen_controlado = 0  # valor de ingreso para volumen control
        # variables globales 
        self.contador  = 0
        self.dato_y_flujo = np.array([])  # Matriz que guadara los datos del flujo recibidos de arduino 
        self.dato_y_volumen = np.array([])  # Matriz que guadara los datos del volumen recibidos de arduino 
        self.dato_x = np.array([])   # Matriz que guadara los datos del tiempo 
        self.dato_y_presion = np.array([])   # Matriz que guadara los datos de la presion recibidos de arduino
        self.dato_int = 0  # variable que recibe los datos de arduino
        self.posicion_com  = 0  # Posicion Index del combobox, COM del serial
        self.com_seleccionado = 0  # Puerto COM seleccionado start
        self.dato_lcd_peep = 5  # Comienza con el valor de PEEP en 5
        self.dato_lcd_peep_confirmado = 5  # Variable de confirmacion del PEEP comienza en 5
        self.sistema_activado = 0  # Toma dos valores verdadero o falso
        self.modo_de_control = "volumen_control"  # Guardamos el Modo de Control por default VC
        self.label_peep_actual.setText(str(self.dato_lcd_peep_confirmado))  # Setea la etiqueta con el valor de PEEP 
        self.lcdNumber_peep.display(self.dato_lcd_peep)  # Mostrara el VALOR de PEEP inicial que es 5
        ################################
        
        self.lcdNumber_frecuencia.display(self.frecuencia_lcd)
        self.setWindowTitle("INTERFAZ GRAFICA VENTILADOR MECANICO")
        self.mensaje = QtWidgets.QMessageBox(self)
        self.pushButton_desconectar_serial.clicked.connect(self.desconectar_puerto)
        self.pushButton_conectar_serial.clicked.connect(self.conectar_puerto)
        self.pushButton_frecuencia_up.clicked.connect(self.incrementar_frecuencia)
        self.pushButton_frecuencia_down.clicked.connect(self.decrementar_frecuencia)
        self.pushButton_incrementar_peep.clicked.connect(self.incrementar_peep_funcion)
        self.pushButton_decrementar_peep.clicked.connect(self.decrementar_peep_funcion)
        self.pushButton_confirmar_peep.clicked.connect(self.confirmar_peep_funcion)
        self.pushButton_encender_vm.clicked.connect(self.activar_sistema)
        self.pushButton_apagar_vm.clicked.connect(self.desactivar_sistema)
        self.pushButton_vc.clicked.connect(self.modo_volumen_control)
        self.pushButton_pc.clicked.connect(self.modo_presion_control)
        self.pushButton_incrementar_volumen.clicked.connect(self.incrementar_volumen)
        self.pushButton_decrementar_volumen.clicked.connect(self.decrementar_volumen)
        

        #FIGURA DINAMICA_1
        self.dynamic_canvas_1 = FigureCanvas(Figure(figsize=(5, 3),dpi=100))
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(self.dynamic_canvas_1, self))
        self.verticalLayout_signal_1.addWidget(self.dynamic_canvas_1)

        #Ploteamos la figura dinamica
        self._dynamic_ax_1 = self.dynamic_canvas_1.figure.subplots()
        self._dynamic_ax_1.grid()
        self._dynamic_ax_1.set_ylabel("PRESION")
        self._dynamic_ax_1.set_title("PRESION")  # Agregamos titulo al  grafica de Presion 
        t = np.linspace(0, 800 , 800)
        # Set up a Line2D.
        #self._line, = self._dynamic_ax.plot(t, np.in(t + time.time()))     
        self._line, = self._dynamic_ax_1.plot(t, np.linspace(0,40,800),"g")
        self._timer = self.dynamic_canvas_1.new_timer(1)  # hace una actualizacion cada 1 milisegundo
        self._timer.add_callback(self.actualizacion_grafica)
        #self._timer.start()
        #FIGURA DINAMICA 1




    def incrementar_volumen(self):
        if self.volumen_controlado < 800:
            self.volumen_controlado += 10
            self.lcdNumber_volumen_entrada.display(self.volumen_controlado)
    def decrementar_volumen(self):
        if self.volumen_controlado > 0:
            self.volumen_controlado -= 10
            self.lcdNumber_volumen_entrada.display(self.volumen_controlado)
    def modo_volumen_control(self):
        self.label_modo.setText("VOLUMEN CONTROL")
        self.led_vc_on.show()
        self.led_vc_off.close()
        self.led_pc_off.show()
        self.led_pc_on.close()

    def modo_presion_control(self):
        self.label_modo.setText("PRESION CONTROL")
        self.led_vc_off.show()
        self.led_vc_on.close()
        self.led_pc_on.show()
        self.led_pc_off.close()




    def activar_sistema(self):
        if self.pase_on==1:
            enviar_datos(self,"activar_sistema")
            self.mostrar_mensaje("Sistema Activado")
            self.sistema_activado = 1
            self._timer.start()  ### Comienza a recibir las señales y activa al timer
        if self.pase_on==0:
            self.mostrar_mensaje("Conectar el Puerto Serie")


    def desactivar_sistema(self):
        if self.pase_on == 1:
            self._timer.stop()  # Desactiva el timer y da en pausa la peticion de datos
            enviar_datos(self,"desactivar_sistema")
            deconectar_puerto(self)
            self.pase_on = 0
            self.contador  = 0
            self.sistema_activado = 0
            self.dato_y_volumen = np.array([])
            self.dato_y_flujo = np.array([]) 
            self.dato_x = np.array([])
            self.dato_y_presion = np.array([])
            self.mostrar_mensaje("Se Apaga el Sistema")

    def desconectar_puerto(self):
        if self.pase_on == 1:
            self._timer.stop()  # Desactiva el timer y da en pausa la peticion de datos
            enviar_datos(self,"desactivar_sistema")
            deconectar_puerto(self)
            self.pase_on = 0
            self.contador  = 0
            self.sistema_activado = 0
            self.dato_y_volumen = np.array([])
            self.dato_y_flujo = np.array([]) 
            self.dato_x = np.array([])
            self.dato_y_presion = np.array([])
            self.mostrar_mensaje("Se Desconecto del Puerto COM")

    def conectar_puerto(self):

        if self.pase_on==1:
            self.comboBox.setCurrentIndex(self.posicion_com)
            self.mostrar_mensaje(f"Ya esta conectado el puerto serie {self.com_seleccionado}")

        if self.pase_on==0:
            self.com_seleccionado = self.comboBox.currentText()
            self.posicion_com = self.comboBox.currentIndex()


            if abrir_puerto(self,self.com_seleccionado):  # Conecta a puerto serie y retorna True or False
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
                enviar_datos(self,"incrementar_frecuencia")
            self.lcdNumber_frecuencia.display(self.frecuencia_lcd)  # Muesta la frecuencia actual en LCD_FRECUENCIA

    def decrementar_frecuencia(self):
        if self.pase_on == 1:
            if self.frecuencia_lcd>10:  # Condiciona que la frecunecia respiratora no baje las 10 rpm
                self.frecuencia_lcd -= 1  # Decrementa la frecuencia en uno
                enviar_datos(self,"decrementar_frecuencia")
            self.lcdNumber_frecuencia.display(self.frecuencia_lcd)  # Muesta la frecuencia actual en LCD_FRECUENCIA

    def incrementar_peep_funcion(self):
        if self.pase_on == 1:
            if self.dato_lcd_peep < 20:  # Condiciona que el maximo valor de peep ingresado sea 20
                self.dato_lcd_peep += 1  # Incrementa en uno el valor de peep
                self.lcdNumber_peep.display(self.dato_lcd_peep)  # Muestra los datos al LCD_PEEP

    def decrementar_peep_funcion(self):
        if self.pase_on == 1:
            if self.dato_lcd_peep>=6:  # Condiciona que el minimo valor de peep ingresado sea 5
                self.dato_lcd_peep -= 1  # Decrementa en uno el valor de peep
                self.lcdNumber_peep.display(self.dato_lcd_peep)  # Muestra los datos al LCD_PEEP

    def confirmar_peep_funcion(self): 
        self.dato_lcd_peep_confirmado = self.dato_lcd_peep  
        self.label_peep_actual.setText(str(self.dato_lcd_peep_confirmado))

    def actualizacion_grafica(self):

        if self.sistema_activado == 1:

            self.contador += 1#*(1/(self.frecuencia_lcd/2))
            self.dato_x = np.append(self.dato_x,self.contador) 
            lista_datos = recibir_datos(self)  # Retorna una lista con dos datos flujo y presion

            self.dato_y_presion = np.append(self.dato_y_presion, (lista_datos[0]*30/255) + self.dato_lcd_peep_confirmado)
            self.dato_y_flujo = np.append(self.dato_y_flujo,lista_datos[1])
            self.dato_y_volumen = np.append(self.dato_y_volumen, lista_datos[2])

            # PLOTER DE LA SEÑAL
            self._line_3.set_data(self.dato_x,self.dato_y_volumen)
            self._line_3.figure.canvas.draw()
            self._line_2.set_data(self.dato_x,self.dato_y_flujo)
            self._line_2.figure.canvas.draw()
            self._line.set_data(self.dato_x,self.dato_y_presion)
            self._line.figure.canvas.draw()
            # Fin del PLoter de la señal

            #Mandamos la señal al LCD de la presion 
            self.lcdNumber_presion.display(lista_datos[0]*30/255 + self.dato_lcd_peep_confirmado)

            if self.contador == 800:
                self.contador = 0 
                self.dato_x = np.array([])
                self.dato_y_presion = np.array([])
                self.dato_y_flujo = np.array([])
                self.dato_y_volumen = np.array([])


    def mostrar_mensaje(self,mensaje):  # Funcion para Mostrar mensajes de alerta 
        self.mensaje.setWindowTitle("Mensaje")  # Titulo del Mensaje
        self.mensaje.setText(mensaje)  # Se muestra el texto de mensaje recibido por la funcion
        self.mensaje.move(self.pos().x()+500, self.pos().y()+400)   # Pocision donde aparecera el mensaje y el tamaño de este
        self.mensaje.exec_()  # Para cerrar el mensaje         

if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    #Style MatploLib
    #plt.style.use('dark_background')  # ok
    #plt.style.use("ggplot")
    #plt.style.use("bmh")
    #plt.style.use("seaborn-notebook")
    #plt.style.use("seaborn-talk")
    plt.style.use("seaborn-dark")  # ok
    #plt.style.use("seaborn-colorblind")
    #Style MatplotLib

    #app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    window = MainWindow()
    window.show()
    app.exec_()
    try:
        ser.close()
    except:
        None