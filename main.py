from pokedex import mostrar_catalogo_disponible
from abc import ABC, abstractmethod
#crear la base abstracta "pokemon"
class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hp_actual = hp_actual
        self.hp_maximo = hp_maximo
        self.energia_actual = energia_actual
        self.energia_maxima = energia_maxima
    @abstractmethod
    def atacar(self, pokemon_enemigo):
        pass
#crear 4 clases hijas en otro archivo

    @property
    def hp_actual(self):
        return self.hp_actual
    @property
    def energia_actual(self):
        return self.energia_actual
    @hp_actual.setter
    def hp_actual(self):
        pass
    @energia_actual.setter
    def energia_actual(self):
        pass

print(f"\n{'╔' + '='*100 + '╗'}\n║{">>> SIMULADOR DE BATALLAS POKEMON <<<":^100}║\n{'╚' + '='*100 + '╝'}")
print(f"{'Escriba salir para cerrar el juego.':>100}")
print(f"\n\t{'SELECCIONE MODO DE JUEGO:':<100}\n\t[1] Jugador vs Jugador\n\t[2] Jugador vs Computadora\n{'='*102}")

while True:
    opcion = input(f"\tIngrese modo de juego (1 o 2): \t")
    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion.lower == "salir":
        break
    else:
        print("")

#mostrar_catalogo_disponible()

