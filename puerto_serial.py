import serial

#class puerto_serial:
#    def __init__(self):  # variable global ser 
#        None
def conectar_puerto(puerto):
    try:
        global ser
        ser = serial.Serial(puerto,9600)
        return True
    except:
        print("Error")
        return False

def recibir_datos():
    try:

        dato = ser.readline()  # Lee el la cadena de byte del puerto serial
        dato = str(dato.decode()).replace('\r','')  # decodifica el byte a str y quita el retorno "\r"
        dato = dato.replace('\n','')  # Quita del str el salto de linea "\n"
        dato = float(dato)
        return dato  # retorna los datos en una lista 
    except:
        dato = 0  # En caso que haya falsa lectura se enviara 0 para no generar errore
        return dato  # Retorn a la lista de datos [0,0,0]

def recibir_datos_signal():
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
        dato = [51,21,11]  # En caso que haya falsa lectura se enviara 0 para no generar errore
        return dato  # Retorn a la lista de datos [0,0,0]


def enviar_datos(dato):
    try:
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
        if dato == "modo_volumen_control":
            ser.write(b'4')
        if dato == "modo_presion_control":
            ser.write(b'5')
    except:
        None

def cerrar_puerto():
    ser.close()

