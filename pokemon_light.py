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
            print(f"You have this Pokemon's in your backpack [{i.name, i.hp}]")

    def evolve_pokemon(self, evolved_pokemon):
        if evolved_pokemon == "charmander":
            evolved_class = Charmeleon
        elif evolved_pokemon == "charmeleon":
            evolved_class = Charizard
        elif evolved_pokemon == "chimchar":
            evolved_class = Monferno
        elif evolved_pokemon == "monferno":
            evolved_class = Infernape
        elif evolved_pokemon == "squirtle":
            evolved_class = Wartortle
        elif evolved_pokemon == "wartortle":
            evolved_class = Blastoise
        elif evolved_pokemon == "bulbasaur":
            evolved_class = Ivysaur
        elif evolved_pokemon == "ivysaur":
            evolved_class = Venusaur
        elif evolved_pokemon == "abra":
            evolved_class = Kadabra
        elif evolved_pokemon == "kadabra":
            evolved_class = Alakazam
        else:
            print("Invalid Pokemon name for evolution.")
            return False

        for i, pokemon in enumerate(self.backpack):
            if isinstance(pokemon, evolved_class):
                self.backpack.pop(i)
                evolved_pokemon_instance = evolved_class(pokemon.name, pokemon.hp)
                self.backpack.insert(i, evolved_pokemon_instance)
                print(f"{pokemon.name} evolved into {evolved_pokemon_instance.name}")
                print(evolved_pokemon_instance)
                for creature in self.backpack:
                    print(f"You have this Pokemon in your backpack: {creature.name} with {creature.hp} HP")
                break
        else:
            print(f"Could not find {evolved_pokemon.capitalize()} in your backpack for evolution.")
            return False

        return True


class Pokemon:
    """This is the base Pokemon class that other Pokemon classes will inherit from.
    This will take name and hp as arguments and have an attack function."""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.attacks = {}
        self.attack_limits = {}

    def attack(self):
        pass

    def use_attack(self, attack_name):
        attack = self.attacks.get(attack_name)
        if attack and self.attack_limits.get(attack_name, 0) > 0:
            self.attack_limits[attack_name] -= 1
            return attack()
        return "You have either reached the limit for that attack or entered an invalid attack."


class Charizard(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Charmeleon(Charizard):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Charmander(Charmeleon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Chimchar(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Monferno(Chimchar):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Infernape(Monferno):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Squirtle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Wartortle(Squirtle):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Blastoise(Wartortle):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Bulbasaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Ivysaur(Bulbasaur):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Venusaur(Ivysaur):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}

    # Psychic-type Pokemon


class Abra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Kadabra(Abra):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


class Alakazam(Kadabra):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {}
        self.attack_limits = {}


charmander = Charmander("Charmander", 100)
charmeleon = Charmeleon("Charmeleon", 200)
charizard = Charizard("Charizard", 300)

chimchar = Chimchar("Chimchar", 100)
monferno = Monferno("Monferno", 200)
infernape = Infernape("Infernape", 300)

squirtle = Squirtle("Squirtle", 100)
wartotle = Wartortle("Wartotle", 200)
blastoise = Blastoise("Blastoise", 300)

bulbasaur = Bulbasaur("Bulbasaur", 100)
ivysaur = Ivysaur("Ivysaur", 200)
venusaur = Venusaur("Venesaur", 300)

abra = Abra("Abra", 100)
kadabra = Kadabra("Kadabra", 200)
alakazam = Alakazam("Alakazam", 300)

backpack = [charmander]
naim = Player(backpack)
naim.evolve_pokemon("charmander")
basic_list = []
# light = game_engine(charizard,naim)
# light.play()


# when I go home need to be able to add attacks,attack_limit, find a way to evolve
