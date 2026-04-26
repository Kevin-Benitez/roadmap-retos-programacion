"""
Operadores
"""

# operadores aritmeticos
print(f"Suma: 10 + 3 = {10 + 3} ")
print(f"Resta: 10 - 3 = {10 - 3} ")
print(f"División: 10 / 3 = {10 / 3} ")
print(f"Multiplicación: 10 * 3 = {10 * 3} ")
print(f"Módulo: 10 % 3 = {10 % 3} ")
print(f"Exponente: 10 ** 3 = {10 ** 3} ")
print(f"División entera: 10 // 3 = {10 // 3} ")

# operadores de comparación
print(f"igualdad: 10 == 3 es {10 == 3} ")
print(f":desigualdad 10 != 3 es {10 != 3} ")
print(f"mayor que: 10 > 3 es {10 > 3} ")
print(f"menor que: 10 < 3 es {10 < 3} ")
print(f"mayor o igual que: 10 >= 3 es {10 >= 3} ")
print(f"menor o igual que: 10 <= 3 es {10 <= 3} ")

#operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ") #ambas correctas
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 and 5 - 1 == 4} ") #una de las dos correctas
print(f"NOT !: not 10 + 3 == 14  es {not 10 + 3 == 14} ") #confirma una negación

#operadores de asignación
print(my_number)
my_number += 1 #suma y asignación
print(my_number)
my_number -= 1 #resta y división
print(my_number)
my_number *= 1 #multiplicación y asignación
print(my_number)
my_number /= 1 #división y asignación
print(my_number)
my_number %= 1 #módulo y asignación
print(my_number)
my_number **= 1 #exponente y asignación
print(my_number)
my_number //= 1 #división entera y asignación
print(my_number)

#operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

#operadores de pertenencia
print(f"'v' in 'Kevin' = {'v' in 'Kevin'}")
print(f"'w' not in 'Kevin' = {'w' not in 'Kevin'}")

#operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 || 3 = {10 || 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = { 10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = { 10 << 2}") # 101000

"""
estructuras de control
"""
#condicionales
my_string = "KevinDev"

if my_string == "KevinDev":
  print("my_string es 'KevinDev'")
elif my_string == "Rodrigo":
  print("my_string es 'Rodrigo'")
else:
  print("my_string no es 'KevinDev'")
  
#iterativas
for i in range(11):
  print(i)

i = 0
while i <= 10:
  print(i)
  i += 1

#manejo de excepciones
try:
  print(10 / 0)
  except:
  print("Se ha producido un error")
finally:
print("Ha finalizado el manejo de excepciones")

"""
extra
"""
for number in range(10, 56):
  if number % 2 == 0 and number != 16 and number % 3 != 0
  print(number)



