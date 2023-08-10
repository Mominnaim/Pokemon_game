from .pokemon_light import Pokemon, Charmander, Charmeleon, Charizard


def test_attack_charmander():
    pokemon_1 = Charmander("Charmander", 100)
    damage = pokemon_1.random_attack()
    assert damage == 30


def test_attack_one_charmeleon():
    pokemon_1 = Charmeleon("Charmeleon", 200)
    damage = pokemon_1.attack_one()
    assert damage == 50


def test_attack_two_charmeleon():
    pokemon_1 = Charmeleon("Charmeleon", 200)
    damage = pokemon_1.attack_two()
    assert damage == 50


def test_attack_one_charizard():
    pokemon_1 = Charizard("Charizard", 300)
    damage = pokemon_1.attack_one()
    assert damage == 75


def test_attack_two_charizard():
    pokemon_1 = Charizard("Charizard", 300)
    damage = pokemon_1.attack_two()
    assert damage == 60
