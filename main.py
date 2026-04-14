from pokedex import mostrar_catalogo_disponible
class Pokemon:
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hp_actual = hp_actual
        self.hp_maximo = hp_maximo
        self.energia_actual = energia_actual
        self.energia_maxima = energia_maxima
   
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
print(f"\n\t{'SELECCIONE MODO DE JUEGO:':<100}\n\t[1] Jugador vs Jugador\n\t[2] Jugador vs Computadora\n{'='*102}")
opcion = input(f"\tIngrese modo de juego (1 o 2): \t")
#mostrar_catalogo_disponible()


print