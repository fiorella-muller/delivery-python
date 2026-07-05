"""
Módulo de pedidos.
Gestiona la creación de pedidos, el cálculo de importes,
la aplicación de descuentos y el control de estados.
"""

import productos
import zonas
import estadisticas

# Estados posibles que puede tener un pedido a lo largo de su ciclo de vida
ESTADOS_VALIDOS = ["Pendiente", "En preparación", "En camino", "Entregado", "Cancelado"]

# Estructura donde se almacenan todos los pedidos del sistema
lista_pedidos = []

MONTO_MINIMO_DESCUENTO = 10000
PORCENTAJE_DESCUENTO = 0.10


def calcular_descuento(subtotal):
    """
    Calcula el descuento aplicable a un pedido.
    Promoción: 10% de descuento en pedidos cuyo subtotal
    sea mayor o igual a $10000.
    """
    if subtotal >= MONTO_MINIMO_DESCUENTO:
        return round(subtotal * PORCENTAJE_DESCUENTO, 2)
    return 0.0


def calcular_promocion_2x1_bebidas(items):
    """
    Promoción 2x1 en bebidas: por cada 2 unidades de un mismo
    producto de la categoría 'Bebidas', se descuenta el valor
    de una unidad.
    """
    descuento_promo = 0.0
    for id_producto, cantidad, nombre_producto, precio_unitario in items:
        producto = productos.obtener_producto(id_producto)
        if producto["categoria"] == "Bebidas":
            unidades_gratis = cantidad // 2
            descuento_promo += unidades_gratis * precio_unitario
    return descuento_promo

def crear_pedido(cliente, items, id_zona, medio_pago):
    """
    Crea un nuevo pedido a partir de los datos ingresados.
    'items' es una lista de tuplas (id_producto, cantidad, nombre_producto, precio_unitario).
    Devuelve el diccionario del pedido creado.
    """
    subtotal = sum(cantidad * precio for _, cantidad, _, precio in items)
    zona = zonas.obtener_zona(id_zona)
    costo_envio = zona["costo_envio"]
    descuento = calcular_descuento(subtotal)
    promo_bebidas = calcular_promocion_2x1_bebidas(items)
    total = subtotal + costo_envio - descuento - promo_bebidas

    pedido = {
        "id": len(lista_pedidos) + 1,
        "cliente": cliente,
        "items": items,
        "zona": zona["nombre"],
        "medio_pago": medio_pago,
        "subtotal": subtotal,
        "envio": costo_envio,
        "descuento": descuento,
        "promo_bebidas": promo_bebidas,
        "total": total,
        "estado": "Pendiente",
    }

    lista_pedidos.append(pedido)
    estadisticas.registrar_nuevo_pedido(pedido, zona["nombre"])
    return pedido


def buscar_pedido(id_pedido):
    """Busca un pedido por su id. Devuelve None si no existe."""
    for pedido in lista_pedidos:
        if pedido["id"] == id_pedido:
            return pedido
    return None


def cambiar_estado(id_pedido, nuevo_estado):
    """
    Cambia el estado de un pedido validando reglas de negocio básicas.
    Devuelve una tupla (exito: bool, mensaje: str).
    """
    pedido = buscar_pedido(id_pedido)

    if pedido is None:
        return False, "No existe ningún pedido con ese número."

    if pedido["estado"] in ("Entregado", "Cancelado"):
        return False, (
            f"El pedido ya se encuentra '{pedido['estado']}' y no puede modificarse."
        )

    if nuevo_estado not in ESTADOS_VALIDOS:
        return False, "Estado inválido."

    pedido["estado"] = nuevo_estado
    estadisticas.registrar_cambio_estado(nuevo_estado)
    return True, "El estado del pedido fue actualizado correctamente."


def mostrar_pedido(pedido):
    """Imprime en consola el detalle completo de un pedido."""
    print(f"\n----- Pedido N° {pedido['id']} -----")
    print(f"Cliente     : {pedido['cliente']}")
    print(f"Zona        : {pedido['zona']}")
    print(f"Medio de pago: {pedido['medio_pago']}")
    print("Detalle:")
    for id_producto, cantidad, nombre_producto, precio_unitario in pedido["items"]:
        print(f"{nombre_producto} x{cantidad} = $ {cantidad * precio_unitario:.2f}")
        print(f"Subtotal    : $ {pedido['subtotal']:.2f}")
        print(f"Envío       : $ {pedido['envio']:.2f}")
        print(f"Descuento   : $ {pedido['descuento']:.2f}")
        print(f"Promo 2x1 bebidas: $ {pedido['promo_bebidas']:.2f}")
        print(f"TOTAL       : $ {pedido['total']:.2f}")
        print(f"Estado      : {pedido['estado']}")
        print("-----------------------------\n")


def mostrar_todos_los_pedidos():
    """Muestra por consola todos los pedidos cargados en el sistema."""
    if not lista_pedidos:
        print("\nAún no se registraron pedidos en el sistema.\n")
        return

    for pedido in lista_pedidos:
        mostrar_pedido(pedido)
