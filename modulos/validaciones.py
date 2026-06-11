def validar_texto(texto):
    try:
        return str(texto)
    except Exception as e:
        print(f"Error al validar el texto: {e}, ingrese un valor válido.")
        return None
        
def validar_numero(numero):
        try:
            numero = int(numero)
            return numero > 0
        except Exception as e:
            print(f"Error al validar el número: {e}, ingrese un valor válido.")
            return None
        
def validar_continente(continente):
    continentes_validos = ["America", "Europa", "Asia", "Africa", "Oceania"]
    if continente in continentes_validos:
        return continente
    else:
        print(f"Error al validar el continente: {continente} no es un continente válido.")
        return None
    
def pedir_numero_positivo_obligatorio():
    while True:
        try:
            numero = int(numero)
            return numero > 0
        except Exception as e:
            print(f"Error al validar el número: {e}, ingrese un valor válido.")
            return None

def pedir_texto_obligatorio():
    while True:
        texto = input("Ingrese un texto: ")
        if validar_texto(texto):
            return texto
        else:
            print("Texto no válido. Por favor, ingrese un texto válido.")