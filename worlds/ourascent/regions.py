from typing import TYPE_CHECKING, Dict, List

from BaseClasses import Entrance, Region
from .locations import LocationData
from .rules import apolonia_offense


if TYPE_CHECKING:
    from .world import OurAscentWorld

def create_and_connect_regions(world: OurAscentWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: OurAscentWorld) -> None:
    story_select = Region("Story Select", world.player, world.multiworld)
    APOLONIA_STAGE_0 = Region("1-1 Beginning-Right", world.player, world.multiworld)
    APOLONIA_STAGE_1 = Region("1-1 Beginning-Left", world.player, world.multiworld)
    APOLONIA_STAGE_2 = Region("1-1 Further Right", world.player, world.multiworld)
    APOLONIA_STAGE_3 = Region("1-1 Further Left", world.player, world.multiworld)
    APOLONIA_STAGE_4 = Region("1-1 Furthest Right", world.player, world.multiworld)
    APOLONIA_STAGE_5 = Region("1-1 Furthest Left", world.player, world.multiworld)
    APOLONIA_STAGE_6 = Region("1-1 Center", world.player, world.multiworld)
    APOLONIA_STAGE_7 = Region("1-1 Center Continued", world.player, world.multiworld)
    APOLONIA_STAGE_8 = Region("1-1 Endgame", world.player, world.multiworld)

    regions = [story_select, APOLONIA_STAGE_0, APOLONIA_STAGE_1, APOLONIA_STAGE_2, APOLONIA_STAGE_3, APOLONIA_STAGE_4, APOLONIA_STAGE_5, APOLONIA_STAGE_6, APOLONIA_STAGE_7, APOLONIA_STAGE_8]

def connect_regions(world: OurAscentWorld) -> None:
    story_select = world.get_region("Main Menu")
    APOLONIA_STAGE_0 = world.get_region("1-1 Beginning-Right")
    APOLONIA_STAGE_1 = world.get_region("1-1 Beginning-Left")
    APOLONIA_STAGE_2 = world.get_region("1-1 Further Right")
    APOLONIA_STAGE_3 = world.get_region("1-1 Further Left")
    APOLONIA_STAGE_4 = world.get_region("1-1 Furthest Right")
    APOLONIA_STAGE_5 = world.get_region("1-1 Furthest Left")
    APOLONIA_STAGE_6 = world.get_region("1-1 Center")
    APOLONIA_STAGE_7 = world.get_region("1-1 Center Continued")
    APOLONIA_STAGE_8 = world.get_region("1-1 Endgame")

    #Story 1-1
    story_select.connect(APOLONIA_STAGE_0, "Begin story 1-1 to level 100 boss", lambda state: state.has("Character - Playable Apolonia", world.player, 1))
    APOLONIA_STAGE_0.connect(APOLONIA_STAGE_1, "Take left path to level 200 boss",  lambda state: state.has(apolonia_offense, world.player, 5))
    APOLONIA_STAGE_0.connect(APOLONIA_STAGE_2, "Continue right path to level 700 boss", lambda state: state.has(apolonia_offense, world.player, 13))
    APOLONIA_STAGE_1.connect(APOLONIA_STAGE_3, "Continue left path to level 500 boss", lambda state: state.has(apolonia_offense, world.player, 12))
    APOLONIA_STAGE_2.connect(APOLONIA_STAGE_4, "Continue right path to level 1200 boss", lambda state: state.has(apolonia_offense, world.player, 20))
    APOLONIA_STAGE_3.connect(APOLONIA_STAGE_5, "Continue left path to level 1300 boss", lambda state: state.has(apolonia_offense, world.player, 19))
    APOLONIA_STAGE_4.connect(APOLONIA_STAGE_6, "Take right path to level 3000 boss", lambda state: state.has(apolonia_offense, world.player, 30))
    APOLONIA_STAGE_5.connect(APOLONIA_STAGE_6, "Take left path to level 3000 boss", lambda state: state.has(apolonia_offense, world.player, 30))
    APOLONIA_STAGE_6.connect(APOLONIA_STAGE_7, "Continue central area to level 5000 boss", lambda state: state.has(apolonia_offense, world.player, 40))
    APOLONIA_STAGE_7.connect(APOLONIA_STAGE_8, "Go north from central area to endgame", lambda state: state.has(apolonia_offense, world.player, 48))

def get_locations_per_ap_region(locations: List[LocationData]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.regions, []).append(location)

    return per_region