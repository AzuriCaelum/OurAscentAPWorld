from typing import List, TYPE_CHECKING

from BaseClasses import CollectionState
from .options import OurAscentOptions
from .constants.ap_regions import *

if TYPE_CHECKING:
    from .world import OurAscentWorld

class OurAscentLogic:
    player: int
    options: OurAscentOptions

    def __init__(self, player: int, options: OurAscentOptions):
        self.player = player
        self.options = options

    def apolonia_power(self, state: CollectionState, amount: int) -> bool:
        return state.has_from_list(apolonia_offense, self.player, amount)

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

apolonia_movement: List[str] = [
    "Equipment - Apolonia Progressive Boots",
]