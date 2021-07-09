


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
    
        self.x = np.linspace(0.0, 20.0,1000 )
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
        layout.addWidget(self.volumen_plot, 2, 0)
        self.volumen_plot.replot()

        
        self.startTimer(10)

    def timerEvent(self,e):
        if variables_globales.estado_signal(): ### Condiciona que se debe enviar un True a estado signal 
            ## Se recibe los datos de arduino en forma de tupla y se agrega a la matriz 
            lista_datos = puerto_serial.recibir_datos_signal() 

            self.y_presion = np.concatenate((self.y_presion[1:], self.y_presion[:1]))
            self.y_presion[-1] = (lista_datos[0]*(30/255)) + variables_globales.get_dato_peep()  # escalamos la señal y sumamos el peep
            maximo_y_presion = np.amax(self.y_presion)  ##se obtiene el valor maximo de la matriz de valores
            variables_globales.set_valor_max_presion(maximo_y_presion)  # Mandamos los valores maximos a la variable global
            self.y_volumen = np.concatenate((self.y_volumen[1:], self.y_volumen[:1]))   
            self.y_volumen[-1] = lista_datos[2]

            self.y_flujo = np.concatenate((self.y_flujo[1:], self.y_flujo[:1]))
            self.y_flujo[-1] = lista_datos[1]

            ## Se manda los datos a las variables correspondiente y se plotea al canva
            self.presion_curve.setData(self.x, self.y_presion)
            self.presion_plot.replot()
            self.volumen_curve.setData(self.x, self.y_volumen)
            self.volumen_plot.replot()
            self.flujo_curve.setData(self.x, self.y_flujo)
            self.flujo_plot.replot()


if __name__ == "__main__":
    from qwt import tests

    tests.test_widget(all_signal, size=(400, 300))