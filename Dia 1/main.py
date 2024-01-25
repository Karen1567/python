## ---------------------------------
## ------Ejercicio 1 -----------
## -------------------------------

# impresion en consola 
print("hola mundo")

# ----Datos primitivos----
#1. String 
texto = "campus"
print(texto)
print(type(texto))
#2. Int 
numeroEntero = 1
print(numeroEntero)
#3. Float 
numeroDecimal = 3.1
print(numeroDecimal)
#4  Double 
numeroDecimalLargo = 3.12168234783
print(numeroDecimalLargo)
#5  Boolean 
booleano= True 
print(booleano) 

# ----entradas parte del usuario----
entradaUsuario = str(input("ingresa tu nombre"))
print ("tu nombre es: ", entradaUsuario)

# ----entradas parte del usuario con definicion de tipo de dato primitivo----
entradaUsuarioNumero = int(input("ingresa tu edad"))
print ("tu edad es: ", entradaUsuarioNumero)
## ----------ciclos-------
## ciclo for
for i in range (5,10,2):#for contador in range (desde,hasta,pasos):
    print (i)
##ciclo while 
booleanito = True
while booleanito == True:#while condicion_a_cumplir:
    print("sigo vivo") 
    booleanito = False 
## ---------condicionales------------
texto1 = "campus"
if texto1 == "campus":
    print("soy campus")
else:
    print("no soy campus")
    
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
print("el mes en que cumples años es: ",mesa())

nombre_de_estudiantes = ['Alexa', 'Daniela', 'Oliver', 'Paula']
print("el nombre de los estudiantes son:")
print(nombre_de_estudiantes[0])
print(nombre_de_estudiantes[1])
print(nombre_de_estudiantes[2])
print(nombre_de_estudiantes[3])


##------------arreglos--------------



## desarrollado por KAREN DANIELA QUIÑONEZ - 1097496454