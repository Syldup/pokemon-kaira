from typing import List

from models.teamPoke import TeamPoke


class Joueur:
    def __init__(self, name: str):
        self.name: str = name
        self.pokemons: List[TeamPoke] = TeamPoke.get_rmd_team()

    def main_poke(self) -> TeamPoke:
        return self.pokemons[0]

    def switch(self, idx=0):
        if 0 >= idx or idx >= len(self.pokemons):
            pok_ok = [p.hp == 0 for p in self.pokemons]
            idx = pok_ok.index(False) if False in pok_ok else 0
        self.pokemons[0], self.pokemons[idx] = self.pokemons[idx], self.pokemons[0]

    def lose(self) -> bool:
        return all(p.hp == 0 for p in self.pokemons)

    def reset(self):
        for p in self.pokemons:
            p.hp = p.hpMax