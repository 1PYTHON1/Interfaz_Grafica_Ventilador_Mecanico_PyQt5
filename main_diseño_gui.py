####### Diseño de Interfaz Grafica BY Jose ID ####

# Importamos las libreria

from diseño import *  # importamos el modulo de nuestro diseño en PyQt5
import serial  # Importamos serial para la comunicacion serial con arduino
import matplotlib.pyplot as plt  # Importamos matplotlib para mostrar las graficas
import numpy as np  # Importamos numpy para manejar matrices de nuestros datos obtenidas de arduino
import qdarkstyle  # Para darle un estilo oscuro a nuestra interfaz graficas diseñada en PyQt5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# fin de la importacion de dependencias

def abrir_puerto(self,com_puerto):
    global ser  # variable global ser 
    try:
        ser = serial.Serial(com_puerto,19200)
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
        return lista  # retorna el dato 
    except:
        dato = [0,0,0]
        return dato

def enviar_datos(self,dato):
    if dato == "activar_sistema":
        ser.write(b'3\r\n')
    if dato == "desactivar_sistema":
        ser.write(b'4\r\n')
    if dato == "enviar_frecuencia":
        ser.write(b'\r\n')
    if dato == "incrementar_frecuencia":
        ser.write(b'1')
    if dato == "decrementar_frecuencia":
        ser.write(b'0')

def deconectar_puerto(self):
    ser.close()

