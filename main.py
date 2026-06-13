from modulos import validaciones, archivos, paises, filtros, estadisticas


#hace los prints generales del menu
def mostrar_menu():
    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("0. Salir")

# Cargamos los países desde el CSV al iniciar el programa
def main():
    lista_paises = archivos.cargar_csv("paises.csv")

    # Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            paises.agregar_pais(lista_paises)
             # Guardamos los cambios en el CSV
            archivos.guardar_csv("paises.csv", lista_paises)

        elif opcion == "2":
            paises.actualizar_pais(lista_paises)
             # Guardamos los cambios en el CSV
            archivos.guardar_csv("paises.csv", lista_paises)

        elif opcion == "3":
            if not lista_paises:
                print("No hay países cargados.")
                continue
            resultados = filtros.buscar_pais(lista_paises)
            for p in resultados:
                print(p)
                
        elif opcion == "4":
            if not lista_paises:
                print("No hay países cargados.")
                continue
            # Submenú de filtros
            print("\n--- FILTRAR POR ---")
            print("1. Continente")
            print("2. Rango de población")
            print("3. Rango de superficie")
            sub_opcion = input("Elegí una opción: ")

            if sub_opcion == "1":
                resultados = filtros.filtrar_continente(lista_paises)
            elif sub_opcion == "2":
                resultados = filtros.filtrar_poblacion(lista_paises)
            elif sub_opcion == "3":
                resultados = filtros.filtrar_superficie(lista_paises)
            else:
                print("Opción inválida.")
                resultados = []

            for p in resultados:
                print(p)

        elif opcion == "5":
            if not lista_paises:
                print("No hay países cargados.")
                continue
            # ordenar_paises() maneja internamente el submenú de criterio y direcció
            resultado = filtros.ordenar_paises(lista_paises)
            for p in resultado:
                print(p)
        
        elif opcion == "6":
            # Verificamos que haya países cargados antes de calcular
            if not lista_paises:
                print("No hay países cargados.")
                continue
            else:
                estadisticas.estadisticas(lista_paises)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intentá de nuevo.")

main()