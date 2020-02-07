from typing import List

from models.teamPoke import TeamPoke


class Joueur:
    def __init__(self, name: str):
        self.name: str = name
        self.pokemons: List[TeamPoke] = TeamPoke.get_rmd_team()

    def main_poke(self) -> TeamPoke:
        return self.pokemons[0]
