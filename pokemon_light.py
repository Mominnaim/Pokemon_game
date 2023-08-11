import time
import random


class game_engine(object):


    # We need two things in this game, and that is the pokemon in the game and the player.

    def __init__(self, player):
        self.player = player
        self.game_backpack = ["charmander", "bulbasaur", "squirtle", "chimchar", "abra"]

        

    # This is where the game is played

    def play(self):

        # This is where you will choose your starter pokemon.

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


        # This is where the round will commence starting from 1 to 9.
        rounds = 1
        while rounds != 9:
            print(f'this is round {rounds}\n\n')

            # If the rounds equal an odd number then the user can either collect or evovle their current pokemon.
            # In this case you are collecting a pokemon

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

                    # In this case you are evolving a pokemon.

                    pick_pokemon = int(input("Pick a pokemon from your backpack to evolve \nType in the number =>"))
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

            # Rounds 2,4,6, and 8 will be fighting rounds where it gets progressively harder.
            elif rounds == 2:
                wild_charmander = Charmander("wild charmander", 100)
                wild_abra = Abra("wild abra", 100)
                wild_bulbasaur = Bulbasaur("wild bulbasuar", 100)
                wild_chimchar = Chimchar("wild chimchar", 100)
                wild_squirtle = Squirtle("wild squirtle", 100)

                level_one_pokemon = [wild_abra, wild_bulbasaur, wild_charmander, wild_chimchar, wild_squirtle]
                opponent_pokemon = random.choice(level_one_pokemon)
                self.battle_arena(wild_charmander)
            elif rounds == 4:
                wild_charmeleon = Charmeleon("wild charmeleon", 200)
                wild_ivysaur = Ivysaur("wild ivysaur", 200)
                wild_kadabra = Kadabra("wild kadabra", 200)
                wild_wortortle = Wartortle("wild wartortle", 200)
                wild_monferno = Monferno("wild monferno", 200)

                level_two_pokemon = [wild_charmeleon, wild_kadabra, wild_ivysaur, wild_monferno, wild_wortortle]
                opponent_pokemon = random.choice(level_two_pokemon)
                self.battle_arena(wild_charmeleon)
            elif rounds == 6:
                wild_alakazam = Alakazam("a wild Alakazam", 300)
                wild_venusaur = Venusaur("a wild Venusaur", 300)
                wild_charizard = Charizard("a wild Charizard", 300)
                wild_blastoise = Blastoise("a wild Blastoise", 300)
                wild_infernape = Infernape("a wild Infernape", 300)
                level_three_pokemon = [wild_charizard, wild_infernape, wild_alakazam, wild_venusaur, wild_blastoise]
                opponent_pokemon = random.choice(level_three_pokemon)
                self.battle_arena(wild_charizard)
            elif rounds == 8:
                print("Get ready to fight the boss MEWTWO!!!")
                self.battle_arena(mewtwo)

            rounds = rounds + 1

    # This is where the battle takes place
    def battle_arena(self, pokemon_2):

        # You choose your battling pokemon


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

        # If the backpack aint empty then the while loops keeps running, and the fighting is still on.
        while len(self.player.backpack) != 0:

            print(f"It is now {pokemon_1.name}\'s turn to attack")

            damage, special_effect = pokemon_1.use_attack()
            

            print(f"{pokemon_1.name} attacks {pokemon_2.name} for {damage} health")
            time.sleep(1)
            pokemon_2.hp = pokemon_2.hp - damage

            if special_effect:
                print(f"{pokemon_2.name} is burned!")
                special_effect.apply_effect(pokemon_2)

            # If the enemy pokemon dies, then whichever of your pokemon deals the winning blow gets to evovle.
            if pokemon_2.hp <= 0:
                print(f"{pokemon_2.name} has lost, and you win the game")
                self.player.evolve_pokemon(pokemon_1.name)
                return True
            else:
                print(f"{pokemon_2.name} has {pokemon_2.hp} health left\n")

            print(f"It is now {pokemon_2.name}\'s turn to attack")
            damage,special_effect = pokemon_2.attack()

            if special_effect:
                print(f"{pokemon_1.name} is burned!")
                special_effect.apply_effect(pokemon_2)


            print(f"{pokemon_2.name} attacks {pokemon_1.name} for {damage} health")
            pokemon_1.hp = pokemon_1.hp - damage
            time.sleep(1)

            # If your pokemon dies, then they get removed from the list, and you have to throw in another pokemon to fight, if your backpack is empty then you lose the game.
            if pokemon_1.hp <= 0:
                print(f"Your {pokemon_1.name} has lost.\n")
                self.player.backpack.remove(pokemon_1)
                if len(self.player.backpack) != 0:
                    number = 1
                    for i in self.player.backpack:
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

    # You simply just collect a pokmemon and put in your backpack.
    def collect_pokemon(self, pokemon):
        print("You have collected a", pokemon.name, "with a", pokemon.hp, "health\n")
        self.backpack.append(pokemon)

    # This is where the evolution happens.
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

    def attack_(self):
        pass

    def get_name(self):
        return self.name


