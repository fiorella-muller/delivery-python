ZONAS = {
    1: {"nombre": "Centro", "costo_envio": 800},
    2: {"nombre": "Zona Norte", "costo_envio": 1200},
    3: {"nombre": "Zona Sur", "costo_envio": 1200},
    4: {"nombre": "Zona Este", "costo_envio": 1500},
    5: {"nombre": "Zona Oeste", "costo_envio": 1500},
}


def mostrar_zonas():
    print("\n===== ZONAS DE REPARTO =====")
    for id_zona, datos in ZONAS.items():
        print(f"  [{id_zona}] {datos['nombre']:<12} - Envío: $ {datos['costo_envio']}")
    print("=============================\n")


def zona_existe(id_zona):
    return id_zona in ZONAS


def obtener_zona(id_zona):
    return ZONAS.get(id_zona)
