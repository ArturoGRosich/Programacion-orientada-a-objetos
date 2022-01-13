#mejor nombre para next_throw, y next_two_trows, ya que next_two, solo es la siguiente de la siguiente,
#no afecta a la siguiente ¿in_two_throws? a lo mejor


class Bowling:
    def __init__(self, game, duration = 10):
        self.in_one_throw = 1  # sirve para multiplicar el valor de la siguiente tirada
        self.in_two_throws = 1 # sirve para llevar la cuenta de la siguiente de la siguiente (para los strikes)
        self.frames_left = duration # es una cueneta atras para reconocer cuando hemos llegado al ultimo frame
        self.score = 0 # puntuacion de la partida
        self.game = game # es el imput, la partida que te pasan
        self.last = 0 # es una variable utilizada para calcular los spares, guarda el valor de la anterior tirada
        self.duration = duration # lo mismo que frames left, pero se guarda entre partidas, de tal modo que solo se cambia una vez
    
    def set_new_game(self, new_game): # ¿duration = self.duration?
        self.game = new_game

    
    def set_game_duration(self, new_duration): # le da opcion al usuario a jugar partidas mas largas o mas cortas 
        self.duration = int(new_duration)

    def get_score(self): # le permite al usuario recuperar el score de la ultima partida
        return self.score
    
    # parte principal del programa donde se usan el resto de funciones para calcular la puntuacion 
    # de la ultima partida introducida
    def calculate_score(self): 
        
        self.frames_left = self.duration        
        
        self.__prepare_game()
        for throw in self.game:

            self.__sum_throw(throw)

            self.__actualice_multipliers(throw)

            self.__is_last_frame(throw)

        return self.score
    
    #actualiza in_one_throw y in_two_throws, para duplicar o triplicar las tiradas 
    # despues de strikes o spares
    def __actualice_multipliers(self, throw):
        self.in_one_throw = self.in_two_throws

        #cuando frames left es uno o menor, significa que queda un frame, y por lo tanto que es el ultimo
        #y en consecuencia desactivamos la parte que aumenta los multiplicadores
        if self.frames_left > 1:      

            ####Mirar de hacer mas comprensible####
            if throw == "x":
                # el strike aumenta un bono de "+ *1" de tal modo de que si ya 
                # teniamos un *2 tendriamos un *3, (dos strikes seguidos)
                self.in_one_throw = self.in_two_throws + 1

                self.in_two_throws = 2
                
            elif throw == "/":
                self.in_one_throw = self.in_two_throws + 1
                self.in_two_throws = 1
        
            else:
                self.in_one_throw = self.in_two_throws
                self.in_two_throws = 1
        
        else:
            self.in_two_throws = 1
    
    # suma una tirada de una partida al score
    def __sum_throw(self, throw):
        
        if throw != "x" and throw != "/":     
            self.score += int(throw) * self.in_one_throw
        elif throw == "x":
            self.score += 10 * self.in_one_throw
        elif throw == "/":
            self.score += (10 - self.last) * self.in_one_throw

        try:
            self.last = int(throw)
        except:
            ""
    
    #cambia la escritura en caso de que el usuario no haya escrito exactamente lo que se espera
    def __prepare_game(self):

        prepared_game = ""
        for letter in self.game:
            if letter == "X":
                prepared_game += "x"
            elif letter == "-":
                prepared_game += "0"
            else:
                prepared_game += letter
        self.game = prepared_game

    #lleva la cuenta de cuantos frames quedan
    def __is_last_frame(self, throw):
        
        #x ocupa un frame entero, el resto solo ocupan medio
        if throw == "x":
            self.frames_left -= 1
        else:
            self.frames_left -= 0.5


