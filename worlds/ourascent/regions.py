from typing import TYPE_CHECKING, Dict, List, Callable

from BaseClasses import Region, Location, CollectionState
from .locations import LocationData
from .rules import apolonia_offense
from .stories import *


if TYPE_CHECKING:
    from .world import OurAscentWorld

ap_region_to_story_subregions_dictionary: Dict[str, str] = {}

story_subregions_dictionary: Dict[str, List[str]] = {
    #Glades
    FALLING_INTO_CHAOS: FALLING_INTO_CHAOS_SUBREGIONS,
    RISING_TO_THE_CHALLENGE: RISING_TO_THE_CHALLENGE_SUBREGIONS,
    UNLEASHING_THE_BEAST: UNLEASHING_THE_BEAST_SUBREGIONS,
    HUNTING_FOR_TRUTH: HUNTING_FOR_TRUTH_SUBREGIONS,
    LURKING_IN_THE_SHADOWS: LURKING_IN_THE_SHADOWS_SUBREGIONS
    #1-6

    #Oasis
    #2-1
    #2-2
}

rules_on_regions: Dict[str, Callable[[CollectionState], bool]] = {}

class OurAscentLocation(Location):
    game: str = "OurAscent"

    def __init__(self, player: int, name: str = " ", address = None, parent=None):
        super().__init__(player, name, address, parent)

def create_and_connect_regions(world: OurAscentWorld) -> None:
    create_all_regions(world)
    #connect_regions(world)

def create_all_regions(world: OurAscentWorld, locations: List[LocationData]) -> None:

    multiworld = world.multiworld
    player = world.player

    locations_per_region = get_locations_per_ap_region(locations)

    multiworld.regions += create_a_region(player, world, locations_per_region, STORY_SELECT)

    if 1 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, FALLING_INTO_CHAOS)
        add_region_exit(world, STORY_SELECT, FALLING_INTO_CHAOS_0, lambda state: state.has("Character - Playable Apolonia", world.player, 1))
        add_region_exit(world, FALLING_INTO_CHAOS_0, FALLING_INTO_CHAOS_1, lambda state: state.has(apolonia_offense, world.player, 5))
        add_region_exit(world, FALLING_INTO_CHAOS_0, FALLING_INTO_CHAOS_2, lambda state: state.has(apolonia_offense, world.player, 13))
        add_region_exit(world, FALLING_INTO_CHAOS_1, FALLING_INTO_CHAOS_3, lambda state: state.has(apolonia_offense, world.player, 12))
        add_region_exit(world, FALLING_INTO_CHAOS_2, FALLING_INTO_CHAOS_4, lambda state: state.has(apolonia_offense, world.player, 20))
        add_region_exit(world, FALLING_INTO_CHAOS_3, FALLING_INTO_CHAOS_5, lambda state: state.has(apolonia_offense, world.player, 19))
        add_region_exit(world, FALLING_INTO_CHAOS_4, FALLING_INTO_CHAOS_6, lambda state: state.has(apolonia_offense, world.player, 30))
        add_region_exit(world, FALLING_INTO_CHAOS_5, FALLING_INTO_CHAOS_6, lambda state: state.has(apolonia_offense, world.player, 30))
        add_region_exit(world, FALLING_INTO_CHAOS_6, FALLING_INTO_CHAOS_7, lambda state: state.has(apolonia_offense, world.player, 40))
        add_region_exit(world, FALLING_INTO_CHAOS_7, FALLING_INTO_CHAOS_8, lambda state: state.has(apolonia_offense, world.player, 48))
    if 2 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, RISING_TO_THE_CHALLENGE)
    if 3 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, UNLEASHING_THE_BEAST)
    if 4 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, HUNTING_FOR_TRUTH)
    if 5 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, LURKING_IN_THE_SHADOWS)


