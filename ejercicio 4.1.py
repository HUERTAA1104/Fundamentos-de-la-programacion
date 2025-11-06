print("Ejercicio 1 con while")

#Inicializamos una variable contador
contador_numero = 1

#Mientras contador sea menor o igual a 5
while contador_numero <=5:    
    print(f"Numero: {contador_numero}")
    contador_numero = contador_numero + 1 #Incrementamos el contador
print("\nEjercicio 2 con while - cuenta regresiva")
# Inicializamos el contador en 5
numero = 5

# Mientras el número sea mayor que 0
while numero > 0:
    print(f"Faltan {numero} segundos...")
    numero = numero - 1  # Decrementamos el contador

print("¡Despegue!")
print("\nEjercicio 3 con while - suma acumulativa")
# Inicializamos las variables
numeros = 1
suma = 0

# Mientras numeros sea menor o igual a 50
while numeros <= 50:
    suma = suma + numeros   # Acumulamos la suma
    numeros = numeros + 1   # Incrementamos el contador

print(f"La suma del 1 al 50 es: {suma}\n")


print("\nEjercicio 4 - Tabla de Multiplicar")
# Inicializamos el contador
multiplicador = 1

# Mientras el multiplicador sea menor o igual a 10
while multiplicador <= 10:
    resultado = 7 * multiplicador
    print(f"7 x {multiplicador} = {resultado}")
    multiplicador = multiplicador + 1

print("¡Tabla completa! \n")
print("\nEjercicio 5 - Números pares del 2 al 50")
# Inicializamos el contador en 2 (primer par)
numeros_pares = 2

# Mientras el número sea menor o igual a 50
while numeros_pares <= 50:
    print(f"Número par: {numeros_pares}")
    numeros_pares = numeros_pares + 2  # Incrementamos de 2 en 2

print("¡Todos los pares mostrados!\n")
print("\nEjercicio 6 - Dividir un número a la mitad")
# Inicializamos con un número
numero_a_dividir = 100

print("\nEjercicio 1: Tabla de multiplicar")
numero = 5
for i in range (1, 11):
resultado = numero * i
print(f"(numero) x {i} = (resultado")
print ("\nEjercicio 2")
numeros = [10, 20, 30, 40, 50]
suma =0
for num in numeros:
suma += num
print(f"La suma total es: {suma}")
texto = "Alo, que haciendo mi gente en miercoles"
contador = 0
for letra in texto:
if letra. lower() in "aeiou":
contador += 1
print(f"Hay (contador) vocales")
print("\nEjercicio 1: Tabla de multiplicar")

numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")



print("\nEjercicio 2")
numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
print(f"La suma total es: {suma}")



print("\nEjercicio 3: Contar vocales")
texto = "Alo, que haciendo mi gente en miercoles"
contador = 0
for letra in texto:
    if letra.lower() in "aeiou":
        contador += 1
print(f"Hay {contador} vocales")



print("\nEjercicio 4")

numeros = [15, 42, 8, 23, 67, 31]
mayor = numeros[0]  # Empezamos con el primero de la lista
for num in numeros:
    if num > mayor:
        mayor = num
print(f"El número mayor es: {mayor}")



print("\nEjercicio 5")

cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)
print(cuadrados)

print("\nEjercicio 1")
canciones = ["As it was","Flowers", "Vampire" , "Cruel summer" , "Calm down"]
print("MIS CANCIONES FAVORITAS:")
print(canciones[0])
print(canciones[1])
print(canciones[2])
print(canciones[3])
print(canciones[4])



print("\nEjercicio 2\n")
amigos = []

print ("Lista inicial:", amigos)

amigos.append ("Andrea")
print("Despues de agregar a Andrea:", amigos)

amigos.append ("Meli")
print("Despues de agregar a Meli:", amigos)

amigos.append ("Xime")
print("Despues de agregar a Xime:", amigos)

print(f"\nTotal de amigos: {len(amigos)}")



print("\nEjercicio 3\n")
calificaciones = [98, 90, 92, 89]

#Mostrar todas las calificaciones
print("Tus calificaciones:", calificaciones)

#Calcular el promedio
suma = sum(calificaciones)
promedio = suma / len(calificaciones)
print(f"Promedio: {promedio}")

#Encontrar la mejor y peor calificacion
mejor = max(calificaciones)
peor = min(calificaciones)
print(f"Mejor calificacion: {mejor}")
print(f"Peor calificacion: {peor}")

print("\nEjercicio 4\n")
carrito = []
# Agregar productos
print("🛍️ Agregando productos al carrito...")
carrito.append("iPhone 15")
carrito.append("AirPods")
carrito.append("Funda")
carrito.append("Cargador")

print("Carrito actual:", carrito)
print(f"Productos en el carrito: {len(carrito)}")

# Decidiste que no quieres la funda
print("\n❌ Eliminando la funda...")
carrito.remove("Funda")

print("Carrito final:", carrito)
print(f"Total de productos: {len(carrito)}")



print("\nEjercicio 5\n")

videojuegos = ["Minecraft", "Fortnite", "Valorant", "Roblox", "GTA V"]

print("🎮 MI TOP 5 DE VIDEOJUEGOS:")
print(videojuegos)

# Mostrar el primero y el último
print(f"\nMi favorito (posición 0): {videojuegos[0]}")
print(f"El de la posición 5 (último): {videojuegos[-1]}")

# Cambiar mi juego favorito
print("\n🔄 Cambio de opinión...")
videojuegos[0] = "Apex Legends"

print("Top 5 actualizado:")
print(videojuegos)


print("\nEjercicio 6\n")
series = ["Stranger Things", "Wednesday", "The Last of Us"]

print("📺 Series para ver:", series)

# Agregar una nueva serie
series.append("One Piece")
print("Agregaste One Piece:", series)

# Verificar si una serie está en tu lista
if "Wednesday" in series:
    print("\n✅ Sí tienes Wednesday en tu lista")

if "Breaking Bad" in series:
    print("Tienes Breaking Bad")
else:
    print("❌ No tienes Breaking Bad en tu lista")

# Ya viste la primera serie, la eliminas
print(f"\n¡Terminaste de ver! {series[0]}!")
series.pop(0)
print("Series restantes:", series)