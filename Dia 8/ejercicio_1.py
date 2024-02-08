import json
print ("ejercicio 1")
print ("            ")
P=open('Dia 8/datos.json')
miJson=json.load(P)
ventas = miJson.get('ventas')
pedidos = ventas.get('pedidos')

pedidos_ordenados = sorted(pedidos, key=lambda x: x["fecha"], reverse=True)
for i in pedidos_ordenados:
    print(i)
print ("            ")
    

print ("ejercicio 2")
print ("            ")
pedidos_ordenados1 = sorted(pedidos, key=lambda x: x["total"], reverse=True)
print  (pedidos_ordenados1[0])
print  (pedidos_ordenados1[1])
print ("            ")


print ("ejercicio 3")
print ("            ")
pedidos_ordenados2 = set(pedidos,["id_cliente"])
print(pedidos_ordenados2)
print ("            ")

clientes = set()
for pedido in pedidos:
    clientes.add(pedido['id_cliente'])
clientes_con_pedido = list(clientes)
for i in clientes_con_pedido:
    print("id_cliente ",i)







