#Importamos el modulo csv para leer y escribir archivos csv
import csv

def cargar_csv(nombre_archivo):

    #Lista donde se almacenaran los paises cargados desde el archivo csv
    paises = []

    try:
        #Abrimos el archivo csv en modo lectura
        with open(nombre_archivo, "r" , encoding='utf-8') as archivo:
            
            lector = csv.DictReader(archivo)
            
            #Recorremos cada fila del archivo
            for fila in lector:

                #Agregamos el pais a la lista convirtiendo poblacion y superficie a enteros
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                    })
            return paises
    #Se ejecuta si el archivo no se encuentra
    except FileNotFoundError:
        print("Archivo no encontrado")

    #Captura cualquier otro error inesperado
    except Exception as e:
        print(f"Error: {e}")

    #Retornamos la lista de paises cargados
    return paises

def guardar_csv(nombre_archivo, paises):

    #Abrimos el archivo en modo escritura
    with open(nombre_archivo, "w", newline='', encoding='utf-8') as archivo:

        #Definimos los nombres de las columnas del csv
        campos = ["nombre", "poblacion", "superficie", "continente"]

        #Creamos el escritor csv
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        #Escribimos la fila de encabezado
        escritor.writeheader()

        #Escribimos todos los paises en el archivo
        escritor.writerows(paises)

    #Confirmamos que los datos fueron guardados correctamente
    print("Datos guardados correctamente")

        