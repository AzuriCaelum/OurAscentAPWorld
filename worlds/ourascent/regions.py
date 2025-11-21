from typing import Callable, TYPE_CHECKING, List, Optional

from BaseClasses import Region, Location, CollectionState, Entrance
from .items import *
from .locations import LocationData, create_location, create_completion
from .options import OurAscentOptions
from .rules import OurAscentLogic
from .stories import *

if TYPE_CHECKING:
    from . import OurAscentWorld

ap_region_to_story_subregions_dictionary: Dict[str, str] = {}

story_subregions_dictionary: Dict[str, List[str]] = {
    STORY_SELECT: STORY_SELECT_SUBREGIONS,

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

    def __init__(self, player: int, name: str = " ", address=None, parent=None):
        super().__init__(player, name, address, parent)

def create_all_regions(world: "OurAscentWorld", locations: List[LocationData], options: OurAscentOptions) -> None:

    multiworld = world.multiworld
    player = world.player
    logic = OurAscentLogic(player, options)
    completion_count = int(0)

    locations_per_region = get_locations_per_ap_region(locations)

    multiworld.regions += create_a_region(player, world, locations_per_region, STORY_SELECT)

    if 1 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, FALLING_INTO_CHAOS)
        add_region_exit(world, STORY_SELECT, FALLING_INTO_CHAOS_0, lambda state: state.has("Character - Playable Apolonia", world.player, 1))
        add_region_exit(world, FALLING_INTO_CHAOS_0, FALLING_INTO_CHAOS_1, lambda state: logic.apolonia_power(state, 5))
        add_region_exit(world, FALLING_INTO_CHAOS_0, FALLING_INTO_CHAOS_2, lambda state: logic.apolonia_power(state, 13))
        add_region_exit(world, FALLING_INTO_CHAOS_1, FALLING_INTO_CHAOS_3, lambda state: logic.apolonia_power(state, 12))
        add_region_exit(world, FALLING_INTO_CHAOS_2, FALLING_INTO_CHAOS_4, lambda state: logic.apolonia_power(state, 20))
        add_region_exit(world, FALLING_INTO_CHAOS_3, FALLING_INTO_CHAOS_5, lambda state: logic.apolonia_power(state, 19))
        add_region_exit(world, FALLING_INTO_CHAOS_4, FALLING_INTO_CHAOS_6, lambda state: logic.apolonia_power(state, 30))
        add_region_exit(world, FALLING_INTO_CHAOS_5, FALLING_INTO_CHAOS_6, lambda state: logic.apolonia_power(state, 30))
        add_region_exit(world, FALLING_INTO_CHAOS_6, FALLING_INTO_CHAOS_7, lambda state: logic.apolonia_power(state, 40))
        add_region_exit(world, FALLING_INTO_CHAOS_7, FALLING_INTO_CHAOS_8, lambda state: logic.apolonia_power(state, 48))
        completion = world.get_region(FALLING_INTO_CHAOS_8)
        completion_count += 1
        create_completion(world, player, completion)

    if 2 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, RISING_TO_THE_CHALLENGE)
        add_region_exit(world, STORY_SELECT, RISING_TO_THE_CHALLENGE_0, lambda state: state.has("Character - Playable Stan", world.player, 1))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_0, RISING_TO_THE_CHALLENGE_1,  lambda state: logic.stan_power(state, 5))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_0, RISING_TO_THE_CHALLENGE_2, lambda state: logic.stan_power(state, 13))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_1, RISING_TO_THE_CHALLENGE_3, lambda state: logic.stan_power(state, 12))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_2, RISING_TO_THE_CHALLENGE_4, lambda state: logic.stan_power(state, 20))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_3, RISING_TO_THE_CHALLENGE_5, lambda state: logic.stan_power(state, 19))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_4, RISING_TO_THE_CHALLENGE_6, lambda state: logic.stan_power(state, 30))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_5, RISING_TO_THE_CHALLENGE_6, lambda state: logic.stan_power(state, 30))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_6, RISING_TO_THE_CHALLENGE_7, lambda state: logic.stan_power(state, 40))
        add_region_exit(world, RISING_TO_THE_CHALLENGE_7, RISING_TO_THE_CHALLENGE_8, lambda state: logic.stan_power(state, 48))
        completion = world.get_region(RISING_TO_THE_CHALLENGE_8)
        completion_count += 1
        create_completion(world, player, completion)

    if 3 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, UNLEASHING_THE_BEAST)
        add_region_exit(world, STORY_SELECT, UNLEASHING_THE_BEAST_0, lambda state: state.has("Character - Playable Hina", world.player, 1))
        add_region_exit(world, UNLEASHING_THE_BEAST_0, UNLEASHING_THE_BEAST_1, lambda state: logic.hina_power(state, 5))
        add_region_exit(world, UNLEASHING_THE_BEAST_0, UNLEASHING_THE_BEAST_2, lambda state: logic.hina_power(state, 13))
        add_region_exit(world, UNLEASHING_THE_BEAST_1, UNLEASHING_THE_BEAST_3, lambda state: logic.hina_power(state, 12))
        add_region_exit(world, UNLEASHING_THE_BEAST_2, UNLEASHING_THE_BEAST_4, lambda state: logic.hina_power(state, 20))
        add_region_exit(world, UNLEASHING_THE_BEAST_3, UNLEASHING_THE_BEAST_5, lambda state: logic.hina_power(state, 19))
        add_region_exit(world, UNLEASHING_THE_BEAST_4, UNLEASHING_THE_BEAST_6, lambda state: logic.hina_power(state, 30))
        add_region_exit(world, UNLEASHING_THE_BEAST_5, UNLEASHING_THE_BEAST_6, lambda state: logic.hina_power(state, 30))
        add_region_exit(world, UNLEASHING_THE_BEAST_6, UNLEASHING_THE_BEAST_7, lambda state: logic.hina_power(state, 40))
        add_region_exit(world, UNLEASHING_THE_BEAST_7, UNLEASHING_THE_BEAST_8, lambda state: logic.hina_power(state, 48))
        completion = world.get_region(UNLEASHING_THE_BEAST_8)
        completion_count += 1
        create_completion(world, player, completion)

    if 4 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, HUNTING_FOR_TRUTH)
        add_region_exit(world, STORY_SELECT, HUNTING_FOR_TRUTH_0, lambda state: state.has("Character - Playable Lan", world.player, 1))
        add_region_exit(world, HUNTING_FOR_TRUTH_0, HUNTING_FOR_TRUTH_1, lambda state: logic.lan_power(state, 5))
        add_region_exit(world, HUNTING_FOR_TRUTH_0, HUNTING_FOR_TRUTH_2, lambda state: logic.lan_power(state, 13))
        add_region_exit(world, HUNTING_FOR_TRUTH_1, HUNTING_FOR_TRUTH_3, lambda state: logic.lan_power(state, 12))
        add_region_exit(world, HUNTING_FOR_TRUTH_2, HUNTING_FOR_TRUTH_4, lambda state: logic.lan_power(state, 20))
        add_region_exit(world, HUNTING_FOR_TRUTH_3, HUNTING_FOR_TRUTH_5, lambda state: logic.lan_power(state, 19))
        add_region_exit(world, HUNTING_FOR_TRUTH_4, HUNTING_FOR_TRUTH_6, lambda state: logic.lan_power(state, 30))
        add_region_exit(world, HUNTING_FOR_TRUTH_5, HUNTING_FOR_TRUTH_6, lambda state: logic.lan_power(state, 30))
        add_region_exit(world, HUNTING_FOR_TRUTH_6, HUNTING_FOR_TRUTH_7, lambda state: logic.lan_power(state, 40))
        add_region_exit(world, HUNTING_FOR_TRUTH_7, HUNTING_FOR_TRUTH_8, lambda state: logic.lan_power(state, 48))
        completion = world.get_region(HUNTING_FOR_TRUTH_8)
        completion_count += 1
        create_completion(world, player, completion)

    if 5 in world.playable_stories:
        multiworld.regions += create_a_region(player, world, locations_per_region, LURKING_IN_THE_SHADOWS)
        add_region_exit(world, STORY_SELECT, LURKING_IN_THE_SHADOWS_0, lambda state: state.has("Character - Playable Sibyl", world.player, 1))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_0, LURKING_IN_THE_SHADOWS_1, lambda state: logic.sibyl_power(state, 5))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_0, LURKING_IN_THE_SHADOWS_2, lambda state: logic.sibyl_power(state, 13))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_1, LURKING_IN_THE_SHADOWS_3, lambda state: logic.sibyl_power(state, 12))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_2, LURKING_IN_THE_SHADOWS_4, lambda state: logic.sibyl_power(state, 20))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_3, LURKING_IN_THE_SHADOWS_5, lambda state: logic.sibyl_power(state, 19))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_4, LURKING_IN_THE_SHADOWS_6, lambda state: logic.sibyl_power(state, 30))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_5, LURKING_IN_THE_SHADOWS_6, lambda state: logic.sibyl_power(state, 30))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_6, LURKING_IN_THE_SHADOWS_7, lambda state: logic.sibyl_power(state, 40))
        add_region_exit(world, LURKING_IN_THE_SHADOWS_7, LURKING_IN_THE_SHADOWS_8, lambda state: logic.sibyl_power(state, 48))
        completion = world.get_region(LURKING_IN_THE_SHADOWS_8)
        completion_count += 1
        create_completion(world, player, completion)


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

def create_ap_region(player: int, world: "OurAscentWorld", locations_per_region: Dict[str, List[LocationData]], name: str) -> Region:
    logic = OurAscentLogic(player, world.options)
    ap_region = Region(name, player, world.multiworld)

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(player, location_data, ap_region)
            ap_region.locations.append(location)
    return ap_region

def add_region_exit(self, region: str, exity: str, rules: Optional[Callable] = None):
    entrance_region = self.get_region(region)
    exit_region = self.get_region(exity)
    entrance_region.connect(exit_region, rules)
    return region