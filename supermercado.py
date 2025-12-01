def productoMasCaro(productos):
  #Variables para ir guardando el producto con mayor precio encontrado
  producto_mas_caro = ""
  precio_max = -1.0 #Comienza en -1 para asegurarnos de que cualquier precio sea mayor

  # El parámetro 'productos' ya es el objeto del archivo abierto
  for linea in productos: #Recorremos cada línea del archivo
    partes = linea.strip().split(',') #Eliminamos salto de línea y separamos por comas

    nombre = partes[1].strip() #Obtenemos el nombre del producto (columna 2 del csv)
    precio = float(partes[2].strip())

    #Si este producto tiene un precio mayor al máximo visto
    if precio > precio_max:
        precio_max = precio #Actualizamos el precio máximo
        producto_mas_caro = nombre #Guardamos el nombre del producto más caro

  print(f"El producto más caro es: {producto_mas_caro}") #Mostramos el resultado por pantalla

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def valorTotalBodega(productos):
  #Acumulador para el valor total de la bodega
  total_bodega = 0.0

  # El parámetro 'productos' ya es el objeto del archivo abierto
  for linea in productos: #Recorrer cada línea del archivo
      partes = linea.strip().split(',') #Eliminar saltos de línea y dividir la línea por comas

      precio = float(partes[2].strip()) #Obtener el precio del producto (columna 3) y convertirlo a float
      cantidad = int(partes[3].strip()) #Obtener la cantidad disponible del producto (columna 4) y convertirla a entero

      total_bodega += precio * cantidad #Calcular el valor total de ese producto (precio × cantidad)

  print(f"El valor total de la bodega es: ${total_bodega:,.2f}") #Mostrar el valor total acumulado, formateado con separador de miles y dos decimales
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Zoé Sebriant, Jeshua Useche, Daniel Ghersi
#Programación y base de datos
#17-11-2025
#3D

import csv

def identificar_producto_mas_caro_simple():
  #Diccionario donde se guardarán los productos cargados desde productos.csv
  #Formato: { id_producto : { 'nombre': ..., 'precio': ... } }
    productos_data = {}

    #Cargar productos (productos.csv, separador: ,)
    #Se utiliza ',' como separador (delimiter=',')
    with open('productos.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')

        #Recorrer cada fila del archivo CSV
        for row in reader:
           #Extraer valores de la fila
            id_producto = row[0].strip()  #ID del producto
            nombre = row[1].strip() #Nombre del producto
            precio = float(row[2].strip()) #Convertir el precio a número (float)

            #Guardar los datos del producto en el diccionario
            productos_data[id_producto] = {'nombre': nombre, 'precio': precio}

    #Encontrar el ID del producto más caro
    #max() evalúa los precios usando una función lambda
    id_mas_caro = max(productos_data, key=lambda id_p: productos_data[id_p]['precio'])
    #Obtener el nombre y precio del producto más caro
    nombre_mas_caro = productos_data[id_mas_caro]['nombre']
    precio_mas_caro = productos_data[id_mas_caro]['precio']

    # Mostrar el resultado
    print(f"El producto más caro es {nombre_mas_caro} con un precio de ${precio_mas_caro:,.2f}.")

#Punto de entrada del programa
#Si se ejecuta este archivo directamente, se llama a la función
if __name__ == "__main__":
    identificar_producto_mas_caro_simple()

#--------------------------------------------------------------------------------------------------------------------------------------------------------

    #Zoé Sebriant, Jeshua Useche, Daniel Ghersi
#Programación y base de datos
#17-11-2025
#3D

def totalVentasDelMes(año, mes, items, productos, ventas):
  import csv
   #Cargar precios de productos desde productos.csv
   #El diccionario 'precios' guardará: { id_producto : precio }


precios = {}

# Abrimos el archivo productos.csv (separado por comas)
with open('productos.csv', 'r', encoding='utf-8') as f:
    for linea in f:
        partes = linea.strip().split(',') #Quitamos saltos de línea y dividimos por coma
        precios[partes[0]] = float(partes[2])

#Identificar ID de ventas de 10/2010 (ventas.csv)
MES, ANIO = 10, 2010 #Se fija el mes y año que se desean buscar
ventas_del_mes = set() #Usamos un set para almacenar los ID de ventas del mes/año
with open('ventas.csv', 'r', encoding='utf-8') as f: #Usamos un set para almacenar los ID de ventas del mes/año
    reader = csv.reader(f, delimiter=';')
    for row in reader: #row[0] = id_venta
            #row[1] = fecha en formato dd-mm-aaaa
        fecha_parts = row[1].strip().split('-') #Separamos la fecha por guiones

            #fecha_parts[1] = mes
            #fecha_parts[2] = año
            #Si coincide con el mes y año buscados, guardamos la venta
        if int(fecha_parts[1]) == MES and int(fecha_parts[2]) == ANIO:
            ventas_del_mes.add(row[0].strip())

