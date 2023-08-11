from unittest import mock

from .pokemon_light import Pokemon, Charmander, Charmeleon, Charizard, Player,Chimchar,Monferno,Infernape,Squirtle,Wartortle,Blastoise,Bulbasaur,Ivysaur,Venusaur
from .pokemon_light import Abra,Kadabra,Alakazam,Mewtwo


# test one
def test_attack_charmander():
    pokemon_1 = Charmander("Charmander", 100)
    damage = pokemon_1.random_attack()
    assert damage == 30


# Test two
def test_attack_one_charmeleon():
    pokemon_1 = Charmeleon("Charmeleon", 200)
    damage = pokemon_1.attack_one()
    assert damage == 50


# Test three
def test_attack_two_charmeleon():
    pokemon_1 = Charmeleon("Charmeleon", 200)
    damage = pokemon_1.attack_two()
    assert damage == 50


# Test four
def test_attack_one_charizard():
    pokemon_1 = Charizard("Charizard", 300)
    damage = pokemon_1.attack_one()
    assert damage == 75


# Test five
def test_attack_two_charizard():
    pokemon_1 = Charizard("Charizard", 300)
    damage = pokemon_1.attack_two()
    assert damage == 60


# Test six
def test_evolution_charmander():
    pokemon_1 = Charmander("charmander", 100)
    backpack = [pokemon_1]
    ash = Player(backpack)
    ash.evolve_pokemon("charmander")
    for poke in backpack:
        assert poke.name == "charmeleon"


# Test seven
def test_evolution_charmeleon():
    pokemon_1 = Charmeleon("charmeleon", 200)
    backpack = [pokemon_1]
    ash = Player(backpack)
    ash.evolve_pokemon("charmeleon")
    assert isinstance(ash.backpack[0], Charizard)



# Test eight
def test_collecting_pokemon():
    backpack = []
    ash = Player(backpack)
    my_friend = Charizard("yer", 400)
    ash.collect_pokemon(my_friend)
    assert len(backpack) == 1

# Test nine
def test_use_attack_charmander():
    charmander = Charmander('Charmander', 100)

    with mock.patch('builtins.input', return_value ="1"):
        assert charmander.use_attack() == 30
    with mock.patch('builtins.input', return_value="2"):
        assert charmander.use_attack() == 30

# Test ten
def test_use_attack_charmeleon():
    charmeleon = Charmeleon("Charmeleon", 200)

    with mock.patch('builtins.input', return_value ="1"):
        assert charmeleon.use_attack() == 50
    with mock.patch('builtins.input', return_value="2"):
        assert charmeleon.use_attack() == 50

# Test eleven
def test_use_attack_charizard():
    charizard = Charizard('Charizard', 300)

    with mock.patch('builtins.input', return_value ="1"):
        assert charizard.use_attack() == 75
    with mock.patch('builtins.input', return_value="2"):
        assert charizard.use_attack() == 60

# Test twelve
def test_use_attack_chimchar():
    chimchar = Chimchar("Chimchar", 100)

    with mock.patch('builtins.input', return_value ="1"):
        assert chimchar.use_attack() == 30
    with mock.patch('builtins.input', return_value="2"):
        assert chimchar.use_attack() == 30

# Test thirteen
def test_use_attack_monferno():
    monferno = Monferno("Monferno",200)

    with mock.patch('builtins.input', return_value ="1"):
        assert monferno.use_attack() == 50
    with mock.patch('builtins.input', return_value="2"):
        assert monferno.use_attack() == 50

# Test fourteen
def test_use_attack_infernape():
    infernape = Infernape("Infernape", 300)

    with mock.patch('builtins.input', return_value ="1"):
        assert infernape.use_attack() == 75
    with mock.patch('builtins.input', return_value="2"):
        assert infernape.use_attack() == 50

# Test Fifteen
def test_use_attack_squirtle():
    squirtle = Squirtle("Squirtle", 100)

    with mock.patch('builtins.input', return_value ="1"):
        assert squirtle.use_attack() == 30
    with mock.patch('builtins.input', return_value="2"):
        assert squirtle.use_attack() == 30

# Test Sixteen
def test_use_attack_wartortle():
    wartortle = Wartortle("Wartortle", 200)

    with mock.patch('builtins.input', return_value ="1"):
        assert wartortle.use_attack() == 50
    with mock.patch('builtins.input', return_value="2"):
        assert wartortle.use_attack() == 50

# Test Seventeen
def test_use_attack_blastoise():
    blastoise = Blastoise("Blastoise", 300)

    with mock.patch('builtins.input', return_value ="1"):
        assert blastoise.use_attack() == 75
    with mock.patch('builtins.input', return_value="2"):
        assert blastoise.use_attack() == 90