class Canvas_1(FigureCanvas):
    def __init__(self, parent):

        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=90)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)
        
        self.ax.plot(t, s,"b")
        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
        self.ax.grid()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)
        #variables del ventana principal
        self.pase_on = 0  # condicionara que se debe conectar el puerto serie primero
        self.frecuencia_lcd = 30 # comienza con 10
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
        
        #FIGURA DINAMICA_1
        self.dynamic_canvas_1 = FigureCanvas(Figure(figsize=(5, 3),dpi=100))
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(self.dynamic_canvas_1, self))
        self.verticalLayout_signal_1.addWidget(self.dynamic_canvas_1)

        #Ploteamos la figura dinamica
        self._dynamic_ax_1 = self.dynamic_canvas_1.figure.subplots()
        self._dynamic_ax_1.grid()
        t = np.linspace(0, 800 , 800)
        # Set up a Line2D.
        #self._line, = self._dynamic_ax.plot(t, np.in(t + time.time()))     
        self._line, = self._dynamic_ax_1.plot(t, np.linspace(0,40,800),"g")
        self._timer = self.dynamic_canvas_1.new_timer(100)  # hace una actualizacion cada 1 milisegundo
        self._timer.add_callback(self._update_canvas)
        #self._timer.start()
        #FIGURA DINAMICA 1


        #FIGURA DINAMICA_2
        self.dynamic_canvas_2 = FigureCanvas(Figure(figsize=(5, 3)))
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(self.dynamic_canvas_2, self))
        self.verticalLayout_signal_2.addWidget(self.dynamic_canvas_2)

        #Ploteamos la figura dinamica
        self._dynamic_ax_2 = self.dynamic_canvas_2.figure.subplots()
        self._dynamic_ax_2.grid()
        # Set up a Line2D.
        #self._line, = self._dynamic_ax.plot(t, np.in(t + time.time()))
        self._line_2, = self._dynamic_ax_2.plot(t, np.linspace(-300,300,800),"b")
        #self._timer_2 = self.dynamic_canvas_2.new_timer(50)
        #self._timer_2.add_callback(self._update_canvas_2)
        #self._timer_2.start()
        #FIGURA DINAMICA 3


        #FIGURA DINAMICA_3
        self.dynamic_canvas_3 = FigureCanvas(Figure(figsize=(5, 3)))
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(self.dynamic_canvas_3, self))
        self.verticalLayout_signal_3.addWidget(self.dynamic_canvas_3)

        #Ploteamos la figura dinamica
        self._dynamic_ax_3 = self.dynamic_canvas_3.figure.subplots()
        self._dynamic_ax_3.grid()
        # Set up a Line2D.
        #self._line, = self._dynamic_ax.plot(t, np.in(t + time.time()))
        self._line_3, = self._dynamic_ax_3.plot(t, np.linspace(0,300,800),"r")
        #self._timer_3 = self.dynamic_canvas_3.new_timer(50)
        #self._timer_3.add_callback(self._update_canvas_3)
        #self._timer_3.start()
        #FIGURA DINAMICA 3

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
        self.label_peep_actual.setText(str(self.dato_lcd_peep_confirmado))  # Setea la etiqueta con el valor de PEEP 
        self.lcdNumber_peep.display(self.dato_lcd_peep)  # Mostrara el VALOR de PEEP inicial que es 5


        # factor de escala de 255 - 0 a valores de reales de medicion 



    def desconectar_puerto(self):
        if self.pase_on == 1:
            self._timer.stop()  # Desactiva el timer y da en pausa la peticion de datos
            deconectar_puerto(self)
            self.pase_on = 0
            self.contador  = 0
            self.dato_y_volumen = np.array([])
            self.dato_y_flujo = np.array([]) 
            self.dato_x = np.array([])
            self.dato_y_presion = np.array([])

            self.mensaje.setWindowTitle("Mensaje")
            self.mensaje.setText("Se Desconecto del Puerto COM")
            self.mensaje.move(self.pos().x()+500, self.pos().y()+400)
            self.mensaje.exec_()

    def conectar_puerto(self):

        if self.pase_on==1:
            self.comboBox.setCurrentIndex(self.posicion_com)
            self.mensaje.setWindowTitle("MENSAJE")
            self.mensaje.setText(f"Ya esta conectado el puerto serie {self.com_seleccionado}")
            self.mensaje.move(self.pos().x()+500, self.pos().y()+400)
            self.mensaje.exec_()

        if self.pase_on==0:
            self._timer.start()  ### Comienza a recibir las señales y activa al timer
            self.com_seleccionado = self.comboBox.currentText()
            self.posicion_com = self.comboBox.currentIndex()


            if abrir_puerto(self,self.com_seleccionado):  # Conecta a puerto serie y retorna True or False
                self.pase_on = 1
                self.mensaje.setWindowTitle("Mensaje")
                self.mensaje.setText(f"Se a Conectado al puerto Serial {self.com_seleccionado}")
                self.mensaje.move(self.pos().x()+500, self.pos().y()+400)
                self.mensaje.exec_()
            elif self.posicion_com == 0:
                self.mensaje.setWindowTitle("Mensaje")
                self.mensaje.setText("Escoger un Puerto COM")
                self.mensaje.move(self.pos().x()+500, self.pos().y()+400)
                self.mensaje.exec_()
            else:
                self.mensaje.setWindowTitle("Mensaje")
                self.mensaje.setText("Error al Conectar el Puerto Seleccionado")
                self.mensaje.move(self.pos().x()+500, self.pos().y()+400)
                self.mensaje.exec_()

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
        if self.dato_lcd_peep < 20:  # Condiciona que el maximo valor de peep ingresado sea 20
            self.dato_lcd_peep += 1  # Incrementa en uno el valor de peep
            self.lcdNumber_peep.display(self.dato_lcd_peep)  # Muestra los datos al LCD_PEEP

    def decrementar_peep_funcion(self):
        if self.dato_lcd_peep>=6:  # Condiciona que el minimo valor de peep ingresado sea 5
            self.dato_lcd_peep -= 1  # Decrementa en uno el valor de peep
            self.lcdNumber_peep.display(self.dato_lcd_peep)  # Muestra los datos al LCD_PEEP

    def confirmar_peep_funcion(self): 
        self.dato_lcd_peep_confirmado = self.dato_lcd_peep  
        self.label_peep_actual.setText(str(self.dato_lcd_peep_confirmado))

    def _update_canvas(self):

        if self.pase_on == 1:

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
            self.lcdNumber_presion.display(lista_datos[0])
            if self.contador == 800:
                self.contador = 0 
                self.dato_x = np.array([])
                self.dato_y_presion = np.array([])
                self.dato_y_flujo = np.array([])
                self.dato_y_volumen = np.array([])



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

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    window = MainWindow()
    window.show()
    app.exec_()
    try:
        ser.close()
    except:
        None