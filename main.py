from pokedex import mostrar_catalogo_disponible, CATALOGO_POKEMON
from abc import ABC, abstractmethod
from random import randint


#crear la base abstracta "pokemon"
class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        #protegemos estos atributos con _
        self.__hp_maximo = hp_maximo
        self.__hp_actual = hp_maximo
        self.__energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima
        self.paralizado = False  # Atributo para indicar si el Pokémon está paralizado
        self.defendiendo = False  # Atributo para indicar si el Pokémon está defendiendo

    #metodo abstracto para que cada clase hija tenga su propia implementacion de ataque
    @abstractmethod
    def atacar(self, pokemon_enemigo):
        pass
    #crear 4 clases hijas en pokemon_clases.py

    @property
    def hp_maximo(self):
        return self.__hp_maximo #atributoprivado
    
    @property
    def hp_actual(self):
        return self.__hp_actual  #atributoprivado
    
    @hp_actual.setter
    def hp_actual(self, valor):
        # Validación, no bajar de 0 ni subir del maximo
        if valor < 0:
            self.__hp_actual = 0
        elif valor > self.__hp_maximo:
            self.__hp_actual = self.__hp_maximo
        else:
            self.__hp_actual = valor
    
    @property
    def energia_actual(self):
        return self.__energia_actual  #atributoprivado 

    @energia_actual.setter
    def energia_actual(self, valor):
        # Validación, no bajar de 0 ni subir del maximo
        if valor < 0:
            self.__energia_actual = 0
        elif valor > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        else:
            self.__energia_actual = valor
    
    @property
    def energia_maxima(self):
        return self.__energia_maxima #atributoprivado


class Jugador:
    def __init__(self, numero_jugador, pokemon_seleccionado=None):
        self.numero_jugador = numero_jugador
        self.pokemon_elegido = pokemon_seleccionado

    def seleccionar_pokemon(self):
        #importacion local para evitar problemas de importacion |
        from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico

        while True:
            #jugador 3 indica que es la pc
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
                    self.pokemon_elegido = clase_pokemon(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])
                    print(f"\n\t\tJugador {self.numero_jugador}, ha seleccionado a {datos['nombre']} como su pokemon.")
                    return self.pokemon_elegido
                
            print(f"Debe ingresar un numero valido entre 1 y {len(CATALOGO_POKEMON)}")
            
            if opcion_catalogo == "salir":
                break
    
