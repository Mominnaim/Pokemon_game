class game_engine(object):

    def __init__(self, player):
        self.player = player

    # This is where the game is played
    def play(self):
        # The user chooses the starter pokemon
        choose_pokemon = input("what pokemon would you like to choose "
                               "\n1.\tCharmander\n2.\tBulbasaur\n3.\tSquirtle\n4.\tChimchar\n=>")

        # Choosing of the pokemon
        if choose_pokemon == "1":
            charmander = Charmander("charmander", 100)
            self.player.collect_pokemon(charmander)
        elif choose_pokemon == "2":
            bulbasaur = Bulbasaur("Bulbasaur", 100)
            self.player.collect_pokemon(bulbasaur)
        elif choose_pokemon == "3":
            squirtle = Squirtle("Squirtle", 100)
            self.player.collect_pokemon(squirtle)
        elif choose_pokemon == "4":
            chimchar = Chimchar("Chimchar", 100)
            self.player.collect_pokemon(chimchar)

        for i in self.player.backpack:
            print(f'{i.name} is your starter pokemon, train it well and become stronger together')

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

    def evolve_pokemon(self, evolved_pokemon):
        if evolved_pokemon == "charmander":
            for i, poke in enumerate(self.backpack):
                if poke.name == "charmander":
                    self.backpack.pop(i)
                    charmeleon = Charmeleon("Charmeleon", 200)
                    self.backpack.insert(i, charmeleon)
                else:
                    print("This pokemon is not in your backpack")
        elif evolved_pokemon == "charmeleon":
            for i, poke in enumerate(self.backpack):
                if poke.name == "charmeleon":
                    self.backpack.pop(i)
                    charizard = Charizard("Charizard", 300)
                    self.backpack.insert(i, charizard)
                else:
                    print("This pokemon is not in your backpack")
        elif evolved_pokemon == "chimchar":
            for i, poke in enumerate(self.backpack):
                if poke.name == "chimchar":
                    self.backpack.pop(i)
                    monferno = Monferno("Monferno", 200)
                    self.backpack.insert(i, monferno)
        elif evolved_pokemon == "monferno":
            for i, poke in enumerate(self.backpack):
                if poke.name == "monferno":
                    self.backpack.pop(i)
                    infernape = Infernape("Infernape", 300)
                    self.backpack.insert(i, infernape)
        elif evolved_pokemon == "squirtle":
            for i, poke in enumerate(self.backpack):
                if poke.name == "squirtle":
                    self.backpack.pop(i)
                    wartotle = Wartortle("Wartotle", 200)
                    self.backpack.insert(i, wartotle)
        elif evolved_pokemon == "wartortle":
            for i, poke in enumerate(self.backpack):
                if poke.name == "wartotle":
                    self.backpack.pop(i)
                    blastoise = Blastoise("Blastoise", 300)
                    self.backpack.insert(i, blastoise)
        elif evolved_pokemon == "bulbasaur":
            for i, poke in enumerate(self.backpack):
                if poke.name == "bulbasaur":
                    self.backpack.pop(i)
                    ivysaur = Ivysaur("Ivysaur", 200)
                    self.backpack.insert(i, ivysaur)
        elif evolved_pokemon == "ivysaur":
            for i, poke in enumerate(self.backpack):
                if poke.name == "ivysaur":
                    self.backpack.pop(i)
                    venusaur = Venusaur("Venesaur", 300)
                    self.backpack.insert(i, venusaur)
        elif evolved_pokemon == "abra":
            for i, poke in enumerate(self.backpack):
                if poke.name == "abra":
                    self.backpack.pop(i)
                    kadabra = Kadabra("Kadabra", 200)
                    self.backpack.insert(i, kadabra)
        elif evolved_pokemon == "kadabra":
            for i, poke in enumerate(self.backpack):
                if poke.name == "kadabra":
                    self.backpack.pop(i)
                    alakazam = Alakazam("Alakazam", 300)
                    self.backpack.insert(i, alakazam)
        else:
            print("Invalid Pokemon name for evolution.")
            return False

        for poke in self.backpack:
            print(poke.name)


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
        if attack and self.attack_limits.get(attack_name) > 0:
            self.attack_limits[attack_name] -= 1
            return attack()
        return "You have either reached the limit for that attack or entered an invalid attack."


