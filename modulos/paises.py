import sys
import os
sys.path.append(os.path.dirname(__file__))

import validaciones


def agregar_pais(lista_paises):
    while True:
        try:
            nombre = validaciones.validar_texto(input("Ingrese el nombre del país: "))
            if not nombre or not nombre.strip():
                print("El nombre no puede estar vacío.")
                continue

            poblacion = int(input("Ingrese la población del país: "))
            if poblacion <= 0:
                print("La población debe ser un número positivo.")
                continue

            superficie = int(input("Ingrese la superficie del país en km²: "))
            if superficie <= 0:
                print("La superficie debe ser un número positivo.")
                continue

            continente = validaciones.validar_continente(input("Ingrese el continente del país: ").capitalize())
            if continente is None:
                continue

        except ValueError:
            print("Error: ingresá solo números enteros.")
            continue

        # Si llegamos acá todos los datos son válidos

        # Verificamos que el país no exista ya en la lista
        for pais in lista_paises:
            if pais["nombre"].lower() == nombre.lower():
                print(f"El país '{nombre.capitalize()}' ya existe en la lista.")
                return lista_paises
            
        nuevo_pais = {
            "nombre": nombre.capitalize(),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente.capitalize()
        }
        lista_paises.append(nuevo_pais)
        print(f"País '{nombre.capitalize()}' agregado correctamente.")
        return lista_paises


def actualizar_pais(lista_paises):
    nombre = validaciones.validar_texto(input("Ingrese el nombre del país a actualizar: "))

    # Recorremos la lista buscando coincidencia exacta 
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
    
            nueva_poblacion = validaciones.validar_numero(input("Ingrese la nueva población: "))
            if nueva_poblacion is None:
                print("Valor inválido, no se actualizó.")
                return lista_paises

            nueva_superficie = validaciones.validar_numero(input("Ingrese la nueva superficie: "))
            if nueva_superficie is None:
                print("Valor inválido, no se actualizó.")
                return lista_paises
            #Cambiamos el valor del país encontrado por los nuevos valores ingresados
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            
            return lista_paises
             
    # Si el for termina sin encontrar el país, avisamos
    print(f"El país '{nombre}' no se encontró en la lista.")
    return lista_paises
  