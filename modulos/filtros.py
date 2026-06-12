def buscar_pais(paises):

    # Pedimos el nombre a buscar
    texto = input("Nombre: ").lower()

    encontrados = []

    # Recorremos la lista de países
    for pais in paises:

        # Buscamos coincidencias parciales
        if texto in pais["nombre"].lower():

            encontrados.append(pais)

    return encontrados


def filtrar_continente(paises):

    # Filtra países por continente
    continente = input("Continente: ").lower()

    return [
        p for p in paises
        if p["continente"].lower() == continente
    ]


def filtrar_poblacion(paises):

    # Filtra países por rango de población
    minimo = int(input("Mínimo: "))
    maximo = int(input("Máximo: "))

    return [
        p for p in paises
        if minimo <= p["poblacion"] <= maximo
    ]


def filtrar_superficie(paises):

    # Filtra países por rango de superficie
    minimo = int(input("Mínimo: "))
    maximo = int(input("Máximo: "))

    return [
        p for p in paises
        if minimo <= p["superficie"] <= maximo
    ]


def ordenar_paises(paises):

    # Menú de ordenamiento
    print("1-Nombre")
    print("2-Población")
    print("3-Superficie")

    opcion = input("Opción: ")
    orden = input(
        "Ascendente(A) Descendente(D): "
    ).upper()

    reverse = orden == "D"

    # Ordenar según el criterio elegido
    if opcion == "1":

        return sorted(
            paises,
            key=lambda p: p["nombre"],
            reverse=reverse
        )

    elif opcion == "2":

        return sorted(
            paises,
            key=lambda p: p["poblacion"],
            reverse=reverse
        )

    elif opcion == "3":

        return sorted(
            paises,
            key=lambda p: p["superficie"],
            reverse=reverse
        )

    return paises