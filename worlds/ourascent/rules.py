from typing import List, TYPE_CHECKING, NamedTuple

from BaseClasses import CollectionState
from .constants import item_names
from .constants.ap_regions import *
from .constants.power_breakpoints import *
from .options import OurAscentOptions


if TYPE_CHECKING:
    from . import OurAscentWorld

class OurAscentLogic:
    player: int
    options: OurAscentOptions

    def __init__(self, player: int, options: OurAscentOptions):
        self.player = player
        self.options = options

    def can_use_holy_power(self, state: CollectionState):
        return state.has("Augment - Apolonia Magical Imbuement", self.player) & state.has("Augment - Apolonia Weapon Mastery", self.player)

    def can_use_fierce_onslaught(self, state: CollectionState):
        return state.has("Augment - Stan Swift Steps", self.player) & state.has("Augment - Stan Amplified Strength", self.player)

    def can_use_form_training(self, state: CollectionState):
        return state.has("Augment - Hina Sinister Serpent", self.player) & state.has("Augment - Hina Tenacious Tiger", self.player)

    def can_use_speed_training(self, state: CollectionState):
        return state.has("Augment - Hina Patient Panda", self.player) & state.has("Augment - Hina Tenacious Tiger", self.player)

    def can_use_kick_training(self, state: CollectionState):
        return state.has("Augment - Hina Patient Panda", self.player) & state.has("Augment - Hina Mighty Monkey", self.player)

    def can_use_punch_training(self, state: CollectionState):
        return state.has("Augment - Hina Sinister Serpent", self.player) & state.has("Augment - Hina Mighty Monkey", self.player)

    def can_use_bloodthirsty_quiver(self, state: CollectionState):
        return state.has("Augment - Lan Lucky Shots", self.player)

    def can_use_killer_instinct(self, state: CollectionState):
        return state.has("Augment - Lan Bloodthirsty Quiver", self.player)

    def can_use_relentless_fire(self, state: CollectionState):
        return state.has("Augment - Lan Lucky Shots", self.player)

    def can_use_hunters_insight(self, state: CollectionState):
        return state.has("Augment - Lan Hunter's Insight", self.player)

    def can_use_grounded_motion(self, state: CollectionState):
        return state.has("Augment - Sibyl Silent Steps", self.player)

    def can_use_stunning_distraction(self, state: CollectionState):
        return state.has("Augment - Sibyl Dual Depredation", self.player)

    def apolonia_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = sum(1 for b in ApoloniaEquipmentBreakpoints() if
                    b.level <= progression and state.count(b.item, self.player) >= b.count)
        power += state.count("Augment - Apolonia Weapon Mastery", self.player)
        power += state.count("Augment - Apolonia Weapon Imbuement", self.player)
        power += state.count("Augment - Apolonia Mobility", self.player)
        if self.can_use_holy_power(state):
            power += state.count("Augment - Apolonia Holy Power", self.player)

        return power >= amount

    def stan_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = sum(1 for b in StanEquipmentBreakpoints() if
                    b.level <= progression and state.count(b.item, self.player) >= b.count)
        power += state.count("Augment - Stan Amplified Strength", self.player)
        power += state.count("Augment - Stan Swift Steps", self.player)
        power += state.count("Augment - Stan Defiant Guard", self.player)
        power += state.count("Augment - Stan Vitality Boost", self.player)
        if self.can_use_fierce_onslaught(state):
            power += state.count("Augment - Stan Fierce Onslaught", self.player)

        return power >= amount

    def hina_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = sum(1 for b in HinaEquipmentBreakpoints() if
                    b.level <= progression and state.count(b.item, self.player) >= b.count)
        power += state.count("Augment - Hina Patient Panda", self.player)
        power += state.count("Augment - Hina Mighty Monkey", self.player)
        power += state.count("Augment - Hina Tenacious Tiger", self.player)
        power += state.count("Augment - Hina Sinister Serpent", self.player)
        if self.can_use_form_training(state):
            power += state.count("Augment - Hina Form Training", self.player)
        if self.can_use_kick_training(state):
            power += state.count("Augment - Hina Kick Training", self.player)
        if self.can_use_punch_training(state):
            power += state.count("Augment - Hina Punch Training", self.player)
        if self.can_use_speed_training(state):
            power += state.count("Augment - Hina Speed Training", self.player)

        return power >= amount

    def lan_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = sum(1 for b in LanEquipmentBreakpoints() if
                    b.level <= progression and state.count(b.item, self.player) >= b.count)
        power += state.count("Augment - Lan Lucky Shots", self.player)
        if self.can_use_relentless_fire(state):
            power += state.count("Augment - Lan Relentless Fire", self.player)
            if self.can_use_hunters_insight(state):
                power += state.count("Augment - Lan Hunter's Insight", self.player)
        if self.can_use_bloodthirsty_quiver(state):
            power += state.count("Augment - Lan Bloodthirsty Quiver", self.player)
            if self.can_use_killer_instinct(state):
                power += state.count("Augment - Lan Killer Instinct", self.player)

        return power >= amount

    def sibyl_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = sum(1 for b in SibylEquipmentBreakpoints() if
                    b.level <= progression and state.count(b.item, self.player) >= b.count)
        power += state.count("Augment - Sibyl Silent Steps", self.player)
        power += state.count("Augment - Sibyl Dual Depredation", self.player)
        power += state.count("Augment - Sibyl Ruinous Bleed", self.player)
        if self.can_use_grounded_motion(state):
            power += state.count("Augment - Sibyl Grounded Motion", self.player)
        if self.can_use_stunning_distraction(state):
            power += state.count("Augment - Sibyl Stunning Distraction", self.player)

        return power >= amount


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