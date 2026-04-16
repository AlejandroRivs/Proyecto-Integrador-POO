#crear 4 clases importando la clase "Pokemon"  (desde main) como padre
from main import Pokemon
class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        # Super llama al constructor de la clase padre (Pokemon)
        super().__init__(nombre, hp_maximo, energia_maxima, "Agua")
    def atacar(self, pokemon_enemigo):
        pass
class PokemonFuego(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima, "Fuego")
    def atacar(self, pokemon_enemigo):
        pass
class PokemonPlanta(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima, "Planta")
    def atacar(self, pokemon_enemigo):
        pass
class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima, "Electrico")
    def atacar(self, pokemon_enemigo):
        pass