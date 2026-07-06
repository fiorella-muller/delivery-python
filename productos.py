CATALOGO = {
    1: {"nombre": "Hamburguesa Simple", "categoria": "Comidas", "precio": 3500},
    2: {"nombre": "Hamburguesa Doble", "categoria": "Comidas", "precio": 4800},
    3: {"nombre": "Pizza Muzzarella", "categoria": "Comidas", "precio": 6500},
    4: {"nombre": "Pizza Especial", "categoria": "Comidas", "precio": 8200},
    5: {"nombre": "Papas Fritas", "categoria": "Acompañamientos", "precio": 2200},
    6: {"nombre": "Aros de Cebolla", "categoria": "Acompañamientos", "precio": 2400},
    7: {"nombre": "Gaseosa 500ml", "categoria": "Bebidas", "precio": 1500},
    8: {"nombre": "Agua Mineral", "categoria": "Bebidas", "precio": 1200},
    9: {"nombre": "Cerveza Artesanal", "categoria": "Bebidas", "precio": 2800},
}


def mostrar_catalogo():
    print("\n===== CATÁLOGO DE PRODUCTOS =====")
    categorias = sorted(set(p["categoria"] for p in CATALOGO.values()))
    for categoria in categorias:
        print(f"\n-- {categoria} --")
        for id_producto, datos in CATALOGO.items():
            if datos["categoria"] == categoria:
                print(f"  [{id_producto}] {datos['nombre']:<20} $ {datos['precio']}")
    print("==================================\n")


def producto_existe(id_producto):
    return id_producto in CATALOGO


def obtener_producto(id_producto):
    return CATALOGO.get(id_producto)
