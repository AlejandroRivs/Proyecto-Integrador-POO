from pokedex import mostrar_catalogo_disponible, CATALOGO_POKEMON
from abc import ABC, abstractmethod
from random import randint
#uso de * para importar todo ya que en ese archivo solo existen esas 4 clases
from pokemon_clases import *


#crear la base abstracta "pokemon"
class Pokemon(ABC):
    def __init__(self, nombre, tipo, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.tipo = tipo
        #protegemos estos atributos con _
        self._hp_actual = hp_actual
        self._hp_maximo = hp_maximo
        self._energia_actual = energia_actual
        self._energia_maxima = energia_maxima
    #metodo abstracto para que cada clase hija tenga su propia implementacion de ataque
    @abstractmethod
    def atacar(self, pokemon_enemigo):
        pass
    
    #crear 4 clases hijas en pokemon_clases.py

    @property
    def hp_actual(self):
        return self._hp_actual  #atributoprivado
    
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
    def energia_actual(self):
        return self._energia_actual  #atributoprivado 
        # Validación, no bajar de 0 ni subir del maximo

    @energia_actual.setter
    def energia_actual(self, valor):
        # Validación, no bajar de 0 ni subir del maximo
        if valor < 0:
            self._energia_actual = 0
        elif valor > self._energia_maxima:
            self._energia_actual = self._energia_maxima
        else:
            self._energia_actual = valor

class Jugador:
    def __init__(self, numero_jugador, pokemon_seleccionado=None):
        self.numero_jugador = numero_jugador
        self.pokemon_elegido = pokemon_seleccionado


    def seleccionar_pokemon(self):
        while True:
            if self.numero_jugador == 3:
                opcion_catalogo = str(randint(1, len(CATALOGO_POKEMON)))
            else:
                opcion_catalogo = input(f"\n\tJugador {self.numero_jugador}, elija el número de su Pokémon: ")
            #vamos a crear un diccionario con las clases para aligerar el codigo y prepararnos en caso de agregar mas tipos.
            clases_por_tipo = {"Agua": PokemonAgua, "Fuego": PokemonFuego, "Planta": PokemonPlanta, "Electrico": PokemonElectrico}

            for clave in CATALOGO_POKEMON:
                if opcion_catalogo == clave:
                    #datos nos ayuda a acceder a la informacion del pokemon seleccionado, y tipo nos ayuda a instanciar la clase correcta segun el tipo del pokemon
                    datos = CATALOGO_POKEMON[clave]
                    tipo = datos["tipo"]
                    #usamos el tipo como llave para obtener la clase
                    clase_pokemon = clases_por_tipo[tipo]
                    #reducimos los if a una sola linea usando la clase obtenida del diccionario
                    self.pokemon_elegido = clase_pokemon(datos["nombre"], datos["tipo"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos['energia_maxima'])
                    print(f"\n\t\tJugador {self.numero_jugador}, ha seleccionado a {datos['nombre']} como su pokemon.")
                    return self.pokemon_elegido
                
            print(f"Debe ingresar un numero valido entre 1 y {len(CATALOGO_POKEMON)}")
            
            if opcion_catalogo == "salir":
                break
    
    def atacar(self, pokemon_enemigo, multiplicador):
        self.pokemon_elegido.energia_actual -= 10
        pokemon_enemigo.hp_actual -= (10 * multiplicador)
        print(f"{self.pokemon_elegido.nombre} ha atacado a {pokemon_enemigo.nombre} con un ataque normal. {pokemon_enemigo.nombre} pierde 10 HP y {self.pokemon_elegido.nombre} pierde 10 EP.")

jugador1=Jugador(1)
jugador2=Jugador(2)
jugador_pc=Jugador(3)

print(f"\n{'╔' + '='*100 + '╗'}\n║{">>> SIMULADOR DE BATALLAS POKEMON <<<":^100}║\n{'╚' + '='*100 + '╝'}")
print(f"{'Escriba salir para cerrar el juego.':>100}")
print(f"\n\t{'SELECCIONE MODO DE JUEGO:':<100}\n\t[1] Jugador vs Jugador\n\t[2] Jugador vs Computadora\n{'='*102}")

while True:
    opcion = input(f"\tIngrese modo de juego (1 o 2): \t")
    if opcion == "1":
        mostrar_catalogo_disponible()
        jugador1.seleccionar_pokemon()
        jugador2.seleccionar_pokemon()
        break
    elif opcion == "2":
        mostrar_catalogo_disponible()
        jugador1.seleccionar_pokemon()
        jugador_pc.seleccionar_pokemon()
        break
    elif opcion == "salir":
        break
    else:
        print("")

#mostrar_catalogo_disponible()

