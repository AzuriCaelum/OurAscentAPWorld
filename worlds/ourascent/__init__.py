from typing import Any, List, Dict

from BaseClasses import Item, MultiWorld, ItemClassification, CollectionState
from worlds.AutoWorld import World
from . import options, rules, web_world
from .constants.completions import *
from .constants.story_data import *
from .items import OurAscentItem, item_table, ItemData, equipment_offset, accessory_offset, filler_items
from .locations import EventId, get_location_name_to_id, get_main_menu_locations, get_11_locations, get_12_locations, get_13_locations, get_14_locations, get_15_locations
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
    playable_stories = []
    starting_story = "1-1: Falling Into Chaos"
    completions = {}

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

        locationss = get_main_menu_locations(self.player)
        locationss.extend(get_11_locations(self.player))
        locationss.extend(get_12_locations(self.player))
        locationss.extend(get_13_locations(self.player))
        locationss.extend(get_14_locations(self.player))
        locationss.extend(get_15_locations(self.player))
        create_all_regions(self, locationss, self.options)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: self.completion_rule(state)

    def create_items(self) -> None:
        self.create_and_assign_event_items()
        pool = self.get_all_items()
        self.multiworld.itempool += pool

    def create_item(self, name: str) -> OurAscentItem:
        data = item_table[name]
        return OurAscentItem(name, data.classification, data.code, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "playable stories": self.playable_stories,
            "starting story": self.starting_story
        }

    def get_all_items(self) -> List[Item]:
        pool: List[Item] = []
        amount: int = int(0)
        for name, data in item_table.items():
            if "1-1: Falling Into Chaos" in self.playable_stories:
                amount = amount + int(data.story11 or 0)
            if "1-2: Rising To The Challenge" in self.playable_stories:
                amount = amount + int(data.story12 or 0)
            if "1-3: Unleashing The Beast" in self.playable_stories:
                amount = amount + int(data.story13 or 0)
            if "1-4: Hunting For Truth" in self.playable_stories:
                amount = amount + int(data.story14 or 0)
            if "1-5: Lurking In The Shadows" in self.playable_stories:
                amount = amount + int(data.story15 or 0)
            for _ in range(amount):
                item = self.set_classifications(name)
                pool.append(item)
        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)):
            item = self.create_item(self.get_filler_item_name())
            pool.append(item)
        return pool

    def generate_early(self):
        self.get_stories()

    def get_all_stories(self, story_list: List[int]) -> List[int]:
        final_story_list = []
        for story in story_list:
            final_story_list += previous_stories[story]
        return final_story_list


    def get_stories(self):
        storied = self.random.sample(stories_per_chapter[self.options.last_chapter.value], self.options.story_count.value)
        story_list = self.get_all_stories(storied)
        story_list = list(set(story_list))
        print(story_list)
        self.playable_stories = [value for key, value in story_id_to_name.items() if key in story_list]
        stories_from_first_chapter = [story for story in story_list if story_to_chapter[story] == 1]
        starting_story = self.random.choice(stories_from_first_chapter)
        self.multiworld.push_precollected(self.create_item(playable_character_to_item[starting_story]))

    def create_and_assign_event_items(self) -> None:
        for location in self.multiworld.get_locations(self.player):
            if location.address == EventId:
                item = Item(location.name, ItemClassification.progression, EventId, self.player)
                location.place_locked_item(item)

    def completion_rule(self, state: CollectionState):
        completions = completion_index
        for completion in completions:
            if completion not in self.location_name_to_id:
                continue
            if not state.has(completion, self.player):
                return False
        return True

    def set_classifications(self, name: str) -> Item:
        data = item_table[name]
        item = Item(name, data.classification, data.code, self.player)

        return item