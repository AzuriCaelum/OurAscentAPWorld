from typing import List, NamedTuple
from .item_names import *

class PowerBreakpoint(NamedTuple):
    item: str
    count: int
    level: int

def ApoloniaEquipmentBreakpoints() -> List[PowerBreakpoint]:
    breakpoint_table = [ #28 max
        PowerBreakpoint(APOLONIA_SWORD, 2, 1),
        PowerBreakpoint(APOLONIA_SWORD, 4, 2),
        PowerBreakpoint(APOLONIA_SWORD, 6, 2),
        PowerBreakpoint(APOLONIA_SWORD, 8, 3),
        PowerBreakpoint(APOLONIA_SWORD, 10, 3),
        PowerBreakpoint(APOLONIA_SHIELD, 3, 1),
        PowerBreakpoint(APOLONIA_SHIELD, 5, 2),
        PowerBreakpoint(APOLONIA_SHIELD, 7, 2),
        PowerBreakpoint(APOLONIA_HELMET, 3, 1),
        PowerBreakpoint(APOLONIA_HELMET, 5, 2),
        PowerBreakpoint(APOLONIA_HELMET, 6, 2),
        PowerBreakpoint(APOLONIA_HELMET, 8, 3),
        PowerBreakpoint(APOLONIA_HELMET, 9, 3),
        PowerBreakpoint(APOLONIA_BREASTPLATE, 3, 1),
        PowerBreakpoint(APOLONIA_BREASTPLATE, 5, 2),
        PowerBreakpoint(APOLONIA_BREASTPLATE, 6, 2),
        PowerBreakpoint(APOLONIA_BREASTPLATE, 8, 3),
        PowerBreakpoint(APOLONIA_BREASTPLATE, 9, 3),
        PowerBreakpoint(APOLONIA_GLOVES, 3, 1),
        PowerBreakpoint(APOLONIA_GLOVES, 5, 2),
        PowerBreakpoint(APOLONIA_GLOVES, 6, 2),
        PowerBreakpoint(APOLONIA_GLOVES, 8, 3),
        PowerBreakpoint(APOLONIA_GLOVES, 9, 3),
        PowerBreakpoint(APOLONIA_BOOTS, 3, 1),
        PowerBreakpoint(APOLONIA_BOOTS, 5, 2),
        PowerBreakpoint(APOLONIA_BOOTS, 6, 2),
        PowerBreakpoint(APOLONIA_BOOTS, 8, 3),
        PowerBreakpoint(APOLONIA_BOOTS, 9, 3)
    ]
    return breakpoint_table

def StanEquipmentBreakpoints() -> List[PowerBreakpoint]:
    breakpoint_table = [ #26 max
        PowerBreakpoint(STAN_SWORD, 2, 1),
        PowerBreakpoint(STAN_SWORD, 4, 2),
        PowerBreakpoint(STAN_SWORD, 6, 2),
        PowerBreakpoint(STAN_SWORD, 8, 3),
        PowerBreakpoint(STAN_SWORD, 10, 3),
        PowerBreakpoint(STAN_SNACK, 2, 1),
        PowerBreakpoint(STAN_SNACK, 4, 2),
        PowerBreakpoint(STAN_SNACK, 5, 2),
        PowerBreakpoint(STAN_SNACK, 7, 3),
        PowerBreakpoint(STAN_SHIRT, 3, 1),
        PowerBreakpoint(STAN_SHIRT, 5, 2),
        PowerBreakpoint(STAN_SHIRT, 6, 2),
        PowerBreakpoint(STAN_SHIRT, 9, 3),
        PowerBreakpoint(STAN_GLOVES, 3, 1),
        PowerBreakpoint(STAN_GLOVES, 5, 2),
        PowerBreakpoint(STAN_GLOVES, 8, 3),
        PowerBreakpoint(STAN_GLOVES, 9, 3),
        PowerBreakpoint(STAN_BELT, 3, 1),
        PowerBreakpoint(STAN_BELT, 5, 2),
        PowerBreakpoint(STAN_BELT, 6, 2),
        PowerBreakpoint(STAN_BELT, 9, 3),
        PowerBreakpoint(STAN_PANTS, 2, 1),
        PowerBreakpoint(STAN_PANTS, 4, 2),
        PowerBreakpoint(STAN_PANTS, 6, 2),
        PowerBreakpoint(STAN_PANTS, 7, 3),
        PowerBreakpoint(STAN_PANTS, 9, 3)
    ]
    return breakpoint_table

