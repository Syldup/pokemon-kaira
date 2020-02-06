import string
from typing import List

import TeamPoke


class Joueur:
    name: string
    pokemons: List[TeamPoke]

    def __init__(self, name: string):
        self.name = name
        self.pokemons = []

    def addPokemon(self, pokemon: TeamPoke):
        self.pokemons.append(pokemon)
