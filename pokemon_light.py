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
        print("You have collected a", pokemon.name)
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
        self.hp = 100

    def attack(self):
        return "Ember"


class Charmeleon(Charmander):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 200


    def attack(self):
        return "Flamethrower"


class Charizard(Charmeleon):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 300


    def attack(self):
        return "Fire Blast"


charmander = Charmander("Charmander")
charmeleon = Charmeleon("Charmeleon")
charizard = Charizard("Charizard")



bagpack = []
naim = Player(bagpack)
fire_type_pokemon = Fire(charmander) # need to find a way to pass in a collection of pokemon.
light = game_engine(fire_type_pokemon,naim)

light.play()

#when I go home need to be able to add attacks,attack_limit, find a way to evolve