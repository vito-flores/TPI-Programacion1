def buscar_pais(paises):

    while True:

        texto = input("Nombre: ").strip()

        if not texto:
            print("Debe ingresar un nombre.")
            continue

        break

    encontrados = []

    for pais in paises:

        if texto.lower() in pais["nombre"].lower():

            encontrados.append(pais)

    return encontrados


def filtrar_continente(paises):

    continentes_validos = [
        "america",
        "europa",
        "asia",
        "africa",
        "oceania"
    ]

    while True:

        continente = input("Continente: ").strip().lower()

        if not continente:
            print("Debe ingresar un continente.")
            continue

        if not continente.isalpha():
            print("Solo se permiten letras.")
            continue

        if continente not in continentes_validos:
            print(
                "Continente inválido. "
                "Opciones: America, Europa, Asia, Africa u Oceania."
            )
            continue

        break

    return [
        p for p in paises
        if p["continente"].lower() == continente
    ]


def filtrar_poblacion(paises):

    while True:

        try:

            minimo = int(input("Minimo: "))
            maximo = int(input("Maximo: "))

            if minimo < 0 or maximo < 0:
                print("Los valores no pueden ser negativos.")
                continue

            if minimo > maximo:
                print("El minimo no puede ser mayor que el maximo.")
                continue

            break

        except ValueError:

            print("Debe ingresar numeros enteros.")

    return [
        p for p in paises
        if minimo <= p["poblacion"] <= maximo
    ]


def filtrar_superficie(paises):

    while True:

        try:

            minimo = int(input("Minimo: "))
            maximo = int(input("Maximo: "))

            if minimo < 0 or maximo < 0:
                print("Los valores no pueden ser negativos.")
                continue

            if minimo > maximo:
                print("El minimo no puede ser mayor que el maximo.")
                continue

            break

        except ValueError:

            print("Debe ingresar numeros enteros.")

    return [
        p for p in paises
        if minimo <= p["superficie"] <= maximo
    ]


def ordenar_paises(paises):

    print("1-Nombre")
    print("2-Poblacion")
    print("3-Superficie")

    while True:

        opcion = input("Opcion: ")

        if opcion in ["1", "2", "3"]:
            break

        print("Opcion invalida.")

    while True:

        orden = input(
            "Ascendente(A) Descendente(D): "
        ).strip().upper()

        if orden in ["A", "D"]:
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