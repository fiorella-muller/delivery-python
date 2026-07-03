"""
Módulo de estadísticas.
Mantiene acumuladores y contadores que se actualizan a medida
que el sistema procesa pedidos, y permite mostrarlos en pantalla.
"""

# ----- Acumuladores y contadores globales del sistema -----
total_pedidos = 0
total_facturado = 0.0
pedidos_entregados = 0
pedidos_cancelados = 0
ventas_por_zona = {}       # {nombre_zona: monto_acumulado}
ventas_por_producto = {}   # {nombre_producto: cantidad_vendida}


def registrar_nuevo_pedido(pedido, nombre_zona):
    """
    Actualiza los acumuladores y contadores cuando se genera un
    nuevo pedido en el sistema.
    """
    global total_pedidos, total_facturado

    total_pedidos += 1
    total_facturado += pedido["total"]

    ventas_por_zona[nombre_zona] = ventas_por_zona.get(nombre_zona, 0) + pedido["total"]

    for id_producto, cantidad, nombre_producto, precio_unitario in pedido["items"]:
        ventas_por_producto[nombre_producto] = (
            ventas_por_producto.get(nombre_producto, 0) + cantidad
        )


def registrar_cambio_estado(nuevo_estado):
    """Actualiza contadores cuando un pedido cambia de estado."""
    global pedidos_entregados, pedidos_cancelados

    if nuevo_estado == "Entregado":
        pedidos_entregados += 1
    elif nuevo_estado == "Cancelado":
        pedidos_cancelados += 1


def mostrar_estadisticas():
    """Muestra por consola un resumen estadístico del día."""
    print("\n========== ESTADÍSTICAS DEL DÍA ==========")
    print(f"Total de pedidos realizados : {total_pedidos}")
    print(f"Pedidos entregados          : {pedidos_entregados}")
    print(f"Pedidos cancelados          : {pedidos_cancelados}")
    print(f"Total facturado             : $ {total_facturado:.2f}")

    if total_pedidos > 0:
        promedio = total_facturado / total_pedidos
        print(f"Ticket promedio por pedido  : $ {promedio:.2f}")

    if ventas_por_zona:
        print("\n-- Ventas por zona --")
        for zona, monto in ventas_por_zona.items():
            print(f"  {zona:<12}: $ {monto:.2f}")
        zona_top = max(ventas_por_zona, key=ventas_por_zona.get)
        print(f"  Zona con mayor demanda: {zona_top}")

    if ventas_por_producto:
        print("\n-- Productos más vendidos --")
        for producto, cantidad in sorted(
            ventas_por_producto.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {producto:<20}: {cantidad} unidades")
        producto_top = max(ventas_por_producto, key=ventas_por_producto.get)
        print(f"  Producto más vendido: {producto_top}")

    print("===========================================\n")