class SimuladorPokemon:
    def __init__(self):
        self.jugador1 = Jugador(1)
        self.jugador2 = Jugador(2)
        self.jugador_pc = Jugador(3)
        self.opcion = ""

    #creamos un metodo para mostrar el catalogo ordenado ya que el metodo de pokedex.py no se adapta a nuestro formato
    @staticmethod
    
    def mostrar_catalogo_ordenado():
        print(f"\n{' POKÉDEX DISPONIBLE ':=^{102}}")
        
        # Usamos el for sobre las llaves del diccionario
        for clave in CATALOGO_POKEMON:
            datos = CATALOGO_POKEMON[clave]
            print(f"{f'[{clave}]':<3} | {datos['nombre']:<15} | {f'Tipo: {datos['tipo']}':<15} | {f'HP: {datos['hp_maximo']}':<10} | {f'EP: {datos['energia_maxima']}':<10}".center(102))        
            
        print("=" * 102)
    @staticmethod
    
    def mostrar_encabezado():
        pokemon_logo = r"""
                                                     ,'\
                       _.----.        ____         ,'  _\   ___    ___     ____
                   _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
                   \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
                    \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
                      \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
                       \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
                        \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
                         \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
                          \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
                           \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                                   `'                            '-._|
                        """

        print(pokemon_logo)
        print(f"\n{'╔' + '='*100 + '╗'}\n║{">>> SIMULADOR DE BATALLAS POKEMON <<<":^100}║\n{'╚' + '='*100 + '╝'}")
        print(f"\n\t{'SELECCIONE MODO DE JUEGO:':<100}\n\t[1] Jugador vs Jugador\n\t[2] Jugador vs Computadora\n")
    
    def iniciar_batalla(self, jugador1, jugador2):
        print(f"\n{'╔' + '='*100 + '╗'}\n║{">>> ¡COMIENZA LA BATALLA! <<<":^100}║\n{'╚' + '='*100 + '╝'}")
        combate = f"{jugador1.pokemon_elegido.nombre} vs {jugador2.pokemon_elegido.nombre}"
        print(f"{'╔' + '='*100 + '╗'}")
        print(f"║{combate:^100}║")
        print(f"{'╚' + '='*100 + '╝'}")
        costo_ataque = 15
        costo_defensa = 5
        aumento_descanso = 20

        while jugador1.pokemon_elegido.hp_actual > 0 and jugador2.pokemon_elegido.hp_actual > 0:   
            for jugador in [jugador1, jugador2]:
                # un if para determinar quien es el jugador actual y quien el oponente
                oponente = jugador2 if jugador == jugador1 else jugador1

                # verificar hp's antes de cada ciclo
                if oponente.pokemon_elegido.hp_actual <= 0:
                    break

                # Creamos un bucle interno para que no pierda el turno por error de dedo o falta de energía
                accion_completada = False
                while not accion_completada:
                    print(f"{'╔' + '='*100 + '╗'}")
                    print(f"\tTurno del jugador {jugador.numero_jugador}: {jugador.pokemon_elegido.nombre} \n\t(HP: {jugador.pokemon_elegido.hp_actual}/{jugador.pokemon_elegido.hp_maximo}, EP: {jugador.pokemon_elegido.energia_actual}/{jugador.pokemon_elegido.energia_maxima})\n")
                    
                    # validacion de parálisis y defensa antes del input para evitar inputs innecesarios
                    if jugador.pokemon_elegido.paralizado:
                        print(f"\n\t{jugador.pokemon_elegido.nombre} está paralizado y pierde su turno.")
                        jugador.pokemon_elegido.paralizado = False  # Se quita la parálisis después de perder un turno
                        accion_completada = True # El turno se consume por parálisis
                        continue  # Salta el turno del jugador paralizado

                    if jugador.pokemon_elegido.defendiendo:
                        print(f"\n\t{jugador.pokemon_elegido.nombre} está defendiendo y recibirá menos daño en este turno.")
                        jugador.pokemon_elegido.defendiendo = False  # Se quita el modo defensa después de un turnol     
                    
                    # en caso que el jugador sea la computadora(jugador 3)
                    if jugador.numero_jugador == 3:
                        opcion_batalla = randint(1, 3)  # La computadora elige aleatoriamente entre atacar, defender o descansar
                        print(f"\tLa computadora elige la opcion {opcion_batalla}")
                    else:
                        print(f"\t[1] Atacar (costo: {costo_ataque} EP) \n\t[2] Defender (costo: {costo_defensa} EP)\n\t[3] Descansar (restaura: {aumento_descanso} EP)\n")
                        print(f"{'╚' + '='*100 + '╝'}")
                        try:
                            print(f"{'╔' + '='*100 + '╗'}")
                            opcion_batalla = int(input(f"\tIngrese la accion (1, 2 o 3) para {jugador.pokemon_elegido.nombre}: "))   
                            print(f"{'╚' + '='*100 + '╝'}")   
                        except ValueError:
                            print("\tPor favor, ingrese un número válido (1, 2 o 3).")
                            continue # Vuelve a preguntar sin saltar de jugador              
            
                    if opcion_batalla == 1:

                        if jugador.pokemon_elegido.energia_actual >= costo_ataque:
                            print(f"{'╔' + '='*100 + '╗'}")
                            jugador.pokemon_elegido.atacar(oponente.pokemon_elegido)
                            jugador.pokemon_elegido.energia_actual -= costo_ataque
                            accion_completada = True # Acción exitosa
                            print(f"{'╚' + '='*100 + '╝'}")
                        else:
                            print(f"{'╔' + '='*100 + '╗'}")
                            print(f"\t\tNo tienes suficiente energía para atacar. Necesitas al menos {costo_ataque} EP.")
                            print(f"{'╚' + '='*100 + '╝'}") 
                    
                    elif opcion_batalla == 2:
                        if jugador.pokemon_elegido.energia_actual >= costo_defensa:
                            jugador.pokemon_elegido.defendiendo = True
                            jugador.pokemon_elegido.energia_actual -= costo_defensa
                            print(f"{'╔' + '='*100 + '╗'}")
                            print(f"\t{jugador.pokemon_elegido.nombre} esta en modo defensa, recibira menos daño en el siguiente turno.")
                            print(f"{'╚' + '='*100 + '╝'}") 
                            accion_completada = True # Acción exitosa
                        else:
                            print(f"{'╔' + '='*100 + '╗'}")
                            print(f"\t\tNo tienes suficiente energía para defender. Necesitas al menos {costo_defensa} EP.")
                            print(f"{'╚' + '='*100 + '╝'}")

                    elif opcion_batalla == 3:
                        jugador.pokemon_elegido.energia_actual += aumento_descanso
                        print(f"{'╔' + '='*100 + '╗'}")
                        print(f"\t{jugador.pokemon_elegido.nombre} ha descansado y recupera {aumento_descanso} EP.")
                        print(f"{'╚' + '='*100 + '╝'}")
                        accion_completada = True # Acción exitosa
                    else:
                        print(f"{'╔' + '='*100 + '╗'}") 
                        print("\n\t\t\t!!! Opción no válida. Elija 1, 2 o 3.!!!\n")
                        print(f"{'╚' + '='*100 + '╝'}")

                #verificar hp luego de cada accion para evitar acciones ilogicas
                if oponente.pokemon_elegido.hp_actual <= 0:
                    print(f"\n\t{oponente.pokemon_elegido.nombre} se ha debilitado.")
                    print(f"\n{'╔' + '='*100 + '╗'}\n║{f'¡El jugador {jugador.numero_jugador} ha ganado la batalla con {jugador.pokemon_elegido.nombre}!':^100}║\n{'╚' + '='*100 + '╝'}")
                    return  
        
    def menu(self):
        self.mostrar_encabezado()     
        while True:
            print(f"{'Escriba salir para cerrar el juego.':>100}")
            opcion = input(f"\tIngrese modo de juego (1 o 2): \t")    

            if opcion == "1":
                self.mostrar_catalogo_ordenado()
                self.jugador1.seleccionar_pokemon()
                self.jugador2.seleccionar_pokemon()
                self.iniciar_batalla(self.jugador1, self.jugador2)
            elif opcion == "2":
                self.mostrar_catalogo_ordenado()
                self.jugador1.seleccionar_pokemon()
                self.jugador_pc.seleccionar_pokemon()
                self.iniciar_batalla(self.jugador1, self.jugador_pc)
            elif opcion == "salir":
                print("¡Gracias por jugar! ¡Hasta la próxima!")
                break
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 'salir'.")
            

if __name__ == "__main__":
    simulador = SimuladorPokemon()
    simulador.menu()
