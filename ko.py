# Lista de pedidos de ejemplo
lista_pedidos = [
    {"id": 1, "fecha_realizacion": "2024-01-20", "producto": "Producto A"},
    {"id": 2, "fecha_realizacion": "2024-01-15", "producto": "Producto B"},
    {"id": 3, "fecha_realizacion": "2024-01-25", "producto": "Producto C"}
]

# Ordenar la lista de pedidos por fecha de realización (de más reciente a más antigua)
lista_pedidos_ordenados = sorted(lista_pedidos, key=lambda x: x["fecha_realizacion"], reverse=True)

# Mostrar la lista de pedidos ordenados
for pedido in lista_pedidos_ordenados:
    print(pedido)
