# Trabajo Final Integrador - Laboratorio de Python

# Algoritmos y Estructuras de Datos - IS

# Escenario 12: Gestión de supermercado
# Diccionario global de productos.
# Cada producto tiene nombre, precio, stock, unidades vendidas
# y si tiene o no una promoción simple.
productos = {
    1: {
        "nombre": "Arroz 1kg",
        "precio": 1800.0,
        "stock": 30,
        "vendidos": 0,
        "promo": False
    },
    2: {
        "nombre": "Leche 1L",
        "precio": 1200.0,
        "stock": 25,
        "vendidos": 0,
        "promo": True
    },
    3: {
        "nombre": "Fideos 500g",
        "precio": 1500.0,
        "stock": 35,
        "vendidos": 0,
        "promo": True
    },
    4: {
        "nombre": "Aceite 900ml",
        "precio": 3200.0,
        "stock": 20,
        "vendidos": 0,
        "promo": False
    },
    5: {
        "nombre": "Azucar 1kg",
        "precio": 1700.0,
        "stock": 28,
        "vendidos": 0,
        "promo": False
    },
    6: {
        "nombre": "Yerba 1kg",
        "precio": 4200.0,
        "stock": 18,
        "vendidos": 0,
        "promo": False
    }
}

# Variables globales usadas como acumuladores y contadores.
clientes_atendidos = 0
total_recaudado = 0.0
numero_venta = 1

# Lista global donde se guarda el detalle de cada venta.
historial_ventas = []


