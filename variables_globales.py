### se guardaran las variables globales del programa 
def estado_signal():  # retorna el estado par aactivar o desactivar las señales en la GUI
	try:
		return estado
	except:
		return False

def activar_signal(dato): # mandamos la señal desde main_diseño para activar las tres señales
	global estado
	estado = dato



def get_dato_peep():  # funcion para obtener el dato del peep
	try:
		return valor_peep
	except:
		return 0

def set_dato_peep(valor):  # Funcion para setear el peep y mandarsela a la Interfaz
	global valor_peep
	valor_peep = valor


def get_valor_max_presion():  # Para obtener el valor maximo de la presion y pasarlo a la GUI
	try:
		return valor_max_presion
	except:
		return 0

def set_valor_max_presion(valor):  # Para setear cual es el valor maximo de la grafica de presion 
	global valor_max_presion
	valor_max_presion = valor


def get_valor_presion_control():
	try:
		return valor_presion_control

	except:
		return 0

def set_valor_presion_control(valor):
	global valor_presion_control
	valor_presion_control = valor









