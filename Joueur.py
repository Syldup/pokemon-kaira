from typing import List

from TeamPoke import TeamPoke


class Joueur:
    def __init__(self, name: str):
        self.name: str = name
        self.pokemons: List[TeamPoke] = []

    def addPokemon(self, pokemon: TeamPoke):
        self.pokemons.append(pokemon)
