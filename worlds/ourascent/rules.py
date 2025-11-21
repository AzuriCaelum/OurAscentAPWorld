from typing import List, TYPE_CHECKING

from BaseClasses import CollectionState
from .options import OurAscentOptions
from .constants.ap_regions import *

if TYPE_CHECKING:
    from . import OurAscentWorld

class OurAscentLogic:
    player: int
    options: OurAscentOptions

    def __init__(self, player: int, options: OurAscentOptions):
        self.player = player
        self.options = options

    def apolonia_power(self, state: CollectionState, amount: int) -> bool:
        return state.has_from_list(apolonia_offense, self.player, amount)

    def stan_power(self, state: CollectionState, amount: int) -> bool:
        return state.has_from_list(stan_offense, self.player, amount)

    def hina_power(self, state: CollectionState, amount: int) -> bool:
        return state.has_from_list(hina_offense, self.player, amount)

    def lan_power(self, state: CollectionState, amount: int) -> bool:
        return state.has_from_list(lan_offense, self.player, amount)

    def sibyl_power(self, state: CollectionState, amount: int) -> bool:
        return state.has_from_list(sibyl_offense, self.player, amount)

def goal_regions(state: CollectionState) -> bool:
    if OurAscentOptions.last_chapter == 1:
        if 1 in OurAscentWorld.playable_stories:
            if not state.can_reach(FALLING_INTO_CHAOS_8):
                return False
        if 2 in OurAscentWorld.playable_stories:
            if not state.can_reach(RISING_TO_THE_CHALLENGE_8):
                return False
        if 3 in OurAscentWorld.playable_stories:
            if not state.can_reach(UNLEASHING_THE_BEAST_8):
                return False
        if 4 in OurAscentWorld.playable_stories:
            if not state.can_reach(HUNTING_FOR_TRUTH_8):
                return False
        if 5 in OurAscentWorld.playable_stories:
            if not state.can_reach(LURKING_IN_THE_SHADOWS_8):
                return False
    return True




apolonia_offense: List[str] = [
    "Equipment - Apolonia Progressive Sword",
    "Equipment - Apolonia Progressive Shield",
    "Equipment - Apolonia Progressive Helmet",
    "Equipment - Apolonia Progressive Breastplate",
    "Equipment - Apolonia Progressive Gloves",
    "Equipment - Apolonia Progressive Boots"
]

stan_offense: List[str] = [
    "Equipment - Stan Progressive Sword",
    "Equipment - Stan Progressive Snack",
    "Equipment - Stan Progressive Shirt",
    "Equipment - Stan Progressive Gloves",
    "Equipment - Stan Progressive Belt",
    "Equipment - Stan Progressive Pants"
]

hina_offense: List[str] = [
    "Equipment - Hina Progressive Right Weapon",
    "Equipment - Hina Progressive Snack",
    "Equipment - Hina Progressive Helmet",
    "Equipment - Hina Progressive Shirt",
    "Equipment - Hina Progressive Cloak",
    "Equipment - Hina Progressive Left Weapon"
]

lan_offense: List[str] = [
    "Equipment - Lan Progressive Bow",
    "Equipment - Lan Progressive Arrow",
    "Equipment - Lan Progressive Hat",
    "Equipment - Lan Progressive Belt",
    "Equipment - Lan Progressive Cloak",
    "Equipment - Lan Progressive Pants"
]

sibyl_offense: List[str] = [
    "Equipment - Sibyl Progressive Accessory",
    "Equipment - Sibyl Progressive Left Weapon",
    "Equipment - Sibyl Progressive Right Weapon",
    "Equipment - Sibyl Progressive Pouch",
    "Equipment - Sibyl Progressive Gloves",
    "Equipment - Sibyl Progressive Boots"
]