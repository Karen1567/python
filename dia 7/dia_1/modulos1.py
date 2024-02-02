## ----------------Funciones---------
## funciones con parametros y con retorno 
def suma(a, b):
    return a +  b
result = suma(5, 5)
print("la suma de 5+5 es ",result)

## funcion sin parametros y sin retorno
def saludar():
    print("hola")

## funcion con parametro y sin retorno 
def holaConNombre(name):
  print("Hola " + name + "!")
holaConNombre("Dani")

## funcion sin parametros y con retorno 
def mesa():
    año = int(input("¿en que año naciste?"))
    return año
print("el año en que naciste es: ",mesa())