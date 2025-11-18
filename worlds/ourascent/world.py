from collections.abc import Mapping
from typing import Any, List, Set, Dict

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World
from . import items, locations, options, regions, rules, web_world
from .items import item_table, ItemData, is_character
from .locations import get_location_name_to_id
from .options import OurAscentOptions
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

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        pool = self.get_all_items()
        self.multiworld.itempool += pool

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return Item(name, data.classification, data.code, self.player)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict()

    def get_all_items(self, excluded_items: Set[str]) -> List[Item]:
        pool: List[Item] = []
        amount: int = int(0)
        for name, data in item_table.items():
            for _ in range(amount):
                item = self.set_classifications(name)
                pool.append(item)
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

        #Get the Glades chapters
        story_range = 1
        while story_range < 7:
            if story_range in self.playable_stories:
                starting_story_pool.append(story_range)

        #Randomize the starting chapter, it must be Glades for the natural progression to work
        story = self.random.choice(starting_story_pool)
        self.starting_story = story

        character_table: Dict[str, ItemData] = {}
        for item in item_table:
            if is_character(item) and (item in self.playable_stories):
                character_table[item] = item_table[item]

        character_table = list(character_table.items())
        character = self.random.choice(character_table)
        character_name = character[0]
        character_data = character[1]
        precollect = self.create_item(character_name)
        self.multiworld.push_precollected(precollect)
