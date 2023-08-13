import time
import random


class game_engine(object):

    # The game needs two things which is the player and the games backpack
    def __init__(self, player):
        self.player = player
        self.game_backpack = ["charmander", "bulbasaur", "squirtle", "chimchar", "abra"]

    # This is where the game is played
    def play(self):

        # Player chooses their starter pokemon
        while len(self.player.backpack) != 1:

            # The user chooses the starter pokemon
            choose_pokemon = input("what pokemon would you like to choose "
                                   "\n1.\tCharmander\n2.\tBulbasaur\n3.\tSquirtle\n4.\tChimchar\npick a number =>")

            # Choosing pokemon, then add it to the backpack
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
                print(f'{i.name},{i.hp}')
            print()

        # This is the actual part where the main game is played and commences the round from 1-8
        rounds = 1
        while rounds != 9:
            print(f'this is round {rounds}\n\n')

            # Odd rounds, you will be able to collect or evolve pokemon
            if rounds in [1, 3, 5, 7]:
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

                    # Player chooses a pokemon to evolve
                    pick_pokemon = int(input("Pick a pokemon from your backpack to evolve \nType in the number =>"))
                    evolving_pokemon = self.player.backpack[pick_pokemon - 1]
                    self.player.evolve_pokemon(evolving_pokemon.name)

            # Even rounds will have you fight a pokemon and it gets progressively harder.
            elif rounds == 2:
                wild_charmander = Charmander("wild charmander", 100)
                wild_abra = Abra("wild abra", 100)
                wild_bulbasaur = Bulbasaur("wild bulbasuar", 100)
                wild_chimchar = Chimchar("wild chimchar", 100)
                wild_squirtle = Squirtle("wild squirtle", 100)

                level_one_pokemon = [wild_abra, wild_bulbasaur, wild_charmander, wild_chimchar, wild_squirtle]
                opponent_pokemon = random.choice(level_one_pokemon)
                self.battle_arena(opponent_pokemon)
            elif rounds == 4:
                wild_charmeleon = Charmeleon("wild charmeleon", 200)
                wild_ivysaur = Ivysaur("wild ivysaur", 200)
                wild_kadabra = Kadabra("wild kadabra", 200)
                wild_wortortle = Wartortle("wild wartortle", 200)
                wild_monferno = Monferno("wild monferno", 200)

                level_two_pokemon = [wild_charmeleon, wild_kadabra, wild_ivysaur, wild_monferno, wild_wortortle]
                opponent_pokemon = random.choice(level_two_pokemon)
                self.battle_arena(opponent_pokemon)
            elif rounds == 6:
                wild_alakazam = Alakazam("a wild Alakazam", 300)
                wild_venusaur = Venusaur("a wild Venusaur", 300)
                wild_charizard = Charizard("a wild Charizard", 300)
                wild_blastoise = Blastoise("a wild Blastoise", 300)
                wild_infernape = Infernape("a wild Infernape", 300)
                level_three_pokemon = [wild_charizard, wild_infernape, wild_alakazam, wild_venusaur, wild_blastoise]
                opponent_pokemon = random.choice(level_three_pokemon)
                self.battle_arena(opponent_pokemon)

                # This is the boss fight.
            elif rounds == 8:
                print("Get ready to fight the boss MEWTWO!!!")
                mewtwo = Mewtwo("Mewtwo", 300)
                self.battle_arena(mewtwo)

            rounds = rounds + 1

    # This is where the battle takes place
    def battle_arena(self, pokemon_2):

        # You get to choose your battling pokemon
        print("Choose one of your pokemon to be your battling pokemon.\n")
        number = 1
        for i in self.player.backpack:
            print(f'{number} -> {i.name},{i.hp}')
            number = number + 1

        battling_pokemon = int(input("\n=> "))
        pokemon_1 = self.player.backpack[battling_pokemon - 1]

        # The actual game
        while len(self.player.backpack) != 0:

            print(f"It is now {pokemon_1.name}\'s turn to attack")

            damage = pokemon_1.use_attack()

            print(f"{pokemon_1.name} attacks {pokemon_2.name} for {damage} health")
            time.sleep(1)
            pokemon_2.hp = pokemon_2.hp - damage

            # If the enemy pokemon dies, you win and your pokemon evolves.
            if pokemon_2.hp <= 0:
                if pokemon_2.name == "Mewtwo":
                    print("You have beat Mewtwo and saved the world!")
                    exit(0)
                print(f"{pokemon_2.name} has lost, and you win the game")
                self.player.evolve_pokemon(pokemon_1.name)
                return True
            else:
                print(f"{pokemon_2.name} has {pokemon_2.hp} health left\n")

            print(f"It is now {pokemon_2.name}\'s turn to attack")
            damage = pokemon_2.random_attack()

            print(f"{pokemon_2.name} attacks {pokemon_1.name} for {damage} health")
            pokemon_1.hp = pokemon_1.hp - damage
            time.sleep(1)

            # If your pokemon dies, then you pick another pokemon to fight, and if your back is empty, then you lose.
            if pokemon_1.hp <= 0:
                print(f"Your {pokemon_1.name} has lost.\n")
                self.player.backpack.remove(pokemon_1)
                if len(self.player.backpack) != 0:
                    number = 1
                    for i in self.player.backpack:
                        print(f'{number} -> {i.name},{i.hp}')
                        number = number + 1
                    battling_pokemon = int(input("\n=> "))
                    pokemon_1 = self.player.backpack[battling_pokemon - 1]
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

    # This is where the collection happens
    def collect_pokemon(self, pokemon):
        print("You have collected a", pokemon.name, "with a", pokemon.hp, "health\n")
        self.backpack.append(pokemon)

    # This is where the evolution happens
    def evolve_pokemon(self, evolved_pokemon):
        if evolved_pokemon == "charmander" or evolved_pokemon == "Charmander":
            for i, poke in enumerate(self.backpack):
                if poke.name == "charmander":
                    self.backpack.pop(i)
                    charmeleon = Charmeleon("charmeleon", 200)
                    self.backpack.insert(i, charmeleon)
                    break
        elif evolved_pokemon == "charmeleon":
            for i, poke in enumerate(self.backpack):
                if poke.name == "charmeleon":
                    self.backpack.pop(i)
                    charizard = Charizard("charizard", 300)
                    self.backpack.insert(i, charizard)
                    break
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
        elif evolved_pokemon in ["charizard","alakazam","infernape","venusaur","blastoise"]:
            print(f"{evolved_pokemon} has reached final evolution\n")
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

    def random_attack(self):
        list_of_attacks = [self.attack_one, self.attack_two]
        random_attack = random.choice(list_of_attacks)
        return random_attack()

    def attack_one(self):
        pass

    def attack_two(self):
        pass

    def get_name(self):
        return self.name

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.attack_one()
        elif pick_attack == "2":
            return self.attack_two()