#def connect_regions(world: OurAscentWorld) -> None:
#    story_select = world.get_region("Main Menu")
#    FALLING_INTO_CHAOS_0 = world.get_region("1-1 Beginning-Right")
#    FALLING_INTO_CHAOS_1 = world.get_region("1-1 Beginning-Left")
#    FALLING_INTO_CHAOS_2 = world.get_region("1-1 Further Right")
#    FALLING_INTO_CHAOS_3 = world.get_region("1-1 Further Left")
#    FALLING_INTO_CHAOS_4 = world.get_region("1-1 Furthest Right")
#    FALLING_INTO_CHAOS_5 = world.get_region("1-1 Furthest Left")
#    FALLING_INTO_CHAOS_6 = world.get_region("1-1 Center")
#    FALLING_INTO_CHAOS_7 = world.get_region("1-1 Center Continued")
#    FALLING_INTO_CHAOS_8 = world.get_region("1-1 Endgame")

    #Story 1-1
#    story_select.connect(FALLING_INTO_CHAOS_0, "Begin story 1-1 to level 100 boss", lambda state: state.has("Character - Playable Apolonia", world.player, 1))
#    FALLING_INTO_CHAOS_0.connect(FALLING_INTO_CHAOS_1, "Take left path to level 200 boss",  lambda state: state.has(apolonia_offense, world.player, 5))
#    FALLING_INTO_CHAOS_0.connect(FALLING_INTO_CHAOS_2, "Continue right path to level 700 boss", lambda state: state.has(apolonia_offense, world.player, 13))
#    FALLING_INTO_CHAOS_1.connect(FALLING_INTO_CHAOS_3, "Continue left path to level 500 boss", lambda state: state.has(apolonia_offense, world.player, 12))
#    FALLING_INTO_CHAOS_2.connect(FALLING_INTO_CHAOS_4, "Continue right path to level 1200 boss", lambda state: state.has(apolonia_offense, world.player, 20))
#    FALLING_INTO_CHAOS_3.connect(FALLING_INTO_CHAOS_5, "Continue left path to level 1300 boss", lambda state: state.has(apolonia_offense, world.player, 19))
#    FALLING_INTO_CHAOS_4.connect(FALLING_INTO_CHAOS_6, "Take right path to level 3000 boss", lambda state: state.has(apolonia_offense, world.player, 30))
#    FALLING_INTO_CHAOS_5.connect(FALLING_INTO_CHAOS_6, "Take left path to level 3000 boss", lambda state: state.has(apolonia_offense, world.player, 30))
#    FALLING_INTO_CHAOS_6.connect(FALLING_INTO_CHAOS_7, "Continue central area to level 5000 boss", lambda state: state.has(apolonia_offense, world.player, 40))
#    FALLING_INTO_CHAOS_7.connect(FALLING_INTO_CHAOS_8, "Go north from central area to endgame", lambda state: state.has(apolonia_offense, world.player, 48))

def get_locations_per_ap_region(locations: List[LocationData]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.regions, []).append(location)

    return per_region

def create_a_region(player: int, world: "OurAscentWorld", locations_per_region: Dict[str, List[LocationData]], region_name: str):
    ap_regions: List[Region] = []
    ap_region_names = story_subregions_dictionary[region_name]

    for ap_region_name in ap_region_names:
        ap_region = create_ap_region(player, world, locations_per_region, ap_region_name)
        ap_regions.append(ap_region)

    return ap_regions

def create_ap_region(player: int, world: "OurAscentWorld", locations_per_region: Dict[str, List[LocationData]], name: str):
    ap_region = Region(name, player, world.multiworld)
    return ap_region

def add_region_exit(self, region: str, exity: str, rules: Dict[str, Callable[[CollectionState], bool]] | None = None):
    if rules is not None:
        for region_rule in rules:
            if not region_rule in exity:
                raise Exception(
                    f"A rule was defined for the entrance {region} -> {region_rule} but {region_rule} isn't the exit from {region}")

    destination_region = ap_region_to_story_subregions_dictionary[exity]
    if rules is None:
        rules = {}
    rules[exity] = rules_on_regions[destination_region]
    self.multiworld.get_region(region, self.player).add_exits(exity, rules)