def HinaEquipmentBreakpoints() -> List[PowerBreakpoint]:
    breakpoint_table = [ #33 max
        PowerBreakpoint(HINA_RWEAPON, 2, 1),
        PowerBreakpoint(HINA_RWEAPON, 4, 2),
        PowerBreakpoint(HINA_RWEAPON, 6, 2),
        PowerBreakpoint(HINA_RWEAPON, 8, 3),
        PowerBreakpoint(HINA_RWEAPON, 10, 3),
        PowerBreakpoint(HINA_RWEAPON, 11, 3),
        PowerBreakpoint(HINA_RWEAPON, 13, 3),
        PowerBreakpoint(HINA_SNACK, 2, 1),
        PowerBreakpoint(HINA_SNACK, 4, 2),
        PowerBreakpoint(HINA_SNACK, 5, 2),
        PowerBreakpoint(HINA_SNACK, 7, 3),
        PowerBreakpoint(HINA_HELMET, 3, 1),
        PowerBreakpoint(HINA_HELMET, 5, 2),
        PowerBreakpoint(HINA_HELMET, 6, 2),
        PowerBreakpoint(HINA_HELMET, 8, 3),
        PowerBreakpoint(HINA_HELMET, 9, 3),
        PowerBreakpoint(HINA_SHIRT, 3, 1),
        PowerBreakpoint(HINA_SHIRT, 5, 2),
        PowerBreakpoint(HINA_SHIRT, 6, 2),
        PowerBreakpoint(HINA_SHIRT, 8, 3),
        PowerBreakpoint(HINA_SHIRT, 9, 3),
        PowerBreakpoint(HINA_CLOAK, 3, 1),
        PowerBreakpoint(HINA_CLOAK, 5, 2),
        PowerBreakpoint(HINA_CLOAK, 6, 2),
        PowerBreakpoint(HINA_CLOAK, 8, 3),
        PowerBreakpoint(HINA_CLOAK, 10, 3),
        PowerBreakpoint(HINA_LWEAPON, 2, 1),
        PowerBreakpoint(HINA_LWEAPON, 4, 2),
        PowerBreakpoint(HINA_LWEAPON, 6, 2),
        PowerBreakpoint(HINA_LWEAPON, 8, 3),
        PowerBreakpoint(HINA_LWEAPON, 10, 3),
        PowerBreakpoint(HINA_LWEAPON, 11, 3),
        PowerBreakpoint(HINA_LWEAPON, 13, 3)
    ]
    return breakpoint_table

def LanEquipmentBreakpoints() -> List[PowerBreakpoint]:
    breakpoint_table = [ #25 max
        PowerBreakpoint(LAN_BOW, 2, 1),
        PowerBreakpoint(LAN_BOW, 4, 2),
        PowerBreakpoint(LAN_BOW, 6, 2),
        PowerBreakpoint(LAN_BOW, 9, 3),
        PowerBreakpoint(LAN_ARROW, 2, 1),
        PowerBreakpoint(LAN_ARROW, 4, 2),
        PowerBreakpoint(LAN_ARROW, 6, 2),
        PowerBreakpoint(LAN_ARROW, 9, 3),
        PowerBreakpoint(LAN_HAT, 3, 1),
        PowerBreakpoint(LAN_HAT, 5, 2),
        PowerBreakpoint(LAN_HAT, 6, 2),
        PowerBreakpoint(LAN_HAT, 9, 3),
        PowerBreakpoint(LAN_BELT, 3, 1),
        PowerBreakpoint(LAN_BELT, 5, 2),
        PowerBreakpoint(LAN_BELT, 6, 2),
        PowerBreakpoint(LAN_BELT, 9, 3),
        PowerBreakpoint(LAN_CLOAK, 3, 1),
        PowerBreakpoint(LAN_CLOAK, 5, 2),
        PowerBreakpoint(LAN_CLOAK, 6, 2),
        PowerBreakpoint(LAN_CLOAK, 8, 3),
        PowerBreakpoint(LAN_CLOAK, 10, 3),
        PowerBreakpoint(LAN_PANTS, 3, 1),
        PowerBreakpoint(LAN_PANTS, 5, 2),
        PowerBreakpoint(LAN_PANTS, 6, 2),
        PowerBreakpoint(LAN_PANTS, 9, 3)
    ]
    return breakpoint_table

def SibylEquipmentBreakpoints() -> List[PowerBreakpoint]:
    breakpoint_table = [ #31 max
        PowerBreakpoint(SIBYL_ACCESSORY, 2, 1),
        PowerBreakpoint(SIBYL_ACCESSORY, 4, 2),
        PowerBreakpoint(SIBYL_ACCESSORY, 6, 2),
        PowerBreakpoint(SIBYL_ACCESSORY, 8, 3),
        PowerBreakpoint(SIBYL_ACCESSORY, 10, 3),
        PowerBreakpoint(SIBYL_LWEAPON, 2, 1),
        PowerBreakpoint(SIBYL_LWEAPON, 4, 2),
        PowerBreakpoint(SIBYL_LWEAPON, 6, 2),
        PowerBreakpoint(SIBYL_LWEAPON, 8, 3),
        PowerBreakpoint(SIBYL_LWEAPON, 10, 3),
        PowerBreakpoint(SIBYL_LWEAPON, 11, 3),
        PowerBreakpoint(SIBYL_LWEAPON, 13, 3),
        PowerBreakpoint(SIBYL_RWEAPON, 2, 1),
        PowerBreakpoint(SIBYL_RWEAPON, 4, 2),
        PowerBreakpoint(SIBYL_RWEAPON, 6, 2),
        PowerBreakpoint(SIBYL_RWEAPON, 8, 3),
        PowerBreakpoint(SIBYL_RWEAPON, 10, 3),
        PowerBreakpoint(SIBYL_RWEAPON, 11, 3),
        PowerBreakpoint(SIBYL_RWEAPON, 13, 3),
        PowerBreakpoint(SIBYL_POUCH, 2, 1),
        PowerBreakpoint(SIBYL_POUCH, 4, 2),
        PowerBreakpoint(SIBYL_POUCH, 5, 2),
        PowerBreakpoint(SIBYL_POUCH, 7, 3),
        PowerBreakpoint(SIBYL_GLOVES, 3, 1),
        PowerBreakpoint(SIBYL_GLOVES, 5, 2),
        PowerBreakpoint(SIBYL_GLOVES, 6, 2),
        PowerBreakpoint(SIBYL_GLOVES, 9, 3),
        PowerBreakpoint(SIBYL_BOOTS, 3, 1),
        PowerBreakpoint(SIBYL_BOOTS, 5, 2),
        PowerBreakpoint(SIBYL_BOOTS, 6, 2),
        PowerBreakpoint(SIBYL_BOOTS, 9, 3)
    ]
    return breakpoint_table