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
    def battle_arena(self, opponent_pokemon):

        # The beginnning part of the phase, where the user chooses their pokemon
        print("Choose one of your pokemon to be your battling pokemon.\n")
        pokemon_1 = self.player.choose_pokemon()
        game_rounds = 1

        # The while loop for the game, and where the fight happens.
        while len(self.player.backpack) != 0:
            print(f"It is now {pokemon_1.name}\'s turn to attack")

            self.my_pokemon_attack(opponent_pokemon, pokemon_1)
            opponent_pokemon.apply_special_effects()  # Apply special effects to the opponent
            if self.alive(opponent_pokemon):
                self.player.evolve_pokemon(pokemon_1.name)
                return True

            self.wild_pokemon_attack(pokemon_1, opponent_pokemon)
            pokemon_1.apply_special_effects()
            if pokemon_1.hp <= 0:
                pokemon_1 = self.alive(pokemon_1)



    # Function to check if the pokemon is alive. Checks to see what the output should be depending on what pokemon.
    def alive(self, pokemon):
        print(f'{pokemon.name} has {pokemon.hp} left\n')
        if pokemon.hp <= 0:
            if isinstance(pokemon, Mewtwo):
                print(f'You beat the boss {pokemon.name}!!')
                exit()
            elif pokemon in self.player.backpack:
                print(f"{pokemon.name} has died.")
                self.player.backpack.remove(pokemon)
                if len(self.player.backpack) == 0:
                    exit("All your pokemons have died,Game Over!!")
                pokemon_1 = self.player.choose_pokemon()

                return pokemon_1
            else:
                print(f'You have beat a {pokemon.name}')
                return True

    # The user pokemon attacks
    def my_pokemon_attack(self, opponent_pokemon, pokemon_1):
        damage = pokemon_1.use_attack(opponent_pokemon)

        # Check if the attack has a special effect
        if "special_effect" in pokemon_1.attacking:
            special_effect = pokemon_1.attacking["special_effect"]
            # Create an instance of the SpecialEffect class and attach it to the opponent
            opponent_pokemon.add_special_effect(
                SpecialEffect(special_effect["name"], special_effect["duration"], special_effect["damage_per_turn"])
            )

        print(f"{pokemon_1.name} attacks {opponent_pokemon.name} for {damage} health")
        time.sleep(1)
        opponent_pokemon.hp = max(opponent_pokemon.hp - damage, 0)
        return opponent_pokemon.hp

    # The wild pokemon attacks
    def wild_pokemon_attack(self, my_pokemon, opponent_pokemon):
        damage = opponent_pokemon.random_attack(my_pokemon)

        # Check if the attack has a special effect
        if "special_effect" in opponent_pokemon.attacking:
            special_effect = opponent_pokemon.attacking["special_effect"]
            my_pokemon.add_special_effect(
                SpecialEffect(special_effect["name"], special_effect["duration"], special_effect["damage_per_turn"])
            )

        print(f"{opponent_pokemon.name} attacks {my_pokemon.name} for {damage} health")
        time.sleep(1)
        my_pokemon.hp = max(my_pokemon.hp - damage, 0)
        return my_pokemon.hp


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
        elif evolved_pokemon in ["charizard", "alakazam", "infernape", "venusaur", "blastoise"]:
            print(f"{evolved_pokemon} has reached final evolution\n")
        else:
            print("Invalid Pokemon name for evolution.")
            return False

        for i, poke in enumerate(self.backpack):
            print(poke.name, "\n")

    def choose_pokemon(self):
        for i, poke in enumerate(self.backpack):
            print(f"{i + 1}-->{poke.name}, with {poke.hp} health ")

        battling_pokemon = int(input("\n=> "))
        pokemon_1 = self.backpack[battling_pokemon - 1]

        return pokemon_1


class Pokemon:
    """This is the base Pokemon class that other Pokemon classes will inherit from.
    This will take name and hp as arguments and have an attack function."""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.special_effects = []

    def random_attack(self,opponent_pokemon):
        list_of_attacks = [self.attack_one, self.attack_two]
        random_attack = random.choice(list_of_attacks)
        return random_attack(opponent_pokemon)

    def attack_one(self,opponent_pokemon):
        pass

    def attack_two(self,opponent_pokemon):
        pass

    def get_name(self):
        return self.name

    def use_attack(self,opponent_pokemon):
        i = 1
        for key, value in self.attacking.items():
            print(f'{i} --> {key}')
            i = i + 1

        pick_attack = input(f'Which attack would you like to use \nPick a number =>')

        if pick_attack == "1":
            return self.attack_one(opponent_pokemon)
        elif pick_attack == "2":
            return self.attack_two(opponent_pokemon)

    def add_special_effect(self, special_effect):
        self.special_effects.append(special_effect)

    def apply_special_effects(self):
        for effect in self.special_effects:
            effect.apply_effect(self)
            effect.duration -= 1
            if effect.duration <= 0:
                self.special_effects.remove(effect)

