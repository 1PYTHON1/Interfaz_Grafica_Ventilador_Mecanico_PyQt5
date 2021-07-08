from PyQt5 import QtWidgets
import numpy as np
import random
import time
import serial
from qtpy.QtWidgets import QFrame ,QVBoxLayout
from qtpy.QtGui import QPen, QBrush
from qtpy.QtCore import QSize, Qt
from qwt import (
    QwtPlot,
    QwtPlotMarker,
    QwtSymbol,
    QwtLegend,
    QwtPlotCurve,
    QwtAbstractScaleDraw,
    QwtPlotGrid
)
import puerto_serial

class DataPlot(QwtPlot):
    def __init__(self, *args, unattended=False):
        QwtPlot.__init__(self, *args)
        self.puerto_serie = puerto_serial.puerto_serial()
        self.puerto_serie.conectar_puerto("COM3")
        self.setCanvasBackground(Qt.black)
        self.alignScales()
        self.vb = QVBoxLayout(self)
        # Initialize data
        self.x = np.linspace(0.0, 100.0,800 )
        self.y = np.zeros(len(self.x))
        self.z = np.zeros(len(self.x))
        numpy_plot = QwtPlot(self)
        self.setTitle("GRAFICA DE FLUJO")
        #self.insertLegend(QwtLegend(), QwtPlot.BottomLegend)

        self.curveR = QwtPlotCurve("Data Moving Right")
        self.curveR.attach(numpy_plot)
        self.curveR.setSymbol(
            QwtSymbol(QwtSymbol.Ellipse, QBrush(), QPen(Qt.red), QSize(4, 4))
        )
        self.vb.addWidget(numpy_plot)
        self.curveR.setPen(QPen(Qt.red))
        self.setAxisTitle(QwtPlot.yLeft, "FLUJO")
        self.startTimer(10 if unattended else 10)


    def alignScales(self):
        self.canvas().setFrameStyle(QFrame.Box | QFrame.Plain)
        self.canvas().setLineWidth(3)
        for axis_id in QwtPlot.AXES:
            scaleWidget = self.axisWidget(axis_id)
            if scaleWidget:
                scaleWidget.setMargin(0)
            scaleDraw = self.axisScaleDraw(axis_id)
            if scaleDraw:
                scaleDraw.enableComponent(QwtAbstractScaleDraw.Backbone, False)

    def timerEvent(self,e):
        self.y = np.concatenate((self.y[1:], self.y[:1]))
        self.y[-1] = self.puerto_serie.recibir_datos()
        self.curveR.setData(self.x, self.y)
        self.replot()
