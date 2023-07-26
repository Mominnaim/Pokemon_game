class game_engine(object):

    def __init__(self,fire,player):
        self.player = player
        self.fire = fire
    def play(self):
        choose_pokemon = input("what pokemon would you like to choose \n1.\tCharmander\n")
        
        if choose_pokemon == "1":
            self.player.collect_pokemon(charmander)
    
class Player(object):

    def __init__(self,bagpack):
        self.bagpack = bagpack

    def collect_pokemon(self,pokemon):
        for key,value in pokemon.items():
            who = key.name
            print("You have collected a", who,"with a",value, "health")
            self.bagpack.append(pokemon)
            print(self.bagpack)

    def evolve_pokemon(self):
        pass

class Fire:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return "No attack defined for this Pokemon."


class Charmander(Fire):
    def __init__(self, name):
        super().__init__(name)
        

    def attack(self):
        return "Ember"


class Charmeleon(Charmander,):
    def __init__(self, name):
        super().__init__(name)


    def attack(self):
        return "Flamethrower"


class Charizard(Charmeleon):
    def __init__(self, name):
        super().__init__(name)


    def attack(self):
        return "Fire Blast"


fire_charmander = Charmander("Charmander")
charmander = {fire_charmander:100}

fire_charmeleon = Charmeleon("Charmeleon")
charmeleon = {fire_charmeleon:200}

fire_charizard = Charizard("Charizard")
charizard = {fire_charizard:300}



bagpack = []
basic_list = []
naim = Player(bagpack)
fire_type_pokemon = Fire(charmander) # need to find a way to pass in a collection of pokemon.
light = game_engine(fire_type_pokemon,naim)

light.play()

#when I go home need to be able to add attacks,attack_limit, find a way to evolve