def leer_entero(mensaje):
    """
    Lee un número entero validado.
    Si el usuario ingresa letras, el programa no se corta.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 55)
    print("              SISTEMA DE CAJA - SUPERMERCADO")
    print("=" * 55)
    print("1. Cargar nueva venta")
    print("2. Ver estadisticas")
    print("3. Ver catalogo")
    print("0. Salir")
    print("=" * 55)


def esperar_salida():
    """
    Deja la pantalla abierta hasta que el usuario ingrese 0.
    Esto evita que la información desaparezca rápido.
    """
    opcion = -1

    while opcion != 0:
        opcion = leer_entero("\nIngrese 0 para volver al menu: ")

        if opcion != 0:
            print("Opcion incorrecta. Para volver debe ingresar 0.")


def mostrar_catalogo():
    """
    Muestra los productos disponibles con precio, stock y promocion.
    """
    print("\n" + "-" * 65)
    print("CATALOGO DE PRODUCTOS")
    print("-" * 65)
    print(
        f"{'Codigo':<8}"
        f"{'Producto':<20}"
        f"{'Precio':>12}"
        f"{'Stock':>10}"
        f"{'Promo':>10}"
    )
    print("-" * 65)

    for codigo, datos in productos.items():
        promo = "2x1" if datos["promo"] else "-"

        print(
            f"{codigo:<8}"
            f"{datos['nombre']:<20}"
            f"${datos['precio']:>11.2f}"
            f"{datos['stock']:>10}"
            f"{promo:>10}"
        )

    print("-" * 65)
    esperar_salida()


def mostrar_catalogo_en_venta():
    """
    Muestra el catalogo dentro del proceso de venta.
    No pide salir, porque se usa solo como referencia.
    """
    print("\n" + "-" * 65)
    print("PRODUCTOS DISPONIBLES")
    print("-" * 65)
    print(
        f"{'Codigo':<8}"
        f"{'Producto':<20}"
        f"{'Precio':>12}"
        f"{'Stock':>10}"
        f"{'Promo':>10}"
    )
    print("-" * 65)

    for codigo, datos in productos.items():
        promo = "2x1" if datos["promo"] else "-"

        print(
            f"{codigo:<8}"
            f"{datos['nombre']:<20}"
            f"${datos['precio']:>11.2f}"
            f"{datos['stock']:>10}"
            f"{promo:>10}"
        )

    print("-" * 65)


def pedir_codigo_producto():
    """
    Pide el codigo del producto.
    El codigo 0 finaliza la carga de productos.
    """
    while True:
        codigo = leer_entero("\nIngrese codigo de producto (0 para terminar): ")

        if codigo == 0:
            return codigo

        if codigo in productos:
            return codigo

        print("El codigo ingresado no existe.")


def pedir_cantidad(codigo):
    """
    Pide una cantidad valida.
    También controla que no se venda más de lo disponible en stock.
    """
    while True:
        cantidad = leer_entero("Ingrese cantidad: ")

        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
        elif cantidad > productos[codigo]["stock"]:
            print("No hay stock suficiente.")
            print(f"Stock disponible: {productos[codigo]['stock']}")
        else:
            return cantidad


def agregar_al_carrito(carrito, codigo, cantidad):
    """
    Agrega productos al carrito.
    Si el producto ya estaba cargado, suma la cantidad.
    """
    if codigo in carrito:
        carrito[codigo] += cantidad
    else:
        carrito[codigo] = cantidad

    productos[codigo]["stock"] -= cantidad


def calcular_total_producto(codigo, cantidad):
    """
    Calcula el total de un producto.
    Si tiene promocion 2x1, se cobra una unidad cada dos productos.

    Ejemplo:
    Si el cliente lleva 5 unidades con promocion:
    5 // 2 = 2 pares
    5 % 2 = 1 unidad restante
    Entonces se cobran 3 unidades.
    """
    precio = productos[codigo]["precio"]

    if productos[codigo]["promo"]:
        cantidad_a_cobrar = cantidad // 2 + cantidad % 2
    else:
        cantidad_a_cobrar = cantidad

    return precio * cantidad_a_cobrar


def calcular_subtotal(carrito):
    """Calcula el subtotal general de la venta."""
    subtotal = 0.0

    for codigo, cantidad in carrito.items():
        subtotal += calcular_total_producto(codigo, cantidad)

    return subtotal


def calcular_descuento(subtotal):
    """
    Aplica un descuento del 10% si la compra supera los $10000.
    """
    if subtotal > 10000:
        return subtotal * 0.10

    return 0.0


def imprimir_ticket(carrito, subtotal, descuento, total_final):
    """
    Imprime un ticket simple y prolijo en consola.
    """
    print("\n" + "=" * 70)
    print("                       SUPERMERCADO UTN")
    print("                         TICKET DE COMPRA")
    print("=" * 70)
    print(
        f"{'Producto':<22}"
        f"{'Cant.':>8}"
        f"{'Precio':>12}"
        f"{'Promo':>10}"
        f"{'Total':>14}"
    )
    print("-" * 70)

    for codigo, cantidad in carrito.items():
        nombre = productos[codigo]["nombre"]
        precio = productos[codigo]["precio"]
        promo = "2x1" if productos[codigo]["promo"] else "-"
        total_producto = calcular_total_producto(codigo, cantidad)

        print(
            f"{nombre:<22}"
            f"{cantidad:>8}"
            f"${precio:>11.2f}"
            f"{promo:>10}"
            f"${total_producto:>13.2f}"
        )

    print("-" * 70)
    print(f"{'Subtotal:':<55}${subtotal:>12.2f}")
    print(f"{'Descuento aplicado:':<55}${descuento:>12.2f}")
    print(f"{'Total final:':<55}${total_final:>12.2f}")
    print("=" * 70)
    print("                    Gracias por su compra")
    print("=" * 70)


def guardar_venta_en_historial(carrito, total_final):
    """
    Guarda el detalle de la venta para poder consultarlo en estadisticas.
    """
    global numero_venta

    detalle_venta = []

    for codigo, cantidad in carrito.items():
        detalle_venta.append({
            "producto": productos[codigo]["nombre"],
            "cantidad": cantidad,
            "total_producto": calcular_total_producto(codigo, cantidad)
        })

    venta = {
        "numero": numero_venta,
        "detalle": detalle_venta,
        "total": total_final
    }

    historial_ventas.append(venta)
    numero_venta += 1


def actualizar_estadisticas(carrito, total_final):
    """
    Actualiza los contadores y acumuladores generales.
    """
    global clientes_atendidos
    global total_recaudado

    clientes_atendidos += 1
    total_recaudado += total_final

    for codigo, cantidad in carrito.items():
        productos[codigo]["vendidos"] += cantidad


def cargar_nueva_venta():
    """
    Realiza el proceso completo de una nueva venta.
    Permite cargar varios productos hasta que el usuario ingrese 0.
    """
    carrito = {}

    print("\n" + "=" * 55)
    print("NUEVA VENTA")
    print("=" * 55)

    mostrar_catalogo_en_venta()

    while True:
        codigo = pedir_codigo_producto()

        if codigo == 0:
            break

        cantidad = pedir_cantidad(codigo)
        agregar_al_carrito(carrito, codigo, cantidad)
        print("Producto agregado correctamente.")

    if len(carrito) == 0:
        print("\nNo se cargaron productos. Venta cancelada.")
        esperar_salida()
        return

    subtotal = calcular_subtotal(carrito)
    descuento = calcular_descuento(subtotal)
    total_final = subtotal - descuento

    imprimir_ticket(carrito, subtotal, descuento, total_final)
    actualizar_estadisticas(carrito, total_final)
    guardar_venta_en_historial(carrito, total_final)

    esperar_salida()


def obtener_producto_mas_vendido():
    """
    Calcula cuál fue el producto más vendido del día.
    """
    mayor_cantidad = 0
    producto_mayor = "No hubo ventas"

    for datos in productos.values():
        if datos["vendidos"] > mayor_cantidad:
            mayor_cantidad = datos["vendidos"]
            producto_mayor = datos["nombre"]

    if mayor_cantidad == 0:
        return "No hubo ventas"

    return f"{producto_mayor} ({mayor_cantidad} unidades)"


def mostrar_productos_vendidos():
    """
    Muestra la cantidad vendida de cada producto.
    """
    print("\nPRODUCTOS VENDIDOS")
    print("-" * 55)
    print(f"{'Producto':<25}{'Unidades vendidas':>20}")
    print("-" * 55)

    for datos in productos.values():
        print(f"{datos['nombre']:<25}{datos['vendidos']:>20}")

    print("-" * 55)


def mostrar_historial_ventas():
    """
    Muestra qué se compró en cada venta realizada.
    """
    print("\nHISTORIAL DE VENTAS")
    print("-" * 55)

    if len(historial_ventas) == 0:
        print("Todavia no se realizaron ventas.")
        print("-" * 55)
        return

    for venta in historial_ventas:
        print(f"\nVenta N° {venta['numero']}")
        print("-" * 55)

        for item in venta["detalle"]:
            print(
                f"{item['producto']} - "
                f"Cantidad: {item['cantidad']} - "
                f"Total: ${item['total_producto']:.2f}"
            )

        print(f"Total de la venta: ${venta['total']:.2f}")


def mostrar_estadisticas():
    """
    Muestra las estadisticas generales del sistema.
    """
    print("\n" + "=" * 55)
    print("ESTADISTICAS DEL DIA")
    print("=" * 55)
    print(f"Clientes atendidos: {clientes_atendidos}")
    print(f"Total recaudado: ${total_recaudado:.2f}")
    print(f"Producto mas vendido: {obtener_producto_mas_vendido()}")
    print("=" * 55)

    mostrar_productos_vendidos()
    mostrar_historial_ventas()
    esperar_salida()


def main():
    """
    Funcion principal.
    Mantiene el programa funcionando hasta que el usuario elige salir.
    """
    opcion = -1

    while opcion != 0:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opcion: ")

        if opcion == 1:
            cargar_nueva_venta()

        elif opcion == 2:
            mostrar_estadisticas()

        elif opcion == 3:
            mostrar_catalogo()

        elif opcion == 0:
            print("\nSistema finalizado correctamente.")

        else:
            print("Opcion incorrecta. Intente nuevamente.")


main()
