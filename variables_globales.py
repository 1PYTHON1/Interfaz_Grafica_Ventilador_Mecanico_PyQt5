### se guardaran las variables globales del programa 
def estado_signal():  # retorna el estado par aactivar o desactivar las señales en la GUI
	try:
		return estado
	except:
		return False

def activar_signal(dato): # mandamos la señal desde main_diseño para activar las tres señales
	global estado
	estado = dato



def get_dato_peep():
	try:
		return valor_peep
	except:
		return 0

def set_dato_peep(valor):
	global valor_peep
	valor_peep = valor


def get_valor_max_presion():
	try:
		return valor_max_presion
	except:
		return 0

def set_valor_max_presion(valor):
	global valor_max_presion
	valor_max_presion = valor





