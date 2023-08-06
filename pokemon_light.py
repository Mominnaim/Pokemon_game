import time
import random


class game_engine(object):

    def __init__(self, player):
        self.player = player
        self.game_backpack = ["charmander", "bulbasaur", "squirtle", "chimchar", "abra"]


    # This is where the game is played
    def play(self):

        while len(self.player.backpack) != 1:

            # The user chooses the starter pokemon
            choose_pokemon = input("what pokemon would you like to choose "
                                   "\n1.\tCharmander\n2.\tBulbasaur\n3.\tSquirtle\n4.\tChimchar\npick a number =>")

            # Choosing of the pokemon
            if choose_pokemon == "1":
                charmander = Charmander("charmander", 100)
                self.player.collect_pokemon(charmander)
                self.game_backpack.remove("charmander")
            elif choose_pokemon == "2":
                bulbasaur = Bulbasaur("bulbasaur", 100)
                self.player.collect_pokemon(bulbasaur)
                self.game_backpack.remove("bulbasaur")
            elif choose_pokemon == "3":
                squirtle = Squirtle("squirtle", 100)
                self.player.collect_pokemon(squirtle)
                self.game_backpack.remove("squirtle")
            elif choose_pokemon == "4":
                chimchar = Chimchar("chimchar", 100)
                self.player.collect_pokemon(chimchar)
                self.game_backpack.remove("chimchar")

            print("This is the the pokemon in your backpack")
            for i in self.player.backpack:
                print(f'{i.name}')
            print()

        rounds = 1

        while rounds != 7:
            print(f'this is round {rounds}\n\n')

            if rounds in [1,3,5,7]:
                prize_pokemon = random.choice(self.game_backpack)
                pick_option = input(f"1. Collect a {prize_pokemon}\n2. Evolve a current pokemon\n=>")
                if pick_option == "1":
                    if prize_pokemon == "charmander":
                        charmander = Charmander("charmander", 100)
                        self.player.collect_pokemon(charmander)
                        self.game_backpack.remove("charmander")
                    elif prize_pokemon == "bulbasaur":
                        bulbasaur = Bulbasaur("bulbasaur", 100)
                        self.player.collect_pokemon(bulbasaur)
                        self.game_backpack.remove("bulbasaur")
                    elif prize_pokemon == "squirtle":
                        squirtle = Squirtle("squirtle", 100)
                        self.player.collect_pokemon(squirtle)
                        self.game_backpack.remove("squirtle")
                    elif prize_pokemon == "chimchar":
                        chimchar = Chimchar("chimchar", 100)
                        self.player.collect_pokemon(chimchar)
                        self.game_backpack.remove("chimchar")
                    elif prize_pokemon == "abra":
                        abra = Abra("abra", 100)
                        self.player.collect_pokemon(abra)
                        self.game_backpack.remove("abra")
                elif pick_option == "2":
                    print("Which pokemon would you like to evolve")
                    print("This are the pokemon(s) in your backpack\n")
                    number = 1
                    for i in self.player.backpack:
                        print(f'{number} -> {i.name}')
                        number = number + 1

                    pick_pokemon = input("Pick a pokemon from your backpack to evolve \nType in the number =>")
                    if pick_pokemon == "1":
                        evolving_pokemon = self.player.backpack[0]
                        self.player.evolve_pokemon(evolving_pokemon.name)
                    elif pick_pokemon == "2":
                        evolving_pokemon = self.player.backpack[1]
                        self.player.evolve_pokemon(evolving_pokemon.name)
                    elif pick_pokemon == "3":
                        evolving_pokemon = self.player.backpack[2]
                        self.player.evolve_pokemon(evolving_pokemon.name)
                    elif pick_pokemon == "4":
                        evolving_pokemon = self.player.backpack[3]
                        self.player.evolve_pokemon(evolving_pokemon.name)
                    elif pick_pokemon == "5":
                        evolving_pokemon = self.player.backpack[4]
                        self.player.evolve_pokemon(evolving_pokemon.name)
                    

            elif rounds == 2:
                wild_charmander = Charmander("wild charmander", 100)
                wild_abra = Abra("wild abra",100)
                wild_bulbasaur = Bulbasaur("wild bulbasuar",100)
                wild_chimchar = Chimchar("wild chimchar",100)
                wild_squirtle = Squirtle("wild squirtle",100)
                
                level_one_pokemon = [wild_abra,wild_bulbasaur,wild_charmander,wild_chimchar,wild_squirtle]
                opponent_pokemon = random.choice(level_one_pokemon)
                self.battle_arena(opponent_pokemon)
            elif rounds == 4:
                wild_charmeleon = Charmeleon("wild charmeleon",200)
                wild_ivysaur = Ivysaur("wild ivysaur",200)
                wild_kadabra = Kadabra("wild kadabra",200)
                wild_wortortle = Wartortle("wild wartortle",200)
                wild_monferno = Monferno("wild monferno",200)

                level_two_pokemon = [wild_charmeleon,wild_kadabra,wild_ivysaur,wild_monferno,wild_wortortle]
                opponent_pokemon = random.choice(level_two_pokemon)
                self.battle_arena(opponent_pokemon)
            elif rounds == 6:
                wild_alakazam = Alakazam("a wild Alakazam", 300)
                wild_venusaur = Venusaur("a wild Venusaur", 300)
                wild_charizard = Charizard("a wild Charizard", 300)
                wild_blastoise = Blastoise("a wild Blastoise", 300)
                wild_infernape = Infernape("a wild Infernape", 300)
                level_three_pokemon = [wild_charizard,wild_infernape,wild_alakazam,wild_venusaur,wild_blastoise]
                opponent_pokemon = random.choice(level_three_pokemon)
                self.battle_arena(opponent_pokemon)
            elif rounds == 8:
                pass
            
            rounds = rounds + 1

    # This is where the battle takes place
    def battle_arena(self, pokemon_2):

        print("Choose one of your pokemon to be your battling pokemon.\n")
        number = 1
        for i in (self.player.backpack):
            print(f'{number} -> {i.name}')
            number = number + 1
        battling_pokemon = input("\n=> ")

        if battling_pokemon == "1":
            pokemon_1 = self.player.backpack[0]
        elif battling_pokemon == "2":
            pokemon_1 = self.player.backpack[1]
        elif battling_pokemon == "3":
            pokemon_1 = self.player.backpack[2]
        elif battling_pokemon == "4":
            pokemon_1 = self.player.backpack[3]
        elif battling_pokemon == "5":
            pokemon_1 = self.player.backpack[4]
        

        while len(self.player.backpack) != 0:

            damage = pokemon_1.attack()

            print(f"It is now {pokemon_1.name}\'s turn to attack")
            print(f"{pokemon_1.name} attacks {pokemon_2.name} for {damage} health")
            time.sleep(1)
            pokemon_2.hp = pokemon_2.hp - damage

            if pokemon_2.hp <= 0:
                print(f"{pokemon_2.name} has lost, and you win the game")
                winning_evolution = pokemon_1.name
                self.player.evolve_pokemon(winning_evolution)
                return True
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
                    number = 1
                    for i in (self.player.backpack):
                        print(f'{number} -> {i.name}')
                        number = number + 1
                    battling_pokemon = input("\n=> ")

                    if battling_pokemon == "1":
                        pokemon_1 = self.player.backpack[0]
                    elif battling_pokemon == "2":
                        pokemon_1 = self.player.backpack[1]
                    elif battling_pokemon == "3":
                        pokemon_1 = self.player.backpack[2]
                    elif battling_pokemon == "4":
                        pokemon_1 = self.player.backpack[3]
                    elif battling_pokemon == "5":
                        pokemon_1 = self.player.backpack[4]
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
                    charmeleon = Charmeleon("charmeleon", 200)
                    self.backpack.insert(i, charmeleon)
                else:
                    print("This pokemon is not in your backpack")
        elif evolved_pokemon == "charmeleon":
            for i, poke in enumerate(self.backpack):
                if poke.name == "charmeleon":
                    self.backpack.pop(i)
                    charizard = Charizard("charizard", 300)
                    self.backpack.insert(i, charizard)
                else:
                    print("This pokemon is not in your backpack")
        elif evolved_pokemon == "chimchar":
            for i, poke in enumerate(self.backpack):
                if poke.name == "chimchar":
                    self.backpack.pop(i)
                    monferno = Monferno("monferno", 200)
                    self.backpack.insert(i, monferno)
        elif evolved_pokemon == "monferno":
            for i, poke in enumerate(self.backpack):
                if poke.name == "monferno":
                    self.backpack.pop(i)
                    infernape = Infernape("infernape", 300)
                    self.backpack.insert(i, infernape)
        elif evolved_pokemon == "squirtle":
            for i, poke in enumerate(self.backpack):
                if poke.name == "squirtle":
                    self.backpack.pop(i)
                    wartotle = Wartortle("wartortle", 200)
                    self.backpack.insert(i, wartotle)
        elif evolved_pokemon == "wartortle":
            for i, poke in enumerate(self.backpack):
                if poke.name == "wartortle":
                    self.backpack.pop(i)
                    blastoise = Blastoise("blastoise", 300)
                    self.backpack.insert(i, blastoise)
        elif evolved_pokemon == "bulbasaur":
            for i, poke in enumerate(self.backpack):
                if poke.name == "bulbasaur":
                    self.backpack.pop(i)
                    ivysaur = Ivysaur("ivysaur", 200)
                    self.backpack.insert(i, ivysaur)
        elif evolved_pokemon == "ivysaur":
            for i, poke in enumerate(self.backpack):
                if poke.name == "ivysaur":
                    self.backpack.pop(i)
                    venusaur = Venusaur("venusaur", 300)
                    self.backpack.insert(i, venusaur)
        elif evolved_pokemon == "abra":
            for i, poke in enumerate(self.backpack):
                if poke.name == "abra":
                    self.backpack.pop(i)
                    kadabra = Kadabra("kadabra", 200)
                    self.backpack.insert(i, kadabra)
        elif evolved_pokemon == "kadabra":
            for i, poke in enumerate(self.backpack):
                if poke.name == "kadabra":
                    self.backpack.pop(i)
                    alakazam = Alakazam("alakazam", 300)
                    self.backpack.insert(i, alakazam)
        else:
            print("Invalid Pokemon name for evolution.")
            return False

        for i, poke in enumerate(self.backpack):
            print(poke.name, "\n")


class Pokemon:
    """This is the base Pokemon class that other Pokemon classes will inherit from.
    This will take name and hp as arguments and have an attack function."""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        pass

    def get_name(self):
        return self.name


class Charizard(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 100
        return damage


class Charmeleon(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage


class Charmander(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage


class Chimchar(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage


class Monferno(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage


class Infernape(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage


class Squirtle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage


class Wartortle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage


class Blastoise(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage


class Bulbasaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage


class Ivysaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage


class Venusaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage


class Abra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 30
        return damage


class Kadabra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 50
        return damage


class Alakazam(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        damage = 70
        return damage


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