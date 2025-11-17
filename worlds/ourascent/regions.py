from typing import TYPE_CHECKING, Dict, List

from BaseClasses import Region
from .locations import LocationData
from .rules import apolonia_offense


if TYPE_CHECKING:
    from .world import OurAscentWorld

def create_and_connect_regions(world: OurAscentWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: OurAscentWorld) -> None:
    story_select = Region("Story Select", world.player, world.multiworld)
    STAGE_11_REGION_0 = Region("1-1 Beginning-Right", world.player, world.multiworld)
    STAGE_11_REGION_1 = Region("1-1 Beginning-Left", world.player, world.multiworld)
    STAGE_11_REGION_2 = Region("1-1 Further Right", world.player, world.multiworld)
    STAGE_11_REGION_3 = Region("1-1 Further Left", world.player, world.multiworld)
    STAGE_11_REGION_4 = Region("1-1 Furthest Right", world.player, world.multiworld)
    STAGE_11_REGION_5 = Region("1-1 Furthest Left", world.player, world.multiworld)
    STAGE_11_REGION_6 = Region("1-1 Center", world.player, world.multiworld)
    STAGE_11_REGION_7 = Region("1-1 Center Continued", world.player, world.multiworld)
    STAGE_11_REGION_8 = Region("1-1 Endgame", world.player, world.multiworld)

    regions = [story_select, STAGE_11_REGION_0, STAGE_11_REGION_1, STAGE_11_REGION_2, STAGE_11_REGION_3, STAGE_11_REGION_4, STAGE_11_REGION_5, STAGE_11_REGION_6, STAGE_11_REGION_7, STAGE_11_REGION_8]

def connect_regions(world: OurAscentWorld) -> None:
    story_select = world.get_region("Main Menu")
    STAGE_11_REGION_0 = world.get_region("1-1 Beginning-Right")
    STAGE_11_REGION_1 = world.get_region("1-1 Beginning-Left")
    STAGE_11_REGION_2 = world.get_region("1-1 Further Right")
    STAGE_11_REGION_3 = world.get_region("1-1 Further Left")
    STAGE_11_REGION_4 = world.get_region("1-1 Furthest Right")
    STAGE_11_REGION_5 = world.get_region("1-1 Furthest Left")
    STAGE_11_REGION_6 = world.get_region("1-1 Center")
    STAGE_11_REGION_7 = world.get_region("1-1 Center Continued")
    STAGE_11_REGION_8 = world.get_region("1-1 Endgame")

    #Story 1-1
    story_select.connect(STAGE_11_REGION_0, "Begin story 1-1 to level 100 boss", lambda state: state.has("Character - Playable Apolonia", world.player, 1))
    STAGE_11_REGION_0.connect(STAGE_11_REGION_1, "Take left path to level 200 boss",  lambda state: state.has(apolonia_offense, world.player, 5))
    STAGE_11_REGION_0.connect(STAGE_11_REGION_2, "Continue right path to level 700 boss", lambda state: state.has(apolonia_offense, world.player, 13))
    STAGE_11_REGION_1.connect(STAGE_11_REGION_3, "Continue left path to level 500 boss", lambda state: state.has(apolonia_offense, world.player, 12))
    STAGE_11_REGION_2.connect(STAGE_11_REGION_4, "Continue right path to level 1200 boss", lambda state: state.has(apolonia_offense, world.player, 20))
    STAGE_11_REGION_3.connect(STAGE_11_REGION_5, "Continue left path to level 1300 boss", lambda state: state.has(apolonia_offense, world.player, 19))
    STAGE_11_REGION_4.connect(STAGE_11_REGION_6, "Take right path to level 3000 boss", lambda state: state.has(apolonia_offense, world.player, 30))
    STAGE_11_REGION_5.connect(STAGE_11_REGION_6, "Take left path to level 3000 boss", lambda state: state.has(apolonia_offense, world.player, 30))
    STAGE_11_REGION_6.connect(STAGE_11_REGION_7, "Continue central area to level 5000 boss", lambda state: state.has(apolonia_offense, world.player, 40))
    STAGE_11_REGION_7.connect(STAGE_11_REGION_8, "Go north from central area to endgame", lambda state: state.has(apolonia_offense, world.player, 48))

def get_locations_per_ap_region(locations: List[LocationData]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.regions, []).append(location)

    return per_region