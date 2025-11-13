#Suma de matrices de 3x3
matriz_a= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
#Crear matriz resultado
resultado = []
#Sumar elemento por elemento
for i in range(3): # 3 filas
    fila = []
    for j in range(3): # 3 columnas
        suma= matriz_a[i][j] + matriz_b[i][j]
        fila.append(suma)

    resultado.append(fila)
#Mostrar resultado
print("Resultado de la suma:")
for fila in resultado:
    for elemento in fila:
        print(elemento, end=" ")
    print()
    


#Creamos las matrices que vamos a restar
matriz_a=[
[10, 15, 20]
[25, 30, 35],
[40, 45, 50]
]
matriz_b = [
[2, 5, 8],
[3, 10, 15],
[5, 20, 25]
]
#Crear una matriz vacía para guardar el resultado
resultado
#Recorre las matrices y restar elemento por elemento
for i in range(3): # 3 filas
    fila () # Crear fila vacia para el resultado
    for j in range(3): # 3 columnas
        resta= matriz_a[i][j] - matriz_b[i][j] # Restar elementos
        fila.append(resta) #Agregar resultado a la fila
    resultado.append(fila) # Agregar fila completa al resultado
#Mostramos las matrices y el resultado
print("Matriz A:")
for elemento in fila:
    for fila in matriz_a:
        print("{elemento:3}", end=" ") # :3 alinea los números
    print()
print("\nMatriz B:")
for fila in matriz_b:
    for elemento in fila:
    print("{elemento:3}", end=" ")
    print()
print("\nResultado (A - B):")
for fila in resultado:
    for elemento in fila:
        print(f"(elemento:3)", end=" ")
    print()

[9:11 AM, 11/13/2025] Fernando Huerta: 21 #Mostramos las matrices y el resultado

22 print("Matriz A:")

for elemento in fila:

25

23 for fila in matriz_a:

24

print("{elemento:3}", end=" ") # :3 alinea los números

26

print()

print("\nMatriz B:")

for fila in matriz_b:

29

Matriz A:

27

10 15 20 25 30 35

28

for elemento in fila:

40 45 50

30

| print("{elemento:3}", end=" ")

Matriz B:

31

print()

258

32

print("\nResultado (A - B):")

33

3 10 15 5 20 25

for fila in resultado:

34

for elemento in fila:

Resultado (A - B):

35

print(f"(elemento:3)", end=" ")

8 10 12 22 20 20 35 25 25

36 print()
matriz = [
[15, 8],
[23, 12]
]
#Empezamos asumiendo que el primero es el mayor
mayor=matriz[0][0] # Empieza con 15
#Recorreremos toda la matriZ
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:#Si encuentre uno más grande
                            # Lo guardo como el nuevo mayor

#Mostramos resultado
print("La matriz es:")
for fila in matriz:
    for elemento in fila:
        print(elemento, ende" ")
    print()
print("\nEl número mayor es: (mayor)")