#crear 4 clases importando la clase "Pokemon"  (desde main) como padre
daño = 10
multiplicador = 1
from main import Pokemon
class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima, tipo):
        super().__init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima, tipo)
        
    def atacar(self, pokemon_enemigo):
        if isinstance(pokemon_enemigo, PokemonFuego):
            multiplicador = 2
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final

class PokemonFuego(Pokemon):
    def atacar(self, pokemon_enemigo):
        if isinstance(pokemon_enemigo, PokemonPlanta):
            multiplicador = 2
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final

class PokemonPlanta(Pokemon):
    def atacar(self, pokemon_enemigo):
        if isinstance(pokemon_enemigo, PokemonAgua):
            multiplicador = 2
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final

class PokemonElectrico(Pokemon):
    pass