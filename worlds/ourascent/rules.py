from typing import List

from BaseClasses import CollectionState
from worlds.ourascent.options import OurAscentOptions


class OurAscentLogic:
    player: int
    options: OurAscentOptions

    def __init__(self, player: int, options: OurAscentOptions):
        self.player = player
        self.options = options

    def apolonia_power(state: CollectionState, player: int, amount: int):
        return state.has_from_list(apolonia_offense, player, amount)

apolonia_offense: List[str] = [
    "Equipment - Apolonia Progressive Sword",
    "Equipment - Apolonia Progressive Shield",
    "Equipment - Apolonia Progressive Helmet",
    "Equipment - Apolonia Progressive Breastplate",
    "Equipment - Apolonia Progressive Gloves",
    "Equipment - Apolonia Progressive Boots",
]

apolonia_movement: List[str] = [
    "Equipment - Apolonia Progressive Boots",
]