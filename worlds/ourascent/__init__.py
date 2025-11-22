#from .world import OurAscentWorld as OurAscentWorld

from typing import Any, List, Set, Dict

from BaseClasses import Item, CollectionState, MultiWorld
from worlds.AutoWorld import World
from . import options, rules, web_world
from .constants.story_data import *
from .items import OurAscentItem, item_table, ItemData, equipment_offset, accessory_offset, filler_items
from .locations import get_location_name_to_id, get_main_menu_locations, get_11_locations, get_12_locations, get_13_locations, get_14_locations, get_15_locations
from .regions import create_all_regions
from .rules import OurAscentLogic, goal_regions
from .stories import *

class OurAscentWorld(World):
    """Our Ascent is an incremental roguelite RPG with many layers of metaprogression."""
    game = "Our Ascent"
    web = web_world.OurAscentWebWorld()

    options_dataclass = options.OurAscentOptions
    options: options.OurAscentOptions

    item_name_to_id = {item: item_table[item].code for item in item_table}
    location_name_to_id = get_location_name_to_id()
    playable_stories = [value for _, value in story_id_to_name.items()]
    starting_story = "1-1: Falling Into Chaos"

    origin_region_name = "Story Select"

    def pre_fill(self):
        from BaseClasses import CollectionState
        from Fill import sweep_from_pool
        state = sweep_from_pool(CollectionState(self.multiworld), self.multiworld.itempool)
        unreachable_locations = [location for location in self.get_locations() if not location.can_reach(state)]
        assert not unreachable_locations, f"All state can't reach all locations: {unreachable_locations}"

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_regions(self) -> None:

        locationss = get_main_menu_locations(self.player, self.options)
        #if 1 in self.playable_stories:
        locationss.extend(get_11_locations(self.player, self.options))
        #if 2 in self.playable_stories:
        locationss.extend(get_12_locations(self.player, self.options))
        #if 3 in self.playable_stories:
        locationss.extend(get_13_locations(self.player, self.options))
        #if 4 in self.playable_stories:
        locationss.extend(get_14_locations(self.player, self.options))
        #if 5 in self.playable_stories:
        locationss.extend(get_15_locations(self.player, self.options))
        create_all_regions(self, locationss, self.options)

    def set_rules(self) -> None:
        count = 0
        range = 1
        while range < 7:
            if range in self.playable_stories:
                count += 1

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Story Completed", count)

    def create_items(self) -> None:
        pool = self.get_all_items()
        self.multiworld.itempool += pool

    def create_item(self, name: str) -> OurAscentItem:
        data = item_table[name]
        return OurAscentItem(name, data.classification, data.code, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict()

    #def get_excluded_items(self):
    #    excluded_items: Set[str] = set()

    #    if self.options.last_chapter.value == 1:
    #        if 1 not in self.playable_stories:
    #            excluded_items.add("Character: Playable Apolonia")


    def get_all_items(self) -> List[Item]:
        pool: List[Item] = []
        amount: int = int(0)
        for name, data in item_table.items():
            #Get the amount of total items across every story within the world, this may change if there is overlap later
            if self.options.last_chapter >= 1:
                if 1 in self.playable_stories:
                    item = self.set_classification("Character: Playable Apolonia")
                    pool.append(item)
                    equipment_range = 1 + equipment_offset
                    while equipment_range < (6 + equipment_offset):
                        amount_range = 1
                        while amount_range < item.story11:
                            pool.append(item)
                    accessory_range = 1 + accessory_offset
                    while accessory_range < (10 + accessory_offset):
                        amount_range = 1
                        while amount_range < item.story11:
                            pool.append(item)
                if 2 in self.playable_stories:
                    amount = amount + int(data.story12)
                if 3 in self.playable_stories:
                    amount = amount + int(data.story13)
                if 4 in self.playable_stories:
                    amount = amount + int(data.story14)
                if 5 in self.playable_stories:
                    amount = amount + int(data.story15)
                if 6 in self.playable_stories:
                    amount = amount + int(data.story16)
        return pool

    def generate_early(self):
        self.get_stories()

    def get_required_stories(self, story_id: int) -> set[int]:
        required_stories = {story_id}
        required_characters = characters_per_story[story_id]

        chapter = story_to_chapter[story_id]

        if chapter != 1:
            for previous_story in stories_per_chapter[chapter - 1]:
                if required_characters & characters_per_story[previous_story]:  # if there is character overlap
                    required_stories |= self.get_required_stories(previous_story)

        return required_stories

    def get_stories(self):
        random_chapter = self.random.choice(list(stories_per_chapter)[1:])  # Don't pick chapter 1
        random_story = self.random.choice(stories_per_chapter[random_chapter])
        stories = self.get_required_stories(random_story)
        stories = sorted(stories)
        stories_from_first_chapter = [story for story in stories if story_to_chapter[story] == 1]
        starting_story = self.random.choice(stories_from_first_chapter)
        self.multiworld.push_precollected(self.create_item(playable_character_to_item[starting_story]))