class Charizard(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.crimson_strike()}
        self.attack_limits = {"crimson strike":2}

    def crimson_strike(self):
        damage = 75
        return f"{self.name} did Crimson strike and did {damage} damage!"


class Charmeleon(Charizard):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.fire_fang()}
        self.attack_limits = {"fire fang": 3}

    def fire_fang(self):
        damage = 45
        return f"{self.name} did fire fang and did {damage} damage!"


class Charmander(Charmeleon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.ember()}
        self.attack_limits = {"ember": 3}

    def ember(self):
        damage = 20
        return f"{self.name} did Ember and did {damage} damage!"


class Chimchar(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.fire_punch()}
        self.attack_limits = {"fire punch": 3}

    def fire_punch(self):
        damage = 20
        return f"{self.name} did Fire punch and did {damage} damage!"


class Monferno(Chimchar):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.fire_flame_dance()}
        self.attack_limits = {"fire flame dance": 3}

    def fire_flame_dance(self):
        damage = 45
        return f"{self.name} did Fire flame dance and did {damage} damage!"


class Infernape(Monferno):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.volcanic_punch()}
        self.attack_limits = {"volcanic punch": 2}

    def volcanic_punch(self):
        damage = 75
        return f"{self.name} did Volcanic punch and did {damage} damage!"


class Squirtle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.water_gun()}
        self.attack_limits = {"water gun": 3}

    def water_gun(self):
        damage = 20
        return f"{self.name} did Water gun and did {damage} damage!"


class Wartortle(Squirtle):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.aqua_splash()}
        self.attack_limits = {"aqua splash": 3}

    def aqua_splash(self):
        damage = 30
        return f"{self.name} did Aqua splash and did {damage} damage!"


class Blastoise(Wartortle):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.hydro_pump()}
        self.attack_limits = {"hydro pump": 2}

    def hydro_pump(self):
        damage = 75
        return f"{self.name} did Hydro pump and did {damage} damage!"


class Bulbasaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.razor_leaf()}
        self.attack_limits = {"razor leaf": 3}

    def razor_leaf(self):
        damage =20
        return f"{self.name} did Razor leaf and did {damage} damage!"


class Ivysaur(Bulbasaur):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.toxic_whip()}
        self.attack_limits = {"toxic whip": 3}

    def toxic_whip(self):
        damage = 45
        return f"{self.name} did Toxic whip and did {damage} damage!"


class Venusaur(Ivysaur):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.jungle_hammer()}
        self.attack_limits = {"jungle hammer": 2}

    def  jungle_hammer(self):
        damage = 75
        return f"{self.name} did Jungle Hammer and did {damage} damage!"


class Abra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.psychic_slap()}
        self.attack_limits = {"psychic slap": 3}

    def psychic_slap(self):
        damage = 20
        return f"{self.name} did Psychic slap and did {damage} damage!"


class Kadabra(Abra):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.psychic_shock()}
        self.attack_limits = {"psychic shock": 3}

    def psychic_shock(self):
        damage = 45
        return f"{self.name} did Psychic shock and did {damage} damage!"


class Alakazam(Kadabra):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacks = {self.power_of_zen()}
        self.attack_limits = {"power of zen": 2}

    def power_of_zen(self):
        damage = 80
        return f"{self.name} used Power of Zen and did {damage} damage!"


abra = Abra("Abra", 100)

dope = Charmeleon("charmeleon", 200)
backpack = [charmander]
naim = Player(backpack)
naim.evolve_pokemon("charmander")
basic_list = []

"""
mt = []
naim = Player(mt)
light = game_engine(naim)
light.play()
"""