#Sumar el total (items.csv)
total = 0.0
with open('items.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader: #row[0] = id_venta
            #row[1] = id_producto
            #row[2] = cantidad

        if row[0].strip() in ventas_del_mes: #Verificamos si este item pertenece a una venta del mes
            id_prod = row[1].strip()
            cantidad = int(row[2].strip())
            total += precios[id_prod] * cantidad #Sumamos precio * cantidad
#mostrar resultado
print(f"Total de ventas para {MES:02d}/{ANIO}: ${total:,.2f}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------

#Zoé Sebriant, Jeshua Useche, Daniel Ghersi
#Programación y base de datos
#17-11-2025
#3D

import csv

SEPARADOR = ';'                 #Separador usado por los archivos CSV de items
ARCHIVO_INFORME = 'informe.txt' #Archivo donde se escribirá el reporte final
MES_BUSCADO = 10                #Mes para el cual se desean calcular ingresos
ANIO_BUSCADO = 2010             #Año para el cual se desean calcular ingresos



#Función principal: generar_reporte_compacto()
#Encargada de cargar archivos, analizar datos y generar informe.


def generar_reporte_compacto():


    #CARGA DE PRODUCTOS DESDE productos.csv (separado por coma)
    #Estructura esperada: id_producto, nombre, precio, cantidad
    #Se guarda en un diccionario así:
    #productos = {
    #"1001": {"nombre": "Leche", "precio": 1200, "cant": 40},
    #    ...
    # }
    productos = {}
    with open('productos.csv', 'r', encoding='utf-8') as f:
        for linea in f:
            partes = linea.strip().split(',')
            id_p = partes[0]  #ID del producto

            #Cada producto se almacena como un diccionario
            productos[id_p] = {
                'nombre': partes[1],
                'precio': float(partes[2]),
                'cant': int(partes[3])
            }


    #DETERMINAR EL PRODUCTO MÁS CARO
    #Se usa max() con una función lambda para comparar precios
    id_max_precio = max(productos, key=lambda id: productos[id]['precio'])
    nombre_caro = productos[id_max_precio]['nombre']


    #CALCULAR EL VALOR TOTAL DE INVENTARIO (BODEGA)
    #Se multiplica precio * cantidad para cada producto
    valor_bodega = sum(p['precio'] * p['cant'] for p in productos.values())


    #CALCULAR INGRESOS POR PRODUCTO DESDE items.csv

    #items.csv tiene formato:
    #id_venta ; id_producto ; cantidad
    #Se usará para sumar ingresos totales por producto.
    ingresos_por_producto = {}

    with open('items.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=SEPARADOR)

        next(reader)  #Se omite la fila de encabezado si existe

        for row in reader:
            id_p = row[1]               #ID del producto en el ítem
            cantidad = int(row[2])      #Cantidad vendida
            precio = productos[id_p]['precio']

            #ingreso = precio por cantidad vendida
            ingreso = precio * cantidad

            #Se suma al total acumulado del producto
            ingresos_por_producto[id_p] = ingresos_por_producto.get(id_p, 0) + ingreso


    #PRODUCTO QUE GENERÓ MÁS INGRESOS

    id_max_ingreso = max(ingresos_por_producto, key=ingresos_por_producto.get)
    nombre_ingresos = productos[id_max_ingreso]['nombre']
    ingresos_total = ingresos_por_producto[id_max_ingreso]


    #GENERACIÓN DEL INFORME DE TEXTO
    #Se arman las líneas del informe en formato legible
    lineas = [
        "--- REPORTE DE GESTION SOOS ---",
        "\n============================================\n",
        f"1. Producto más caro: **{nombre_caro}**.",
        f"2. Producto con más ingresos: **{nombre_ingresos}**.",
        f"3. Valor total de inventario: **${valor_bodega:,.2f}**.",
        f"4. Total de ingresos ({MES_BUSCADO:02d}/{ANIO_BUSCADO}): **${ingresos_total:,.2f}**.",
        "\n============================================\n"
    ]

    #Se escribe todo en el archivo informe.txt
    with open(ARCHIVO_INFORME, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lineas))

    #Se retorna un mensaje indicando éxito
    return f" **¡Informe generado con éxito!** Se ha creado el archivo '{ARCHIVO_INFORME}'."
#Código principal que ejecuta la función si el archivo se corre
#directamente desde Python (no cuando se importa como módulo)
if __name__ == "__main__":
    print(generar_reporte_compacto())