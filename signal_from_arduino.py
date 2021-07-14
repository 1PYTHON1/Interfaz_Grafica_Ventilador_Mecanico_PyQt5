


import numpy as np
from qtpy.QtWidgets import QGridLayout, QWidget
from qtpy.QtGui import QPen
from qtpy.QtCore import Qt
from qwt import QwtPlot, QwtPlotCurve
import puerto_serial    ## se recibe los datos por el puerto serie de arduino 
import variables_globales  ## para manipular el control de todos los scripts 

def drange(start, stop, step):
    start, stop, step = float(start), float(stop), float(step)
    size = int(round((stop - start) / step))
    result = [start] * size
    for i in range(size):
        result[i] += i * step
    return result


def lorentzian(x):
    return 1.0 / (1.0 + (x - 5.0) ** 2)


class all_signal(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        layout = QGridLayout(self)
    
        self.x = np.linspace(0.0, 20.0,800 )
        self.y_flujo = np.zeros(len(self.x))
        self.y_presion = np.zeros(len(self.x))
        self.y_volumen = np.zeros(len(self.x))

        self.presion_curve = QwtPlotCurve("y = lorentzian(x)")
        x = np.arange(0.0, 10.0, 0.01)
        y = lorentzian(x)
        self.presion_curve.setData(x, y)
        # Create a plot presion
        self.presion_plot = QwtPlot(self)
        self.presion_plot.setTitle("PRESION")
        self.presion_plot.setCanvasBackground(Qt.gray)
        self.presion_plot.plotLayout().setCanvasMargin(0)
        self.presion_plot.plotLayout().setAlignCanvasToScales(True)
        # insert a curve and make it Blue
        self.presion_curve.attach(self.presion_plot)
        self.presion_curve.setPen(QPen(Qt.blue))

        self.presion_min = QwtPlotCurve("Presion_minima")  ## solo son niveles de referencia para el auto escalado 
        self.presion_min.attach(self.presion_plot)
        self.presion_min.setPen(QPen(Qt.blue))

        self.presion_max = QwtPlotCurve("Presion_maxima")  ## solo son niveles de referencia para el auto escalado 
        self.presion_max.attach(self.presion_plot)
        self.presion_max.setPen(QPen(Qt.blue))

        layout.addWidget(self.presion_plot, 0, 0)
        self.presion_plot.replot()




        # create a plot Flujo
        self.flujo_plot = QwtPlot(self)
        self.flujo_plot.setTitle("FLUJO")
        self.flujo_plot.setCanvasBackground(Qt.black)
        self.flujo_plot.plotLayout().setCanvasMargin(0)
        self.flujo_plot.plotLayout().setAlignCanvasToScales(True)
        x = drange(0.0, 10.0, 0.01)
        y = [lorentzian(item) for item in x]
        # insert a curve
        self.flujo_curve = QwtPlotCurve("y = lorentzian(x)")
        self.flujo_curve.attach(self.flujo_plot)
        self.flujo_curve.setPen(QPen(Qt.green))
        self.flujo_curve.setData(x, y)

        self.flujo_min = QwtPlotCurve("Flujo_min")  ## solo son niveles de referencia para el auto escalado 
        self.flujo_min.attach(self.flujo_plot)
        self.flujo_min.setPen(QPen(Qt.green))

        self.flujo_max = QwtPlotCurve("Flujo_max")  ## solo son niveles de referencia para el auto escalado
        self.flujo_max.attach(self.flujo_plot)
        self.flujo_max.setPen(QPen(Qt.green))

        layout.addWidget(self.flujo_plot, 1, 0)
        self.flujo_plot.replot()
        

        # create a plot Volumen
        self.volumen_plot = QwtPlot(self)
        self.volumen_plot.setTitle("VOLUMEN")
        self.volumen_plot.setCanvasBackground(Qt.white)
        self.volumen_plot.plotLayout().setCanvasMargin(0)
        self.volumen_plot.plotLayout().setAlignCanvasToScales(True)
        x = drange(0.0, 10.0, 0.01)
        y = [lorentzian(item) for item in x]
        # insert a curve
        self.volumen_curve = QwtPlotCurve("y = lorentzian(x)")
        self.volumen_curve.attach(self.volumen_plot)
        self.volumen_curve.setPen(QPen(Qt.red))
        self.volumen_curve.setData(x, y)
        self.volumen_max = QwtPlotCurve("Volumen Max")  # referencia 
        self.volumen_max.attach(self.volumen_plot)
        self.volumen_max.setPen(QPen(Qt.red))

        layout.addWidget(self.volumen_plot, 2, 0)
        self.volumen_plot.replot()
        self.startTimer(6)


    def timerEvent(self,e):


        if variables_globales.estado_signal(): ### Condiciona que se debe enviar un True a estado signal 
            ## Se recibe los datos de arduino en forma de tupla y se agrega a la matriz 
            rango_datos = 800
            lista_datos = puerto_serial.recibir_datos_signal() 


            self.y_presion = np.concatenate((self.y_presion[1:], self.y_presion[:1]))
            self.y_presion[-1] = (lista_datos[0]*(30/255)) + variables_globales.get_dato_peep()  # escalamos la señal y sumamos el peep
            maximo_y_presion = np.amax(self.y_presion)  ##se obtiene el valor maximo de la matriz de valores
            minimo_y_flujo = np.amin(self.y_presion)
            variables_globales.set_valor_max_presion(maximo_y_presion)  # Mandamos los valores maximos a la variable global
            matriz_presion_max = np.linspace(maximo_y_presion+10,maximo_y_presion+10, rango_datos)


            self.y_volumen = np.concatenate((self.y_volumen[1:], self.y_volumen[:1]))   
            self.y_volumen[-1] = lista_datos[2]*(variables_globales.get_valor_presion_control()/255)

            self.y_flujo = np.concatenate((self.y_flujo[1:], self.y_flujo[:1]))
            self.y_flujo[-1] = lista_datos[1]*(90/255)
            minimo_y_flujo = np.amin(self.y_flujo)
            maximo_y_flujo = np.amax(self.y_flujo)
            matriz_flujo_min = np.linspace(minimo_y_flujo-60 ,minimo_y_flujo-60, rango_datos)
            matriz_flujo_max = np.linspace(maximo_y_flujo+60,maximo_y_flujo+60, rango_datos)


            ## Se manda los datos a las variables correspondiente y se plotea al canva
            self.presion_curve.setData(self.x, self.y_presion)
            self.presion_min.setData(self.x, np.linspace(0, 0 , rango_datos))
            self.presion_max.setData(self.x, matriz_presion_max)
            self.presion_plot.replot()

            self.volumen_curve.setData(self.x, self.y_volumen)
            self.volumen_max.setData(self.x , np.linspace(900, 900, rango_datos))
            self.volumen_plot.replot()

            self.flujo_curve.setData(self.x, self.y_flujo)
            self.flujo_min.setData(self.x, matriz_flujo_min)
            self.flujo_max.setData(self.x, matriz_flujo_max)
            self.flujo_plot.replot()




if __name__ == "__main__":
    from qwt import tests

    tests.test_widget(all_signal, size=(400, 300))