"""
Sistema de Delivery - Trabajo Final Integrador
Algoritmos y Estructuras de Datos - ISI - Ciclo 2026

Escenario 15: Sistema de Delivery
Permite gestionar pedidos, calcular importes, controlar
entregas y visualizar estadísticas de ventas y zonas de reparto.
"""
from datetime import datetime

import productos
import zonas
import pedidos
import estadisticas
from validaciones import leer_entero, leer_texto_no_vacio, leer_si_no

MEDIOS_DE_PAGO = {1: "Efectivo", 2: "Tarjeta de débito/crédito", 3: "Mercado Pago"}

HORA_APERTURA = 10
HORA_CIERRE = 23

def dentro_del_horario_de_atencion():
    """Devuelve True si la hora actual está dentro del horario de atención."""
    hora_actual = datetime.now().hour
    return HORA_APERTURA <= hora_actual < HORA_CIERRE

def mostrar_menu_principal():
    print("\n========== SISTEMA DE DELIVERY ==========")
    print("1. Realizar un pedido")
    print("2. Ver todos los pedidos")
    print("3. Cambiar estado de un pedido")
    print("4. Ver estadísticas de ventas")
    print("5. Salir")
    print("==========================================")


def seleccionar_medio_de_pago():
    """Muestra las opciones de pago y devuelve la elegida."""
    print("\nMedios de pago disponibles:")
    for id_medio, nombre in MEDIOS_DE_PAGO.items():
        print(f"  [{id_medio}] {nombre}")
    opcion = leer_entero("Seleccione un medio de pago: ", minimo=1, maximo=len(MEDIOS_DE_PAGO))
    return MEDIOS_DE_PAGO[opcion]


def armar_items_del_pedido():
    """
    Permite al usuario agregar productos al pedido de forma repetida
    hasta que decida finalizar la carga. Devuelve la lista de items.
    """
    items = []
    productos.mostrar_catalogo()

    while True:
        id_producto = leer_entero("Ingrese el número de producto a agregar: ")

        if not productos.producto_existe(id_producto):
            print("  Error: no existe un producto con ese número. Intente nuevamente.")
            continue

        cantidad = leer_entero("Ingrese la cantidad: ", minimo=1)
        producto = productos.obtener_producto(id_producto)
        items.append((id_producto, cantidad, producto["nombre"], producto["precio"]))
        print(f"  Agregado: {producto['nombre']} x{cantidad}")

        if not leer_si_no("¿Desea agregar otro producto? (S/N): "):
            break

    return items

def opcion_realizar_pedido():
    """Flujo completo para cargar un nuevo pedido en el sistema."""
    if not dentro_del_horario_de_atencion():
        print(
            f"\nLo sentimos, el horario de atención es de {HORA_APERTURA}:00 "
            f"a {HORA_CIERRE}:00 hs. Intente nuevamente más tarde.\n"
        )
        return

    print("\n--- NUEVO PEDIDO ---")
    cliente = leer_texto_no_vacio("Ingrese el nombre del cliente: ")

    items = armar_items_del_pedido()
    if not items:
        print("El pedido no contiene productos. Se cancela la operación.\n")
        return

    zonas.mostrar_zonas()
    id_zona = leer_entero("Seleccione la zona de reparto: ", minimo=1, maximo=len(zonas.ZONAS))
    while not zonas.zona_existe(id_zona):
        print("  Error: zona inválida.")
        id_zona = leer_entero("Seleccione la zona de reparto: ", minimo=1, maximo=len(zonas.ZONAS))

    medio_pago = seleccionar_medio_de_pago()

    pedido = pedidos.crear_pedido(cliente, items, id_zona, medio_pago)

    print("\n¡Pedido registrado con éxito!")
    pedidos.mostrar_pedido(pedido)


def opcion_ver_pedidos():
    print("\n--- LISTADO DE PEDIDOS ---")
    pedidos.mostrar_todos_los_pedidos()


def opcion_cambiar_estado():
    print("\n--- CAMBIAR ESTADO DE PEDIDO ---")

    if not pedidos.lista_pedidos:
        print("No hay pedidos cargados en el sistema.\n")
        return

    id_pedido = leer_entero("Ingrese el número de pedido: ", minimo=1)

    print("\nEstados disponibles:")
    for indice, estado in enumerate(pedidos.ESTADOS_VALIDOS, start=1):
        print(f"  [{indice}] {estado}")

    opcion = leer_entero(
        "Seleccione el nuevo estado: ", minimo=1, maximo=len(pedidos.ESTADOS_VALIDOS)
    )
    nuevo_estado = pedidos.ESTADOS_VALIDOS[opcion - 1]

    exito, mensaje = pedidos.cambiar_estado(id_pedido, nuevo_estado)
    print(f"\n{mensaje}\n")


def opcion_ver_estadisticas():
    estadisticas.mostrar_estadisticas()


def main():
    """Función principal: controla el ciclo de vida del programa."""
    print("Bienvenido/a al Sistema de Delivery")

    while True:
        mostrar_menu_principal()
        opcion = leer_entero("Seleccione una opción: ", minimo=1, maximo=5)

        if opcion == 1:
            opcion_realizar_pedido()
        elif opcion == 2:
            opcion_ver_pedidos()
        elif opcion == 3:
            opcion_cambiar_estado()
        elif opcion == 4:
            opcion_ver_estadisticas()
        elif opcion == 5:
            print("\nGracias por usar el Sistema de Delivery. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()
