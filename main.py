from pokedex import mostrar_catalogo_disponible
from abc import ABC, abstractmethod

#crear la base abstracta "pokemon"
class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima, tipo):
        self.nombre = nombre
        self.tipo = tipo
        #protegemos estos atributos con _
        self._hp_maximo = hp_maximo
        self._energia_maxima = energia_maxima

#crear 4 clases hijas en otro archivo
    @property
    def hp_actual(self):
        return self.hp_actual
    @hp_actual.setter
    def hp_actual(self, valor):
        # Validación, no bajar de 0 ni subir del maximo
        if valor < 0:
            self._hp_actual = 0
        elif valor > self._hp_maximo:
            self._hp_actual = self._hp_maximo
        else:
            self._hp_actual = valor
    @property
    def energia_actual(self, valor):
        return self.energia_actual
    @energia_actual.setter
    def energia_actual(self):
        pass

class Jugador:
    def __init__(self, numero_jugador, pokemon_seleccionado=None):
        self.numero_jugador = numero_jugador
        self.pokemon_seleccionado = pokemon_seleccionado


    def seleccion_pokemon(self):
            self.pokemon_seleccionado = input(f"Jugador {self.numero_jugador}, elija el número de su Pokémon: ")
            return self.pokemon_seleccionado

jugador1=Jugador(1)
jugador2=Jugador(2)
charmander = Pokemon("Charmander", 100, 100, 50, 50, "Fuego")
vulpix = Pokemon("Vulpix", 90, 90, 60, 60, "Fuego")
squirtle = Pokemon("Squirtle", 110, 110, 45, 45, "Agua")
psyduck = Pokemon("Psyduck", 95, 95, 55, 55, "Agua")
bulbasaur = Pokemon("Bulbasaur", 105, 105, 50, 50, "Planta")
oddish = Pokemon("Oddish", 90, 90, 60, 60, "Planta")
pikachu = Pokemon("Pikachu", 80, 80, 70, 70, "Electrico")
magnemite = Pokemon("Magnemite", 75, 75, 80, 80, "Electrico")

print(f"\n{'╔' + '='*100 + '╗'}\n║{">>> SIMULADOR DE BATALLAS POKEMON <<<":^100}║\n{'╚' + '='*100 + '╝'}")
print(f"{'Escriba salir para cerrar el juego.':>100}")
print(f"\n\t{'SELECCIONE MODO DE JUEGO:':<100}\n\t[1] Jugador vs Jugador\n\t[2] Jugador vs Computadora\n{'='*102}")

while True:
    opcion = input(f"\tIngrese modo de juego (1 o 2): \t")
    if opcion == "1":
        mostrar_catalogo_disponible()
        jugador1.seleccion_pokemon()
        print(jugador1.pokemon_seleccionado)
        jugador2.seleccion_pokemon()
        print(jugador2.pokemon_seleccionado)
        break
    elif opcion == "2":
        pass
    elif opcion == "salir":
        break
    else:
        print("")

#mostrar_catalogo_disponible()

