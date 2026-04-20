from pokedex import mostrar_catalogo_disponible, CATALOGO_POKEMON
from abc import ABC, abstractmethod

#crear la base abstracta "pokemon"
class Pokemon(ABC):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima, tipo):
        self.nombre = nombre
        self.tipo = tipo
        #protegemos estos atributos con _
        self._hp_actual = hp_actual
        self._hp_maximo = hp_maximo
        self._energia_actual = energia_actual
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
        return self.hp_actual
    @property
    def energia_actual(self, valor):
        # Validación, no bajar de 0 ni subir del maximo
        if valor < 0:
            self._energia_actual = 0
        elif valor > self._energia_maxima:
            self._energia_actual = self._energia_maxima
        else:
            self._energia_actual = valor
        return self.energia_actual
    @energia_actual.setter
    def energia_actual(self):
        return self.energia_actual

class Jugador:
    def __init__(self, numero_jugador, pokemon_seleccionado=None):
        self.numero_jugador = numero_jugador
        self.pokemon_seleccionado = pokemon_seleccionado


    def seleccion_pokemon(self):
        while True:
            opcion_catalogo = input(f"Jugador {self.numero_jugador}, elija el número de su Pokémon: ")
            for clave in CATALOGO_POKEMON:
                if opcion_catalogo == clave:
                    datos = CATALOGO_POKEMON[clave]
                    self.pokemon_seleccionado = Pokemon(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos['energia_maxima'], datos["tipo"])
                    print(f"Seleccionaste a {datos['nombre']} como tu pokemon.")
                    return self.pokemon_seleccionado
            print(f"Debe ingresar un numero valido entre 1 y {len(CATALOGO_POKEMON)}")
            if opcion_catalogo == "salir":
                break

    
    def atacar(self, pokemon_enemigo, multiplicador):
        self.pokemon_seleccionado.energia_actual -= 10
        pokemon_enemigo.hp_actual -= (10 * multiplicador)
        print(f"{self.pokemon_seleccionado.nombre} ha atacado a {pokemon_enemigo.nombre} con un ataque normal. {pokemon_enemigo.nombre} pierde 10 HP y {self.pokemon_seleccionado.nombre} pierde 10 EP.")

jugador1=Jugador(1)
jugador2=Jugador(2)
jugador_pc=Jugador(2)

print(f"\n{'╔' + '='*100 + '╗'}\n║{">>> SIMULADOR DE BATALLAS POKEMON <<<":^100}║\n{'╚' + '='*100 + '╝'}")
print(f"{'Escriba salir para cerrar el juego.':>100}")
print(f"\n\t{'SELECCIONE MODO DE JUEGO:':<100}\n\t[1] Jugador vs Jugador\n\t[2] Jugador vs Computadora\n{'='*102}")

while True:
    opcion = input(f"\tIngrese modo de juego (1 o 2): \t")
    if opcion == "1":
        jugador1.seleccion_pokemon()
        jugador2.seleccion_pokemon()
        break
    elif opcion == "2":
        jugador1.seleccion_pokemon()
        jugador_pc.seleccion_pokemon()
        break
        pass
    elif opcion == "salir":
        break
    else:
        print("")

#mostrar_catalogo_disponible()

