diccionario = {"arroz":2500,"leche":3000,"juguitodecaja":5000}
for llave,valor in diccionario.items():
    print (llave,valor)
a=str(input(""))
if a=="arroz":
    c=int(input(""))
    b=2500*c
    print(b)
elif a=="leche":
    c=int(input(""))
    b=3000*c
    print(b)
elif a=="juguitodecaja":
    c=int(input(""))
    b=5000*c
    print(b)
else:
    print("el producto no existe")
            
    