# A class for special effects that deal damage
class DamageSpecialEffect:
    def __init__(self, name, duration, damage_per_turn):
        self.name = name
        self.duration = duration
        self.damage_per_turn = damage_per_turn

    def apply_effect(self, target):
        print(f"{target.name} is affected by {self.name} and does {self.damage_per_turn}!")
        target.hp -= self.damage_per_turn

# A class for special effects that heal
class HealingSpecialEffect:
    def __init__(self, name, duration, healing_per_turn):
        self.name = name
        self.duration = duration
        self.healing_per_turn = healing_per_turn

    def apply_effect(self, target):
        print(f"{target.name} is affected by {self.name} and is healing!")
        target.hp += self.healing_per_turn



class Charizard(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Crimson strike": self.attack_one, "Fire breathe": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Charizard uses Crimson Strike!")
        damage = 75
        return damage

    def attack_two(self, opponent_pokemon):
        print("Charizard uses Fire Breathe!")
        damage = 60
        burn_effect = DamageSpecialEffect("Burn", duration=3, damage_per_turn=30)
        opponent_pokemon.add_special_effect(burn_effect)  # Attach the effect to the opponent
        return damage


class Charmeleon(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Fire tail": self.attack_one, "Fire scratch": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Charmeleon uses Fire Tail!")
        damage = 50
        return damage

    def attack_two(self, opponent_pokemon):
        print("Charmeleon uses Fire Scratch")
        damage = 50
        return damage


class Charmander(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Ember": self.attack_one, "Scratch": self.attack_two}

    def attack_two(self,opponent_pokemon):
        print("Charmander uses Scratch!")
        damage = 30
        return damage

    def attack_one(self, opponent_pokemon):
        print("Charmander uses Ember!")
        damage = 30
        return damage


class Chimchar(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Ember": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Chimchar uses Ember!")
        damage = 30
        return damage

    def attack_two(self, opponent_pokemon):
        print("Chimchar uses Scratch!")
        damage = 30
        return damage


class Monferno(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Fire Punch": self.attack_one, "Fire Slap": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Monferno uses Fire punch")
        damage = 50
        return damage

    def attack_two(self, opponent_pokemon):
        print("Monferno uses Fire slap")
        damage = 50
        return damage


class Infernape(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Volcanic Punch": self.attack_one, "Lava Rain": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Infernape uses Volcanic punch!")
        damage = 75
        return damage

    def attack_two(self, opponent_pokemon):
        print("Infernape uses Lava rain")
        damage = 50
        return damage


class Squirtle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Water Gun": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Squirtle uses Water gun!")
        damage = 30
        return damage

    def attack_two(self, opponent_pokemon):
        print("Squirtle uses Scratch!")
        damage = 30
        return damage


class Wartortle(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Water Pump": self.attack_one, "Waterfall": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Wartortle uses Water fall!")
        damage = 50
        return 50

    def attack_two(self, opponent_pokemon):
        print("Wartortle uses Water pump!")
        damage = 50
        return damage


class Blastoise(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Hydro Pump": self.attack_one, "Tsunami": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Blastoise uses Hydro pump!")
        damage = 75
        return damage

    def attack_two(self, opponent_pokemon):
        print("Blastoise unleashes a Tsunami!")
        damage = 90
        return damage


class Bulbasaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Vine whip": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Bulbasaur uses vine whip")
        damage = 30
        return damage

    def attack_two(self, opponent_pokemon):
        print("Bulbasaur uses Scratch!")
        damage = 30
        return damage


class Ivysaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Pollen Power": self.attack_one, "Branch Slap": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Ivysaur uses Pollen Powder")
        damage = 50
        return damage

    def attack_two(self, opponent_pokemon):
        print("Ivysaur uses branch slap")
        damage = 50
        return damage


class Venusaur(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Jungle Hammer": self.attack_one, "Forest whip": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Venusaur uses Forest whip!")
        damage = 60
        return damage

    def attack_two(self, opponent_pokemon):
        print("Venusaur uses Jungle hammer!")
        damage = 75
        return damage


class Abra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Slap": self.attack_one, "Scratch": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Abra uses slap!")
        damage = 30
        return damage

    def attack_two(self, opponent_pokemon):
        print("Abra uses Scratch!")
        damage = 30
        return damage


class Kadabra(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Psychic Slap": self.attack_one, "Mind Twist": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Kadabra uses Psychic Slap!")
        damage = 50
        return damage

    def attack_two(self, opponent_pokemon):
        print("Kadabra uses Mind twist")
        damage = 50
        return damage


class Alakazam(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Power of Zen": self.attack_one, "Mantra Kick": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Alakazam uses the Power of Zen")
        damage = 50
        return damage

    def attack_two(self, opponent_pokemon):
        print("Alakazam uses Mantra Kick")
        damage = 75
        return damage


class Mewtwo(Pokemon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.attacking = {"Pulse Ray": self.attack_one, "Major Beatdown": self.attack_two}

    def attack_one(self,opponent_pokemon):
        print("Mewtwo uses Pulse Ray")
        damage = 75
        return damage

    def attack_two(self, opponent_pokemon):
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

# work on special effects on another branch -- 3
# Book chapter exercise -> 48, 49 --> 4


