def buscar_pais(paises):

    texto = input("Nombre: ").strip().lower()

    if not texto:
        print("Debe ingresar un nombre.")
        return []

    encontrados = []

    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    return encontrados


def filtrar_continente(paises):

    continente = input("Continente: ").strip().lower()

    if not continente:
        print("Debe ingresar un continente.")
        return []

    return [
        p for p in paises
        if p["continente"].lower() == continente
    ]


def filtrar_poblacion(paises):

    while True:
        try:
            minimo = int(input("Mínimo: "))
            maximo = int(input("Máximo: "))

            if minimo > maximo:
                print("El mínimo no puede ser mayor que el máximo.")
                continue

            break

        except ValueError:
            print("Debe ingresar números enteros.")

    return [
        p for p in paises
        if minimo <= p["poblacion"] <= maximo
    ]


def filtrar_superficie(paises):

    while True:
        try:
            minimo = int(input("Mínimo: "))
            maximo = int(input("Máximo: "))

            if minimo > maximo:
                print("El mínimo no puede ser mayor que el máximo.")
                continue

            break

        except ValueError:
            print("Debe ingresar números enteros.")

    return [
        p for p in paises
        if minimo <= p["superficie"] <= maximo
    ]


def ordenar_paises(paises):

    print("1-Nombre")
    print("2-Población")
    print("3-Superficie")

    while True:
        opcion = input("Opción: ")

        if opcion in ("1", "2", "3"):
            break

        print("Opción inválida.")

    while True:
        orden = input(
            "Ascendente(A) Descendente(D): "
        ).upper()

        if orden in ("A", "D"):
            break

        print("Debe ingresar A o D.")

    reverse = orden == "D"

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

    else:

        return sorted(
            paises,
            key=lambda p: p["superficie"],
            reverse=reverse
        )