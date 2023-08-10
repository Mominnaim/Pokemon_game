from .pokemon_light import Pokemon, Charmander, Charmeleon, Charizard, Player


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
    for poke in backpack:
        assert poke.name == "charizard"


# Test eight
def test_collecting_pokemon():
    backpack = []
    ash = Player(backpack)
    my_friend = Charizard("yer", 400)
    ash.collect_pokemon(my_friend)
    assert len(backpack) == 1
