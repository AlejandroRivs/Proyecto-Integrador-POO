#crear 4 clases importando la clase "Pokemon"  (desde main) como padre
from random import randint
from main import Pokemon
daño = 20
class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        
    def atacar(self, pokemon_enemigo):
        multiplicador = 1

        from pokemon_clases import PokemonFuego # Import local para evitar circularidad

        if isinstance(pokemon_enemigo, PokemonFuego):
            multiplicador *= 2
            print(f"\tEs super efectivo !")

        if pokemon_enemigo.defendiendo:
            print(f"\n\t{pokemon_enemigo.nombre} se ha defendido y redujo el daño a la mitad.")
            multiplicador *= 0.5

        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        print(f"\n\t{self.nombre} ha atacado a {pokemon_enemigo.nombre} causando {daño_final} puntos de daño.")
        return daño_final

class PokemonFuego(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        
    def atacar(self, pokemon_enemigo):
        multiplicador = 1

        from pokemon_clases import PokemonPlanta # Import local para evitar circularidad

        if isinstance(pokemon_enemigo, PokemonPlanta):
            multiplicador *= 2
            print(f"\tEs super efectivo !")

        if pokemon_enemigo.defendiendo:
            print(f"\n\t{pokemon_enemigo.nombre} se ha defendido y redujo el daño a la mitad.")
            multiplicador *= 0.5

        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        print(f"\n\t{self.nombre} ha atacado a {pokemon_enemigo.nombre} causando {daño_final} puntos de daño.")
        return daño_final
    
class PokemonPlanta(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
        
    def atacar(self, pokemon_enemigo):
        multiplicador = 1

        from pokemon_clases import PokemonAgua # Import local para evitar circularidad

        if isinstance(pokemon_enemigo, PokemonAgua):
            multiplicador *= 2
            print(f"\tEs super efectivo !")

        if pokemon_enemigo.defendiendo:
            print(f"\n\t{pokemon_enemigo.nombre} se ha defendido y redujo el daño a la mitad.")
            multiplicador *= 0.5

        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        print(f"\n\t{self.nombre} ha atacado a {pokemon_enemigo.nombre} causando {daño_final} puntos de daño.")
        return daño_final

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_maximo,energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)
    def atacar(self, pokemon_enemigo): 
        multiplicador = 1
        
        if pokemon_enemigo.defendiendo:
            print(f"\t{pokemon_enemigo.nombre} se ha defendido y reduce el daño a la mitad.")
            multiplicador = 0.5
        daño_final = daño * multiplicador
        pokemon_enemigo.hp_actual -= daño_final
        paralizar = randint(1, 5)  # 20% de probabilidad de paralizar
        if paralizar == 1:
            #se paraliza al enemigo y se le asigna el atributo "paralizado" como True para que pierda su próximo turno
            print(f"\n\t¡{pokemon_enemigo.nombre} ha sido paralizado y perderá su próximo turno!")
            pokemon_enemigo.paralizado = True
        print(f"\t{self.nombre} ha atacado a {pokemon_enemigo.nombre} causando {daño_final} puntos de daño.")
        return daño_final