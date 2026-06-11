def estadisticas(paises):

    #Obtenemos el pais con mayor poblacion
    mayor = max(
        paises,
        key=lambda p: p["poblacion"]
    )

    #Obtenemos el pais con menor poblacion
    menor = min(
        paises,
        key=lambda p: p["poblacion"]
    )

    #Calculamos el promedio de poblacion de todos los paises
    promedio_poblacion = sum(
        p["poblacion"] for p in paises
    ) / len(paises)

    #Calculamos el promedio de superficie de todos los paises
    promedio_superficie = sum(
        p["superficie"] for p in paises
    ) / len(paises)

    #Diccionario para mostrar cuantos paises hay por continente
    continentes = {}

    #Recorremos todos los paises
    for pais in paises:

        #Guardamos el pais del continente actual
        cont = pais["continente"]

        #Si el continente ya esta en el diccionario, sumamos 1 a su contador
        if cont in continentes:
            continentes[cont] += 1

        #Si no existe, lo agregamos con valor 1
        else:
            continentes[cont] = 1

    
    #Mostramos el titulo de la seccion de estadisticas
    print("\nESTADISTICAS:")

     # Mostramos el país con mayor población
    print(f"Mayor población: {mayor['nombre']}")

    # Mostramos el país con menor población
    print(f"Menor población: {menor['nombre']}")

    # Mostramos el promedio de población
    print(f"Promedio población: {promedio_poblacion:.2f}")

    # Mostramos el promedio de superficie
    print(f"Promedio superficie: {promedio_superficie:.2f}")

    # Mostramos la cantidad de países agrupados por continente
    print("\nCantidad por continente")

    # Recorremos el diccionario de continentes
    for c, cant in continentes.items():

        print(f"{c}: {cant}")