class Charizard(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Crimson strike": self.attack_one, "Fire breathe": self.attack_two}

    def attack_one(self):
        print("Charizard uses Crimson Strike!")
        damage = 75
        return damage

    def attack_two(self):
        print("Charizard uses Fire Breathe!")
        damage = 60
        return damage


class Charmeleon(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Fire tail": self.attack_one, "Fire scratch": self.attack_two}

    def attack_one(self):
        print("Charmeleon uses Fire Tail!")
        damage = 50
        return damage

    def attack_two(self):
        print("Charmeleon uses Fire Scratch")
        damage = 50
        return damage


class Charmander(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Ember": self.attack_one, "Scratch": self.attack_two}

    def attack_two(self):
        print("Charmander uses Scratch!")
        damage = 30
        return damage

    def attack_one(self):
        print("Charmander uses Ember!")
        damage = 30
        return damage


class Chimchar(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Ember": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self):
        print("Chimchar uses Ember!")
        damage = 30
        return damage

    def attack_two(self):
        print("Chimchar uses Scratch!")
        damage = 30
        return damage


class Monferno(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Fire Punch": self.attack_one, "Fire Slap": self.attack_two}

    def attack_one(self):
        print("Monferno uses Fire punch")
        damage = 50
        return damage

    def attack_two(self):
        print("Monferno uses Fire slap")
        damage = 50
        return damage


class Infernape(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Volcanic Punch": self.attack_one, "Lava Rain": self.attack_two}

    def attack_one(self):
        print("Infernape uses Volcanic punch!")
        damage = 75
        return damage

    def attack_two(self):
        print("Infernape uses Lava rain")
        damage = 50
        return damage


class Squirtle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Water Gun": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self):
        print("Squirtle uses Water gun!")
        damage = 30
        return damage

    def attack_two(self):
        print("Squirtle uses Scratch!")
        damage = 30
        return damage


class Wartortle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Water Pump": self.attack_one, "Waterfall": self.attack_two}

    def attack_one(self):
        print("Wartortle uses Water fall!")
        damage = 50
        return 50

    def attack_two(self):
        print("Wartortle uses Water pump!")
        damage = 50
        return damage


class Blastoise(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Hydro Pump": self.attack_one, "Tsunami": self.attack_two}

    def attack_one(self):
        print("Blastoise uses Hydro pump!")
        damage = 75
        return damage

    def attack_two(self):
        print("Blastoise unleashes a Tsunami!")
        damage = 90
        return damage


class Bulbasaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Vine whip": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self):
        print("Bulbasaur uses vine whip")
        damage = 30
        return damage

    def attack_two(self):
        print("Bulbasaur uses Scratch!")
        damage = 30
        return damage


class Ivysaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Pollen Power": self.attack_one, "Branch Slap": self.attack_two}

    def attack_one(self):
        print("Ivysaur uses Pollen Powder")
        damage = 50
        return damage

    def attack_two(self):
        print("Ivysaur uses branch slap")
        damage = 50
        return damage


class Venusaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Jungle Hammer": self.attack_one, "Forest whip": self.attack_two}

    def attack_one(self):
        print("Venusaur uses Forest whip!")
        damage = 60
        return damage

    def attack_two(self):
        print("Venusaur uses Jungle hammer!")
        damage = 75
        return damage


class Abra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Slap": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self):
        print("Abra uses slap!")
        damage = 30
        return damage

    def attack_two(self):
        print("Abra uses Scratch!")
        damage = 30
        return damage


class Kadabra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Psychic Slap": self.attack_one, "Mind Twist": self.attack_two}

    def attack_one(self):
        print("Kadabra uses Psychic Slap!")
        damage = 50
        return damage

    def attack_two(self):
        print("Kadabra uses Mind twist")
        damage = 50
        return damage


class Alakazam(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Power of Zen": self.attack_one, "Mantra Kick": self.attack_two}

    def attack_one(self):
        print("Alakazam uses the Power of Zen")
        damage = 50
        return damage

    def attack_two(self):
        print("Alakazam uses Mantra Kick")
        damage = 75
        return damage


class Mewtwo(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Pulse Ray": self.attack_one, "Major Beatdown": self.attack_two}

    def attack_one(self):
        print("Mewtwo uses Pulse Ray")
        damage = 75
        return damage

    def attack_two(self):
        print("Mewtwo uses Major beatdown")
        damage = 60
        return damage


def main():
    players_backpack = []
    naim = Player(players_backpack)
    light = game_engine(naim)
    light.play()


if __name__ == "__main__":
    main()
