# Sistema de Delivery — Trabajo Final Integrador

**Materia:** Algoritmos y Estructuras de Datos — ISI — Ciclo 2026
**Escenario asignado:** N° 15 — Sistema de Delivery

## Integrantes del grupo
- Lopez, Tomas
- Montenegro, Mateo
- Müller, Fiorella
- Sosa, Mía

## Comisión
k1.1

## Descripción general del sistema

El sistema simula el funcionamiento de un servicio de **delivery de comidas**,
ejecutándose por consola. Permite:

- Registrar pedidos de clientes, seleccionando productos de un catálogo
  organizado por categorías (Comidas, Acompañamientos, Bebidas, Postres).
- Calcular automáticamente el importe del pedido, incluyendo:
  - Subtotal según productos y cantidades.
  - Costo de envío según la zona de reparto elegida.
  - Descuento promocional (10%) para pedidos cuyo subtotal sea mayor o
    igual a $10.000.
- Elegir el medio de pago (Efectivo, Tarjeta o Mercado Pago).
- Gestionar el **estado de cada pedido** a lo largo de su ciclo de vida:
  `Pendiente → En preparación → En camino → Entregado` (o `Cancelado`).
- Consultar el listado completo de pedidos realizados.
- Visualizar **estadísticas de ventas**: total facturado, ticket promedio,
  pedidos entregados/cancelados, ventas por zona y productos más vendidos.

### Estructura del proyecto (modularización)

| Archivo             | Responsabilidad                                              |
|---------------------|----------------------------------------------------------------|
| `main.py`           | Menú principal y flujo de interacción con el usuario         |
| `productos.py`      | Catálogo de productos y funciones de consulta                |
| `zonas.py`          | Zonas de reparto y costos de envío                            |
| `pedidos.py`        | Creación de pedidos, cálculo de importes y control de estados |
| `validaciones.py`   | Funciones genéricas de lectura y validación de datos          |
| `estadisticas.py`   | Acumuladores, contadores y reporte estadístico                |

### Requisitos técnicos cumplidos
- Estructuras condicionales (`if/elif/else`) para validaciones y menús.
- Estructuras repetitivas (`while`, `for`) para la carga de productos,
  reintentos ante errores y recorrido de listados.
- Funciones para modularizar cada responsabilidad del sistema.
- Validaciones de datos ingresados por el usuario (números, texto no
  vacío, opciones dentro de rango, existencia de productos/zonas).
- Acumuladores y contadores (total facturado, cantidad de pedidos,
  ventas por zona, ventas por producto, pedidos entregados/cancelados).
- Manejo básico de errores con `try/except` (por ejemplo, ante el
  ingreso de texto donde se espera un número) y mensajes claros al
  usuario ante datos inválidos.

## Instrucciones de ejecución

1. Tener instalado **Python 3.10** o superior.
2. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd sistema_delivery
   ```
3. Ejecutar el programa:
   ```bash
   python3 main.py
   ```
4. Seguir las instrucciones que aparecen en el menú por consola.

No se requieren librerías externas: el sistema utiliza únicamente
módulos propios y la biblioteca estándar de Python.

## Uso de Inteligencia Artificial

- **Herramienta utilizada:**  ChatGPT, Claude
- **Para qué se utilizó:** para generar la estructura inicial
  del código, resolver dudas puntuales sobre manejo de errores,
  proponer la organización en módulos, asistir en la redacción del
  README, etc.
- **Cómo se utilizó:** se revisó y discutió en equipo
  cada fragmento de código generado antes de incorporarlo, se
  modificaron nombres de variables y lógica para adaptarlo a lo visto
  en clase, se probó manualmente cada funcionalidad, etc.


