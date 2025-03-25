"""
Paso 1: Crear Arrays con Datos de Ventas

Usa la librería numpy para crear los siguientes arrays:
meses: un array con los nombres de los meses del año.
ventas_A, ventas_B, ventas_C: arrays que representan las ventas mensuales de tres productos diferentes.

Paso 2: Estadísticas Básicas

Calcula la media y la suma de ventas para los productos A, B y C usando las funciones de NumPy.
Imprime estos valores en el formato siguiente:
Media de ventas Producto A: <valor>
Suma de ventas Producto A: <valor>
Repite para los productos B y C.

Paso 3: Manipulación y Análisis de Datos

Total de ventas por mes: Suma las ventas de los tres productos para cada mes.
Promedio de ventas por producto: Calcula el promedio de ventas por producto.
Mes con mayor y menor ventas: Identifica qué mes tuvo el total de ventas más alto y cuál el más bajo usando las funciones np.argmax y np.argmin.

Paso 4: Operaciones Avanzadas con NumPy

Reshape y Transposición:

Crea una matriz 2D con las ventas de los tres productos y transforma su forma (reshape) a un array tridimensional con dimensiones (3, 4, 3).
Transpone la matriz de ventas para que las filas se conviertan en columnas.
Invertir arrays: Invierte las ventas de cada producto en orden de meses.
Aplanar la matriz: Convierte la matriz de ventas a un array unidimensional.

Paso 5: Análisis de Elementos Únicos

Utiliza np.unique para encontrar los elementos únicos en los datos de ventas y cuenta cuántas veces aparece cada uno.

Paso 6: Indexación y Slicing

Ventas del primer trimestre: Extrae las ventas de los tres primeros meses del año.
Indexación booleana: Selecciona los meses donde el total de ventas de los tres productos supere los 800.
Selección avanzada: Usa una lista de índices para seleccionar las ventas de los meses pares (o selecciona los meses a tu elección) y muestra esas ventas en una nueva matriz.
"""

import numpy as np

# Paso 1: Crear Arrays con Datos de Ventas
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
ventas_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
ventas_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
ventas_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])

# Paso 2: Estadísticas Básicas

# Media de ventas y suma de ventas para los productos A, B y C
mediaA = np.mean(ventas_A)
sumaA = np.sum(ventas_A)
mediaB = np.mean(ventas_B)
sumaB = np.sum(ventas_B)        
mediaC = np.mean(ventas_C)
sumaC = np.sum(ventas_C)
print(f'Media de ventas y Suma Producto A: {mediaA} y {sumaA}')
print(f'Media de ventas y Suma Producto B: {mediaB} y {sumaB}') 
print(f'Media de ventas y Suma Producto C: {mediaC} y {sumaC}')

# Paso 3: Manipulación y Análisis de Datos

# Total de ventas por mes
ventas_total = ventas_A + ventas_B + ventas_C
# Promedio de ventas por producto
promedio= np.mean([ventas_A, ventas_B, ventas_C], axis=1)
# Mes con mayor y menor ventas
mes_max=meses[np.argmax(ventas_total)]
mes_min=meses[np.argmin(ventas_total)]
print(f'Total de ventas por mes: {ventas_total}')
print(f'Promedio de ventas por producto: {promedio}')
print(f'Mes con mayor venta: {mes_max}')
print(f'Mes con menor venta: {mes_min}')

# Paso 4: Operaciones Avanzadas con NumPy       