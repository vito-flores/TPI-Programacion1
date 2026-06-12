import validaciones
def agregar_pais(lista_paises):
    nombre = validaciones.validar_texto(input("Ingrese el nombre del país: "))
    poblacion = validaciones.validar_numero(input("Ingrese la población del país: "))
    superficie = validaciones.validar_numero(input("Ingrese la superficie del país: "))
    continente = validaciones.validar_continente(input("Ingrese el continente del país: "))

    nuevo_pais = { 
        "nombre": nombre.capitalize(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.capitalize()
    }
    lista_paises.append(nuevo_pais)
    return lista_paises

def actualizar_pais(lista_paises):
    nombre = validaciones.validar_texto(input("Ingrese el nombre del país a actualizar: "))
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
    
            nueva_poblacion = validaciones.validar_numero(input("Ingrese la nueva población del país: "))
            nueva_superficie = validaciones.validar_numero(input("Ingrese la nueva superficie del país: "))
            
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            
            return lista_paises
        
    print(f"El país '{nombre}' no se encontró en la lista.")
    return lista_paises
  