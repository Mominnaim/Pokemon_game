import time


class game_engine(object):

    def __init__(self, player):
        self.player = player

    # This is where the game is played
    def play(self):

        while len(self.player.backpack) != 3:

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

            print("This are the pokemons in your backpack")
            for i in self.player.backpack:
                print(f'{i.name}')
            print()

        self.battle_arena(mewtwo)

    # This is where the battle takes place
    def battle_arena(self, pokemon_2):

        pokemon_1 = self.player.backpack[0]

        while len(self.player.backpack) != 0:

            damage = pokemon_1.attack()

            print(f"It is now {pokemon_1.name}\'s turn to attack")
            print(f"{pokemon_1.name} attacks {pokemon_2.name} for {damage} health")
            time.sleep(1)
            mewtwo.hp = mewtwo.hp - damage

            if pokemon_2.hp <= 0:
                exit("Mewtwo has lost, and you win the game")
            else:
                print(f"{pokemon_2.name} has {pokemon_2.hp} health left\n")

            print(f"It is now {pokemon_2.name}\'s turn to attack")
            damage = pokemon_2.attack()

            print(f"{pokemon_2.name} attacks {pokemon_1.name} for {damage} health")
            pokemon_1.hp = pokemon_1.hp - damage
            time.sleep(1)

            if pokemon_1.hp <= 0:
                print(f"Your {pokemon_1.name} has lost.\n")
                self.player.backpack.remove(pokemon_1)
                if len(self.player.backpack) != 0:
                    pokemon_1 = self.player.backpack[0]
                    print(f"You threw in {pokemon_1.name} to fight")
                    print(f"{pokemon_1.name} has {pokemon_1.hp} health\n")
                    time.sleep(1)
                elif len(self.player.backpack) == 0:
                    exit(f"You have lost against {pokemon_2.name}")
            else:
                print(f"{pokemon_1.name} has {pokemon_1.hp} health left\n")


class Player(object):
    """The player class stores the pokemon in the backpack. The player class also is responsible for the
    evolution."""

    def __init__(self, backpack):
        self.backpack = backpack

    def collect_pokemon(self, pokemon):
        print("You have collected a", pokemon.name, "with a", pokemon.hp, "health\n")
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

    def attack(self):
        pass


class Charizard(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 100
        return damage

    def get_name(self):
        return self.name


class Charmeleon(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage

    def get_name(self):
        return self.name


class Charmander(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage

    def get_name(self):
        return self.name


class Chimchar(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage

    def get_name(self):
        return self.name


class Monferno(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage

    def get_name(self):
        return self.name


class Infernape(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage

    def get_name(self):
        return self.name


class Squirtle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage

    def get_name(self):
        return self.name


class Wartortle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage

    def get_name(self):
        return self.name


class Blastoise(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage

    def get_name(self):
        return self.name


class Bulbasaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage

    def get_name(self):
        return self.name


class Ivysaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage

    def get_name(self):
        return self.name


class Venusaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage

    def get_name(self):
        return self.name


class Abra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage

    def get_name(self):
        return self.name


class Kadabra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage

    def get_name(self):
        return self.name


class Alakazam(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage

    def get_name(self):
        return self.name


class Mewtwo(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage

    def get_name(self):
        return self.name


mewtwo = Mewtwo("Mewtwo", 300)


def main():
    players_backpack = []
    naim = Player(players_backpack)
    light = game_engine(naim)
    light.play()


if __name__ == "__main__":
    main()

# 1. Below
# create a get_name function, every class should have an attack function -> check
# Every class should inherit from the pokemon class -> check
# Create mewtwo and have it inherit from the pokemon class. - > check

# 2. Finish the battle function -> check
# 3. Create 3 rounds to collect different pokemon -> check
# 4. create a main function -> check