class Charizard(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Crimson strike": self.crimson_strike, "Fire breathe": self.fire_breathe}

    def attack(self):
        list_of_attacks = [self.crimson_strike, self.fire_breathe]
        random_attack = random.choice(list_of_attacks)
        damage, special_effect = random_attack()
        return damage, special_effect

    def crimson_strike(self):
        print("Charizard uses Crimson Strike!")
        damage = 75
        return damage, None     

    def fire_breathe(self):
        print("Charizard uses Fire Breathe!")
        special_effect = StatusEffect(name="burned", duration=3, damage_per_turn=30)
        damage = 60
        return damage, special_effect

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.crimson_strike()
        elif pick_attack == "2":
            return self.fire_breathe()


class Charmeleon(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Fire tail": self.fire_tail, "Fire scratch": self.fire_scratch}

    def attack(self):
        list_of_attacks = [self.fire_tail, self.fire_scratch]
        random_attack = random.choice(list_of_attacks)
        return damage, None


    def fire_tail(self):
        print("Charmeleon uses Fire Tail!")
        damage = 50
        return damage, None

    def fire_scratch(self):
        print("Charmeleon uses Fire Scratch")
        damage = 50
        return damage, None

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.fire_tail()
        elif pick_attack == "2":
            return self.fire_scratch()


class Charmander(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Ember": self.ember}

    def attack(self):
        print("Charmander uses Ember!")
        damage = 30
        return damage, None

    def ember(self):
        print("Charmander uses Ember!")
        damage = 30
        return damage, None

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.ember()


class Chimchar(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Ember": self.ember}

    def attack(self):
        print("Chimchar uses Ember!")
        damage = 30
        return damage

    def ember(self):
        print("Charmander uses Ember!")
        damage = 30
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            pass
        if pick_attack == "2":
            pass


class Monferno(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Fire Punch": self.fire_punch, "Fire Slap": self.fire_slap}

    def attack(self):
        list_of_attacks = [self.fire_slap, self.fire_punch]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def fire_punch(self):
        print("Monferno uses Fire punch")
        damage = 50
        return damage

    def fire_slap(self):
        print("Monferno uses Fire slap")
        damage = 50
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.fire_punch()
        if pick_attack == "2":
            return self.fire_slap()


class Infernape(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Volcanic Punch": self.volcanic_punch, "Lava Rain": self.lava_rain}

    def attack(self):
        list_of_attacks = [self.volcanic_punch, self.lava_rain]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def volcanic_punch(self):
        print("Infernape uses Volcanic punch!")
        damage = 75
        return damage

    def lava_rain(self):
        print("Infernape uses Lava rain")
        damage = 50
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.volcanic_punch()
        if pick_attack == "2":
            return self.lava_rain()


class Squirtle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Water Gun": self.water_gun}

    def attack(self):
        print("Squirtle uses Water gun!")
        damage = 30
        return damage

    def water_gun(self):
        print("Squirtle uses Water gun!")
        damage = 30
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.water_gun()


class Wartortle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Water Pump": self.waterfall, "Waterfall": self.water_pump}

    def attack(self):
        list_of_attacks = [self.water_pump, self.waterfall]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def waterfall(self):
        print("Wartortle uses Water fall!")
        damage = 50
        return 50

    def water_pump(self):
        print("Wartortle uses Water pump!")
        damage = 50
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.waterfall()
        if pick_attack == "2":
            return self.water_pump()


class Blastoise(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Hydro Pump": self.hydro_pump, "Tsunami": self.tsunami}

    def attack(self):
        list_of_attacks = [self.hydro_pump, self.tsunami]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def hydro_pump(self):
        print("Blastoise uses Hydro pump!")
        damage = 75
        return damage

    def tsunami(self):
        print("Blastoise unleashes a Tsunami!")
        damage = 90
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.hydro_pump()
        if pick_attack == "2":
            return self.tsunami()


class Bulbasaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Vine whip": self.vine_whip}

    def attack(self):
        print("Bulbasaur uses vine whip")
        damage = 30
        return damage

    def vine_whip(self):
        print("Bulbasaur uses vine whip")
        damage = 30
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.vine_whip()


class Ivysaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Pollen Power": self.pollen_power, "Branch Slap": self.branch_slap}

    def attack(self):
        list_of_attacks = [self.branch_slap, self.pollen_power]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def pollen_power(self):
        print("Ivysaur uses Pollen Powder")
        damage = 30
        return damage

    def branch_slap(self):
        print("Ivysaur uses branch slap")
        damage = 30
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.pollen_power()
        if pick_attack == "2":
            return self.branch_slap()


class Venusaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Jungle Hammer": self.jungle_hammer, "Forest whip": self.forest_whip}

    def attack(self):
        list_of_attacks = [self.jungle_hammer, self.forest_whip]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def forest_whip(self):
        print("Venusaur uses Forest whip!")
        damage = 60
        return damage

    def jungle_hammer(self):
        print("Venusaur uses Jungle hammer!")
        damage = 75
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.jungle_hammer()
        if pick_attack == "2":
            return self.forest_whip()


class Abra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Slap": self.slap}

    def attack(self):
        print("Abra uses slap!")
        damage = 30
        return damage

    def slap(self):
        print("Abra uses slap!")
        damage = 30
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            self.slap()


class Kadabra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Psychic Slap": self.psychic_slap, "Mind Twist": self.mind_twist}

    def attack(self):
        list_of_attacks = [self.psychic_slap, self.mind_twist]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def psychic_slap(self):
        print("Kadabra uses Psychic Slap!")
        damage = 50
        return damage

    def mind_twist(self):
        print("Kadabra uses Mind twist")
        damage = 50
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.psychic_slap()
        if pick_attack == "2":
            return self.mind_twist()


class Alakazam(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Power of Zen": self.power_of_zen, "Mantra Kick": self.mantra_kick}

    def attack(self):
        list_of_attacks = [self.power_of_zen, self.mantra_kick]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def power_of_zen(self):
        print("Alakazam uses the Power of Zen")
        damage = 50
        return damage

    def mantra_kick(self):
        print("Alakazam uses Mantra Kick")
        damage = 75
        return damage

    def use_attack(self):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.power_of_zen()
        if pick_attack == "2":
            return self.mantra_kick()


class Mewtwo(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self):
        list_of_attacks = [self.pulse_ray, self.major_beatdown, self.tail_shock]
        random_attack = random.choice(list_of_attacks)
        damage = random_attack()
        return damage

    def pulse_ray(self):
        print("Mewtwo uses Pulse Ray")
        damage = 75
        return damage

    def major_beatdown(self):
        print("Mewtwo uses Major beatdown")
        damage = 60
        return damage

    def tail_shock(self):
        print("Mewtwo uses Tail shock")
        damage = 85
        return damage

    def get_name(self):
        return self.name

        
class StatusEffect:
    def __init__(self, name, duration, damage_per_turn=0):
        self.name = name
        self.duration = duration
        self.damage_per_turn = damage_per_turn

    def apply_effect(self, target):
        if self.damage_per_turn > 0:
            for _ in range(self.duration):
                print(f"{target.name} takes {self.damage_per_turn} damage from {self.name}!")
                target.hp -= self.damage_per_turn
        else:
            print(f"{target.name} is {self.name}!")

    def __str__(self):
        return self.name


mewtwo = Mewtwo("Mewtwo", 300)

def main():
    players_backpack = []
    naim = Player(players_backpack)
    light = game_engine(naim)
    light.play()


if __name__ == "__main__":
    main()
