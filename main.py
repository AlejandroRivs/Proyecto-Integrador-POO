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
    def energia_actual(self):
        return self.energia_actual
    @hp_actual.setter
    def hp_actual(self):
        pass
    @energia_actual.setter
    def energia_actual(self):
        pass
