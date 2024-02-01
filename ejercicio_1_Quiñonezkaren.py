#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO

diccionario = {"arroz":2500,"leche":3000,"juguitodecaja":5000}
for llave,valor in diccionario.items():
    print (llave,valor)
a=str(input(""))
if a=="arroz":
    c=int(input(""))
    b=2500*c
    print(b)
    if a=="leche":
        c=int(input(""))
        b=3000*c
        print(b)
        if a=="juguitodecaja":
            c=int(input(""))
            b=5000*c
            print(b)
        else:
            print("el producto no existe")
            
    