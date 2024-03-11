#Imprimir todos los multiplos de 3 que hay entre 1 a 100
Multiplo = 3
while Multiplo < 101:
 print (Multiplo)  
 Multiplo += 3

 #Imprimir los números impares entre 0 a 100

 Impar  = 3 
 while Impar < 101:
  print(Impar)
  Impar +=2

  #Imprimir los números pares del 1 al 100
  Pares = 2 
  while Pares < 101:
   print (Pares)
   Pares += 2
 
 #Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30
  num=1
while num<31:
    cuadrados=num**2
    print(cuadrados)
    num += 1

#Escribir un programa que sume los cuadrados de los nuúmeros del 1 al 100
def sumadecuadrados(n):
    suma = 0
    for x in range(1, n+1):
        suma += x**2
    return suma

resultado = sumadecuadrados(100)
print("La suma de las potencias de los primero 100 numeros es:", resultado)


#Dados dos números naturales, el primero menor que el segundo, generar y mostrar 
#todos los números comprendidos entre ellos en secuencia ascendente. 
def numerosentre(a, b):
    for x in range(a+1, b):
        print(x, end=" ")

a = int(input("Ingrese el primer numero "))
b = int(input("Ingrese el segundo numero mayor al primero: "))

if a>= b:
    print("El primer número debe ser menor que el segundo.")
else:
    print("Los números comprendidos entre", a, "y", b, "son: ")
    numerosentre(a,b)

#Sumar todos números que se digita por teclado mientras no sea cero
def sumanumeros():
    suma = 0
    while True:
        a = float(input("Ingrese un número y cuando quiera terminar de sumar digite 0: "))
        if a == 0:
            break
        suma += a
    return suma

resultado = sumanumeros()
print("La suma de los números ingresados es:", resultado)