from typing import List, TYPE_CHECKING

from BaseClasses import CollectionState
from .constants import item_names
from .constants.ap_regions import *
from .options import OurAscentOptions


if TYPE_CHECKING:
    from . import OurAscentWorld

class OurAscentLogic:
    player: int
    options: OurAscentOptions

    def __init__(self, player: int, options: OurAscentOptions):
        self.player = player
        self.options = options

    def apolonia_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = 0
        #Determine the total power of Apolonia's equipment. Only take the highest progression step due to scaling.
        count1 = state.count(item_names.APOLONIA_SWORD, self.player)
        count2 = state.count(item_names.APOLONIA_SHIELD, self.player)
        count3 = state.count(item_names.APOLONIA_HELMET, self.player)
        count4 = state.count(item_names.APOLONIA_BREASTPLATE, self.player)
        count5 = state.count(item_names.APOLONIA_GLOVES, self.player)
        count6 = state.count(item_names.APOLONIA_BOOTS, self.player)
        if progression >= 3: #Max 9
            if count1 >= 9:
                power += 2
            elif count1 >= 8:
                power += 1
            if count2 >= 7:
                power += 1
            if count3 >= 8:
                power += 1
            if count4 >= 9:
                power += 2
            elif count4 >= 8:
                power += 1
            if count5 >= 9:
                power += 1
            if count6 >= 8:
                power += 2
            elif count6 >= 7:
                power += 1
        elif progression >= 2: #Max 11
            if count1 >= 6:
                power += 2
            elif count1 >= 4:
                power += 1
            if count2 >= 5:
                power += 2
            elif count2 >= 4:
                power += 1
            if count3 >= 6:
                power += 2
            elif count3 >= 5:
                power = power + 1
            if count4 >= 5:
                power += 1
            if count5 >= 6:
                power += 2
            elif count5 >= 5:
                power += 1
            if count6 >= 6:
                power += 2
            elif count6 >= 4:
                power += 1
        elif progression == 1: #Max 6
            if count1 >= 2:
                power += 1
            if count2 >= 2:
                power += 1
            if count3 >= 3:
                power += 1
            if count4 >= 3:
                power += 1
            if count5 >= 3:
                power += 1
            if count6 >= 2:
                power += 1
        #print("Apolonia Power:", power, "Amount:", amount)
        return power >= amount

    def stan_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = 0
        #Determine the total power of Stan's equipment. Only take the highest progression step due to scaling.
        count1 = state.count(item_names.STAN_SWORD, self.player)
        count2 = state.count(item_names.STAN_SNACK, self.player)
        count3 = state.count(item_names.STAN_SHIRT, self.player)
        count4 = state.count(item_names.STAN_GLOVES, self.player)
        count5 = state.count(item_names.STAN_BELT, self.player)
        count6 = state.count(item_names.STAN_PANTS, self.player)
        if progression >= 3: #Max 9
            if count1 >= 9:
                power += 2
            elif count1 >= 8:
                power += 1
            if count2 >= 7:
                power += 1
            if count3 >= 8:
                power += 1
            if count4 >= 9:
                power += 2
            elif count4 >= 8:
                power += 1
            if count5 >= 9:
                power += 1
            if count6 >= 8:
                power += 2
            elif count6 >= 7:
                power += 1
        elif progression >= 2: #Max 11
            if count1 >= 6:
                power += 2
            elif count1 >= 4:
                power += 1
            if count2 >= 5:
                power += 2
            elif count2 >= 4:
                power += 1
            if count3 >= 6:
                power += 2
            elif count3 >= 5:
                power = power + 1
            if count4 >= 5:
                power += 1
            if count5 >= 6:
                power += 2
            elif count5 >= 5:
                power += 1
            if count6 >= 6:
                power += 2
            elif count6 >= 4:
                power += 1
        elif progression == 1: #Max 6
            if count1 >= 2:
                power += 1
            if count2 >= 2:
                power += 1
            if count3 >= 3:
                power += 1
            if count4 >= 3:
                power += 1
            if count5 >= 3:
                power += 1
            if count6 >= 2:
                power += 1
        #print("Stan Power:", power, "Amount:", amount)
        return power >= amount

    def hina_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = 0
        #Determine the total power of Hina's equipment. Only take the highest progression step due to scaling.
        count1 = state.count(item_names.HINA_RWEAPON, self.player)
        count2 = state.count(item_names.HINA_SNACK, self.player)
        count3 = state.count(item_names.HINA_HELMET, self.player)
        count4 = state.count(item_names.HINA_SHIRT, self.player)
        count5 = state.count(item_names.HINA_CLOAK, self.player)
        count6 = state.count(item_names.HINA_LWEAPON, self.player)
        if progression >= 3: #Max 9
            if count1 >= 9:
                power += 2
            elif count1 >= 8:
                power += 1
            if count2 >= 7:
                power += 1
            if count3 >= 8:
                power += 1
            if count4 >= 9:
                power += 2
            elif count4 >= 8:
                power += 1
            if count5 >= 9:
                power += 1
            if count6 >= 8:
                power += 2
            elif count6 >= 7:
                power += 1
        elif progression >= 2: #Max 11
            if count1 >= 6:
                power += 2
            elif count1 >= 4:
                power += 1
            if count2 >= 5:
                power += 2
            elif count2 >= 4:
                power += 1
            if count3 >= 6:
                power += 2
            elif count3 >= 5:
                power = power + 1
            if count4 >= 5:
                power += 1
            if count5 >= 6:
                power += 2
            elif count5 >= 5:
                power += 1
            if count6 >= 6:
                power += 2
            elif count6 >= 4:
                power += 1
        elif progression == 1: #Max 6
            if count1 >= 2:
                power += 1
            if count2 >= 2:
                power += 1
            if count3 >= 3:
                power += 1
            if count4 >= 3:
                power += 1
            if count5 >= 3:
                power += 1
            if count6 >= 2:
                power += 1
        #print("Hina Power:", power, "Amount:", amount)
        return power >= amount

    def lan_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = 0
        #Determine the total power of Lan's equipment. Only take the highest progression step due to scaling.
        count1 = state.count(item_names.LAN_BOW, self.player)
        count2 = state.count(item_names.LAN_ARROW, self.player)
        count3 = state.count(item_names.LAN_HAT, self.player)
        count4 = state.count(item_names.LAN_BELT, self.player)
        count5 = state.count(item_names.LAN_CLOAK, self.player)
        count6 = state.count(item_names.LAN_PANTS, self.player)
        if progression >= 3: #Max 9
            if count1 >= 9:
                power += 2
            elif count1 >= 8:
                power += 1
            if count2 >= 7:
                power += 1
            if count3 >= 8:
                power += 1
            if count4 >= 9:
                power += 2
            elif count4 >= 8:
                power += 1
            if count5 >= 9:
                power += 1
            if count6 >= 8:
                power += 2
            elif count6 >= 7:
                power += 1
        elif progression >= 2: #Max 11
            if count1 >= 6:
                power += 2
            elif count1 >= 4:
                power += 1
            if count2 >= 5:
                power += 2
            elif count2 >= 4:
                power += 1
            if count3 >= 6:
                power += 2
            elif count3 >= 5:
                power = power + 1
            if count4 >= 5:
                power += 1
            if count5 >= 6:
                power += 2
            elif count5 >= 5:
                power += 1
            if count6 >= 6:
                power += 2
            elif count6 >= 4:
                power += 1
        elif progression == 1: #Max 6
            if count1 >= 2:
                power += 1
            if count2 >= 2:
                power += 1
            if count3 >= 3:
                power += 1
            if count4 >= 3:
                power += 1
            if count5 >= 3:
                power += 1
            if count6 >= 2:
                power += 1
        #print("Lan Power:", power, "Amount:", amount)
        return power >= amount

    def sibyl_power(self, state: CollectionState, progression: int, amount: int) -> bool:
        power = int(0)
        count1 = state.count(item_names.SIBYL_BOOTS, self.player)
        #Determine the total power of Sibyl's equipment. Only take the highest progression step due to scaling.
        count1 = state.count(item_names.SIBYL_ACCESSORY, self.player)
        count2 = state.count(item_names.SIBYL_LWEAPON, self.player)
        count3 = state.count(item_names.SIBYL_RWEAPON, self.player)
        count4 = state.count(item_names.SIBYL_POUCH, self.player)
        count5 = state.count(item_names.SIBYL_GLOVES, self.player)
        count6 = state.count(item_names.SIBYL_BOOTS, self.player)
        if progression >= 3: #Max 9
            if count1 >= 9:
                power += 2
            elif count1 >= 8:
                power += 1
            if count2 >= 7:
                power += 1
            if count3 >= 8:
                power += 1
            if count4 >= 7:
                power += 2
            elif count4 >= 6:
                power += 1
            if count5 >= 9:
                power += 1
            if count6 >= 8:
                power += 2
            elif count6 >= 7:
                power += 1
        elif progression >= 2: #Max 11
            if count1 >= 6:
                power += 2
            elif count1 >= 4:
                power += 1
            if count2 >= 5:
                power += 2
            elif count2 >= 4:
                power += 1
            if count3 >= 6:
                power += 2
            elif count3 >= 5:
                power += 1
            if count4 >= 5:
                power += 1
            if count5 >= 6:
                power += 2
            elif count5 >= 5:
                power += 1
            if count6 >= 6:
                power += 2
            elif count6 >= 4:
                power += 1
        elif progression == 1: #Max 6
            if count1 >= 2:
                power += 1
            if count2 >= 2:
                power += 1
            if count3 >= 3:
                power += 1
            if count4 >= 3:
                power += 1
            if count5 >= 3:
                power += 1
            if count6 >= 2:
                power += 1
        #print("Sibyl Power:", power, "Amount:", amount)
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