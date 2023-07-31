class game_engine(object):

    def __init__(self, player):
        self.player = player

    # This is where the game is played
    def play(self):

        # The user chooses the starter pokemon
        choose_pokemon = input("what pokemon would you like to choose \n1.\tCharmander\n=>")

        # Choosing of the pokemon
        if choose_pokemon == "1":
            self.player.collect_pokemon(charmander)

    # This is where the battle takes place
    def battle_arena(self, pokemon_1, pokemon_2):
        pass


class Player(object):
    """The player class stores the pokemon in the backpack. The player class also is responsible for the
    evolution."""

    def __init__(self, backpack):
        self.backpack = backpack

    def collect_pokemon(self, pokemon):
        print("You have collected a", pokemon.name, "with a", pokemon.hp, "health")
        self.backpack.append(pokemon)
        for i in self.backpack:
            print(f"You have this Pokemon's in your backpack [{i.name,i.hp}]")

    def evolve_pokemon(self, evolved_pokemon):
        if evolved_pokemon.lower() == "charmander":

            for i, pokemon in enumerate(self.backpack):
                if isinstance(pokemon, Charmander):
                    self.backpack.pop(i)
                    evolved_pokemon_now = Charmeleon(pokemon.name, pokemon.hp)
                    self.backpack.insert(i, evolved_pokemon_now)
                    print(f"{pokemon.name} evolved into {evolved_pokemon_now.name}")
                    for creature in self.backpack:
                        print(f"You have this Pokemon's in your backpack [{creature.name, creature.hp}]")
                    break
            else:
                print("Could not find Charmander in your backpack for evolution.")
        elif evolved_pokemon.lower() == "charmeleon":
            pass
        elif evolved_pokemon.lower() == "charmander":
            pass



class Pokemon:
    """This is the base pokemon class and the other pokemon class will inherit from. This will take
    name,hp as arguments, and have attack function."""
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        pass


class Charmander(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {'Ember': self.ember, 'Scratch': self.scratch}
        self.attack_limits = {'Ember': 3, "Scratch": 3}

    def use_attack(self, attack_name):
        attack = self.attacks.get(attack_name)
        if attack and self.attack_limits.get(attack_name) > 0:
            self.attack_limits[attack_name] -= 1
            return attack()
        return "You have either reached the limit for that attack or entered an invalid attack."

    def ember(self):
        damage = 20
        return f"{self.name} used Ember and dealt {damage} damage!"

    def scratch(self):
        damage = 10
        return f"{self.name} used Scratch and dealt {damage} damage!"


class Charmeleon(Charmander):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        pass


class Charizard(Charmeleon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        pass


charmander = Charmander("Charmander", 100)

charmeleon = Charmeleon("Charmeleon", 200)

charizard = Charizard("Charizard", 300)

bagpack = [charmander]
naim = Player(bagpack)
(naim.evolve_pokemon("charmander"))
basic_list = []
#light = game_engine(charizard,naim)
#light.play()


# when I go home need to be able to add attacks,attack_limit, find a way to evolve
