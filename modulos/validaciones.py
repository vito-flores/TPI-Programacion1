def validar_texto(texto):
    # Intenta convertir el valor recibido a string
    try:
        return str(texto)
    except Exception as e:
    # Si falla la conversión, muestra el error
        print(f"Error al validar el texto: {e}, ingrese un valor válido.")
        return None
        
def validar_numero(numero):
        try:
            # Convierte el valor a entero
            numero = int(numero)
            # Retorna True si es positivo, de lo contrario False
            if numero > 0:
                return numero
            else:
                print("El numero debe ser positivo")
                return None
        except Exception as e:
            # Si no se puede convertir a entero, muestra el error
            print(f"Error al validar el número: {e}, ingrese un valor válido.")
            return None
        
def validar_continente(continente):
    # Lista de continentes aceptados por el sistema
    continentes_validos = ["America", "Europa", "Asia", "Africa", "Oceania"]
    # Verifica si el continente ingresado está en la lista
    if continente in continentes_validos:
        return continente
    else:
         # Si no es válido, informa al usuario
        print(f"Error al validar el continente: {continente} no es un continente válido.")
        return None
    
# def pedir_numero_positivo_obligatorio(numero):
#     while True:
#         try:
#             numero = int(input("Ingrese un número positivo: "))
#             return numero > 0
#         except Exception as e:
#             print(f"Error al validar el número: {e}, ingrese un valor válido.")
#             return None

# def pedir_texto_obligatorio(texto):
#     while True:
#         try:
#             texto = input("Ingrese un texto: ")
#             if validar_texto(texto):
#                 return texto
#         except Exception as e:
#             print(f"Error al validar el texto: {e}, ingrese un valor válido.")
#             return None