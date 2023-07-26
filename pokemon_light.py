class game_engine(object):

    def __init__(self,fire,player):
        self.player = player
        self.fire = fire
    def play(self):
        choose_pokemon = input("what pokemon would you like to choose \n1.\tCharmander\n")
        
        if choose_pokemon == "1":
            self.player.collect_pokemon(charmander)

    def battle_arena(self,pokemon_1,pokemon_2):
        pass
    
class Player(object):

    def __init__(self,bagpack):
        self.bagpack = bagpack

    def collect_pokemon(self,pokemon):
        print("You have collected a", pokemon.name,"with a",pokemon.hp, "health")
        self.bagpack.append(pokemon)
        

    def evolve_pokemon(self):
        pass

class Fire:
    def __init__(self, name,hp):
        self.name = name
        self.hp = hp
    def attack(self):
        return "No attack defined for this Pokemon."


class Charmander(Fire):
    def __init__(self, name, hp):
        super().__init__(name,hp)
        self.attacks = [Ember(),Scratch()]
        self.attacks_limits = {'Ember':3,"Scratch":3}
        
        
    def use_attack(self, attack_name):
        for attack in self.attacks:
            if attack.name == attack_name and self.attack_limit.get(attack_name, 0) > 0:
                self.attack_limit[attack_name] -=1
                return attack.perform_attack()
        return "You have either reached the limit for that attack or entered and invalid attack."




class Charmeleon(Charmander):
    def __init__(self, name, hp):
        super().__init__(name,hp)


    def attack(self):
        return "Flamethrower"


class Charizard(Charmeleon):
    def __init__(self, name, hp):
        super().__init__(name,hp)


    def attack(self):
        return "Fire Blast"

class Attack(object):

    def __init__(self,name,dmg):
        self.name = name
        self.dmg = dmg

    def perform_attack(self,pokemon):
        return f"{pokemon.name} used {self.name} and it does {self.dmg}"

class Ember(Attack):

    def __init__(self):
        super().__init__("Ember",20)

class Scratch(Attack):

    def __init__(self):
        super().__init__("Scratch",10)

        

charmander = Charmander("Charmander",100)

charmeleon = Charmeleon("Charmeleon",200)

charizard = Charizard("Charizard",300)




bagpack = []
basic_list = []
naim = Player(bagpack)
light = game_engine(charizard,naim)

light.play()

#when I go home need to be able to add attacks,attack_limit, find a way to evolve