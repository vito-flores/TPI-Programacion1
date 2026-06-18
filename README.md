# TPI-Programacion1
# Gestión de Datos de Países en Python

Trabajo Práctico Integrador de Programación I - UTN

## Integrantes

- Flores Vito
- Ivan Lomoc

## Funcionalidades

## Gestión de países
Agregar un país.
Actualizar información de un país.
Buscar países por nombre.
Mostrar información almacenada.

## Filtros
Filtrar por continente.
Filtrar por rango de población.
Filtrar por rango de superficie.

## Ordenamientos
Ordenar por nombre.
Ordenar por población.
Ordenar por superficie.
Orden ascendente y descendente.

## Estadísticas
País con mayor población.
País con menor población.
Promedio de población.
Promedio de superficie.
Cantidad de países por continente.

## Requisitos

Python 3.10 o superior

## Ejecución

python main.py

## Tecnologías

- Python
- CSV
- Listas
- Diccionarios

## Estructura del proyecto

TPI_Paises_UTN/
|
|-- main.py
|-- paises.csv
|-- README.md
|-- informe.pdf
|
|-- modulos/
    |-- __ininit__.py
    |-- archivos.py
    |-- estadisticas.py
    |-- filtros.py
    |-- paises.py
    |-- validaciones.py

## Instrucciones

## Formato del archivo CSV

El archivo debe contener las siguientes columnas:

nombre,poblacion,superficie,continente
Argentina,46234830,2780400,America
Brasil,211140729,8515767,America
Japon,123294513,377975,Asia

## Ejemplo de uso
1 - Agregar país
2 - Actualizar país
3 - Buscar país
4 - Filtrar países
5 - Ordenar países
6 - Mostrar estadísticas
0 - Salir

## 1 - Agregar país

Entrada:

Ingrese el nombre del país: Canadá
Ingrese la población del país: 40100000
Ingrese la superficie del país: 9984670
Ingrese el continente del país: America

Salida esperada:

País agregado correctamente.

## 2 - Actualizar país

Entrada:

Ingrese el nombre del país a actualizar: Chile
Ingrese la nueva población del país: 20000000
Ingrese la nueva superficie del país: 756102
Ingrese el nuevo continente del país: America

Salida esperada:

País actualizado correctamente.

## 3 - Buscar país

Entrada:

Ingrese el nombre del país a buscar: Argentina

Salida esperada:

Nombre: Argentina
Población: 46234830
Superficie: 2780400 km²
Continente: America

## 4 - Filtrar países

Entrada:

Ingrese el continente: Europa

Salida esperada:

Alemania
Francia
España
Italia

## 5 - Ordenar países

Entrada:

Ordenar por: población
Tipo de orden: descendente

Salida esperada:

India
China
Brasil
México
Argentina

## 6 - Mostrar estadísticas

Salida esperada:

País con mayor población: India
País con menor población: Uruguay

Promedio de población: 237841357
Promedio de superficie: 2586170

Cantidad de países por continente:

America: 5
Europa: 4
Asia: 4
Africa: 1
Oceania: 1

## 0 - Salir

Salida esperada:

Gracias por utilizar el sistema de gestión de países.

## Instalación
1-Clonar el repositorio:
git clone https://github.com/vito-flores/TPI-Programacion1

2-Ingresar al directorio:
cd TPI_Paises_UTN

3-Ejecutar el programa:
python main.py

## Video

[video explicativo](https://www.youtube.com/watch?v=B6MIDQw-saE)

## Informe PDF

[Programación I – UTN TUPaD – Trabajo Practico Integrador.pdf](https://github.com/user-attachments/files/29072790/Programacion.I.UTN.TUPaD.Trabajo.Practico.Integrador.pdf)

