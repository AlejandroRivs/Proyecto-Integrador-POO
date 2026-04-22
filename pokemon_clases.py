#crear 4 clases importando la clase "Pokemon"  (desde main) como padre
from random import randint
daño = 10
from main import Pokemon
class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        
    def atacar(self, pokemon_enemigo):
        multiplicador = 1
        if isinstance(pokemon_enemigo, PokemonFuego):
            multiplicador = 2
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        return daño_final

class PokemonFuego(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
    def atacar(self, pokemon_enemigo):
        multiplicador = 1
        if isinstance(pokemon_enemigo, PokemonPlanta):
            multiplicador = 2
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        return daño_final

class PokemonPlanta(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
    def atacar(self, pokemon_enemigo):
        multiplicador = 1
        if isinstance(pokemon_enemigo, PokemonAgua):
            multiplicador = 2
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        return daño_final

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
    def atacar(self, pokemon_enemigo):
        multiplicador = 1
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        paralizar = randint(1, 5)  # 20% de probabilidad de paralizar
        if paralizar == 1:
            print(f"{pokemon_enemigo.nombre} ha sido paralizado y no podrá atacar en el próximo turno.")
            pokemon_enemigo.paralizado = True
        return daño_final