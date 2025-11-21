#from .world import OurAscentWorld as OurAscentWorld

from typing import Any, List, Set, Dict

from BaseClasses import Item, CollectionState, MultiWorld
from worlds.AutoWorld import World
from . import options, rules, web_world
from .items import OurAscentItem, item_table, ItemData, is_character, equipment_offset, accessory_offset, filler_items
from .locations import get_location_name_to_id, get_main_menu_locations, get_11_locations
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

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_regions(self) -> None:

        locationss = get_main_menu_locations(self.player, self.options)
        if 1 in self.playable_stories:
            locationss.extend(get_11_locations(self.player, self.options))
        #if 2 in self.playable_stories:
        #    locations.extend(get_12_locations(self.player))
        #if 3 in self.playable_stories:
        #    locations.extend(get_13_locations(self.player))
        #if 4 in self.playable_stories:
        #    locations.extend(get_14_locations(self.player))
        #if 5 in self.playable_stories:
        #    locations.extend(get_15_locations(self.player))
        create_all_regions(self, locationss, self.options)

    def set_rules(self) -> None:
        count = 0
        range = 1
        while range < 7:
            if range in self.playable_stories:
                count += 1

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Story Completed", count)

    def create_items(self) -> None:
        pool = self.get_all_items(self.get_excluded_items())
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


    def get_all_items(self, excluded_items: Set[str]) -> List[Item]:
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

    def get_stories(self):
        #Need the list of potential stories from the latest chapter indicated
        playable_story_choice = list(
            [value for key, value in story_id_to_name.items()])
        if self.options.last_chapter == 1:
            story_range = 1
            while story_range < 6:
                playable_story_choice.append(range)
        if self.options.last_chapter == 2:
            story_range = 7
            while story_range < 9:
                playable_story_choice.append(range)

        #Get the list of latest chapter stories to use in the world
        self.random.shuffle(playable_story_choice)
        self.playable_stories = playable_story_choice[0:
                                                      self.options.story_count.value]

        #If a story from a later chapter is in the multiworld, it needs its requisite story(ies) from the previous chapter
        starting_story_pool = self.playable_stories[1]
        if 7 in self.playable_stories:
            self.playable_stories += 1
            self.playable_stories += 2
        if 8 in self.playable_stories:
            self.playable_stories += 3
            self.playable_stories += 5

        #Get the Glades stories
        for story_range in range(1, 7):
            if story_range in self.playable_stories:
                starting_story_pool.append(story_range)

        #Randomize the starting story, it must be Glades for the natural progression to work
        story = self.random.choice(starting_story_pool)
        self.starting_story = story

        character_table: Dict[str, ItemData] = {}
        for item in item_table:
            if is_character(item) and (item in self.playable_stories):
                character_table[item] = item_table[item]

        character_table = Dict(character_table.items())
        character = self.random.choice(character_table)
        character_name = character[0]
        character_data = character[1]
        precollect = self.create_item(character_name)
        self.multiworld.push_precollected(precollect)