# Test Eighteen
def test_use_attack_bulbasaur():
    bulbasaur = Bulbasaur("Bulb",100)

    with mock.patch('builtins.input', return_value ="1"):
        assert bulbasaur.use_attack() == 30
    with mock.patch('builtins.input', return_value="2"):
        assert bulbasaur.use_attack() == 30

# Test Nineteen
def test_use_attack_ivysaur():
    ivysaur = Ivysaur("ivy",200)

    with mock.patch('builtins.input', return_value ="1"):
        assert ivysaur.use_attack() == 50
    with mock.patch('builtins.input', return_value="2"):
        assert ivysaur.use_attack() == 50

# Test twenty
def test_use_attack_venusaur():
    venusaur = Venusaur("Ven",200)

    with mock.patch('builtins.input', return_value ="1"):
        assert venusaur.use_attack() == 60
    with mock.patch('builtins.input', return_value="2"):
        assert venusaur.use_attack() == 75

# Test twenty-one
def test_use_attack_abra():
    abra = Abra("ABRA",100)

    with mock.patch('builtins.input', return_value ="1"):
        assert abra.use_attack() == 30
    with mock.patch('builtins.input', return_value="2"):
        assert abra.use_attack() == 30

# Test twenty-two
def test_use_attack_kadabra():
    kadabra = Kadabra("kad",200)

    with mock.patch('builtins.input', return_value ="1"):
        assert kadabra.use_attack() == 50
    with mock.patch('builtins.input', return_value="2"):
        assert kadabra.use_attack() == 50

# Test Twenty-three
def test_use_attack_alakazam():
    alakazam = Alakazam("alakazam", 30)

    with mock.patch('builtins.input', return_value ="1"):
        assert alakazam.use_attack() == 50
    with mock.patch('builtins.input', return_value="2"):
        assert alakazam.use_attack() == 75

#Test Twenty-four
def test_use_attack_mewtwo():
    mewtwo = Mewtwo("Mewtwo",400)

    with mock.patch('builtins.input', return_value ="1"):
        assert mewtwo.use_attack() == 75
    with mock.patch('builtins.input', return_value="2"):
        assert mewtwo.use_attack() == 60


def test_evolution():
    charmander = Charmander("charmander",100)
    back_1 = [charmander]
    ash_1 = Player(back_1)

    pokemon_2 = Charmeleon("charmeleon", 200)
    back_2 = [pokemon_2]
    ash_2 = Player(back_2)

    chimchar = Chimchar("chimchar", 100)
    back_3 = [chimchar]
    ash_3 = Player(back_3)

    monferno = Monferno("monferno",200)
    back_4 = [monferno]
    ash_4 = Player(back_4)

    squirtle = Squirtle("squirtle", 100)
    back_5 = [squirtle]
    ash_5 = Player(back_5)

    wartortle = Wartortle("wartortle", 200)
    back_6 = [wartortle]
    ash_6 = Player(back_6)

    bulbasaur = Bulbasaur("bulbasaur",100)
    back_7 = [bulbasaur]
    ash_7 = Player(back_7)

    ivysaur = Ivysaur("ivysaur",200)
    back_8 = [ivysaur]
    ash_8 = Player(back_8)

    abra = Abra("abra",100)
    back_9 = [abra]
    ash_9 = Player(back_9)

    kadabra = Kadabra("kadabra",200)
    back_10 = [kadabra]
    ash_10 = Player(back_10)

    ash_1.evolve_pokemon("charmander")
    assert isinstance(ash_1.backpack[0], Charmeleon)
    ash_2.evolve_pokemon("charmeleon")
    assert isinstance(ash_2.backpack[0], Charizard)
    ash_3.evolve_pokemon("chimchar")
    assert isinstance(ash_3.backpack[0], Monferno)
    ash_4.evolve_pokemon("monferno")
    assert isinstance(ash_4.backpack[0], Infernape)
    ash_5.evolve_pokemon("squirtle")
    assert isinstance(ash_5.backpack[0], Wartortle)
    ash_6.evolve_pokemon("wartortle")
    assert isinstance(ash_6.backpack[0], Blastoise)
    ash_7.evolve_pokemon("bulbasaur")
    assert isinstance(ash_7.backpack[0], Ivysaur)
    ash_8.evolve_pokemon("ivysaur")
    assert isinstance(ash_8.backpack[0], Venusaur)
    ash_9.evolve_pokemon("abra")
    assert isinstance(ash_9.backpack[0], Kadabra)
    ash_10.evolve_pokemon("kadabra")
    assert isinstance(ash_10.backpack[0], Alakazam)
         










    