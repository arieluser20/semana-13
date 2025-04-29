# Definimos una clase llamada Perro
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo nombre
        self.edad = edad      # atributo edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Crear un objeto de la clase Perro
mi_perro = Perro("Firulais", 3)

# Usar sus métodos
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años.")
mi_perro.ladrar("!Guau!")




import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

# Crear un objeto de tipo Circulo
c1 = Circulo(5)

print(f"El área del círculo es {c1.area():.2f}")




# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} hace un sonido.")

# Clase derivada
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Miau")

# Crear un objeto de la clase Gato
gato1 = Gato("Michi")
gato1.hablar()
Michi dice: Miau

