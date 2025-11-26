from typing import Any, List, Dict

from BaseClasses import Item, MultiWorld, ItemClassification, CollectionState
from worlds.AutoWorld import World
from . import options, rules, web_world
from .constants.completions import *
from .constants.story_data import *
from .items import OurAscentItem, item_table, ItemData, equipment_offset, accessory_offset, filler_items
from .locations import EventId, get_location_name_to_id, get_main_menu_locations, get_11_locations, get_12_locations, get_13_locations, get_14_locations, get_15_locations
from .regions import create_all_regions
from .rules import OurAscentLogic
from .stories import *

class OurAscentWorld(World):
    """Our Ascent is an incremental roguelite RPG with many layers of metaprogression."""
    game = "Our Ascent"
    web = web_world.OurAscentWebWorld()

    options_dataclass = options.OurAscentOptions
    options: options.OurAscentOptions

    item_name_to_id = {item: data.code for item, data in item_table.items()}
    location_name_to_id = get_location_name_to_id()
    playable_stories = []
    starting_story = "1-1: Falling Into Chaos"
    completions = {}
    excluded_items: Dict[str, ItemData] = {}

    origin_region_name = "Story Select"

    #def pre_fill(self):
    #    from BaseClasses import CollectionState
    #    from Fill import sweep_from_pool
    #    state = sweep_from_pool(CollectionState(self.multiworld), self.multiworld.itempool)
    #    unreachable_locations = [location for location in self.get_locations() if not location.can_reach(state)]
    #    assert not unreachable_locations, f"All state can't reach all locations: {unreachable_locations}"

    def pre_fill(self) -> None:
        unreachable_locations = []
        all_state = self.multiworld.get_all_state(False)
        for location in self.multiworld.get_locations(self.player):
            if not location.can_reach(all_state):
                unreachable_locations.append(location)
        if unreachable_locations:
            raise Exception(f"The following locations can't be reached even with every progression item.\n\n{unreachable_locations}\n\n{all_state.prog_items[self.player]}")

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_regions(self) -> None:

        locationss = get_11_locations(self.player)
        locationss.extend(get_12_locations(self.player))
        locationss.extend(get_13_locations(self.player))
        locationss.extend(get_14_locations(self.player))
        locationss.extend(get_15_locations(self.player))
        create_all_regions(self, locationss, self.options)

    def set_rules(self) -> None:
        required_completions = [value for key, value in completion_index.items() if key in self.playable_stories]
        print("Required Completions:", required_completions)
        self.multiworld.completion_condition[self.player] = lambda state: state.has_all(required_completions, self.player)

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
        amount:int = int(0)
        for name, data in item_table.items():
            #if name not in self.excluded_items:
                if "1-1: Falling Into Chaos" in self.playable_stories:
                    amount = data.story11
                    for _ in range(amount):
                        item = self.create_item(name)
                        pool.append(item)
                if "1-2: Rising To The Challenge" in self.playable_stories:
                    amount = data.story12
                    for _ in range(amount):
                        item = self.create_item(name)
                        pool.append(item)
                if "1-3: Unleashing The Beast" in self.playable_stories:
                    amount = data.story13
                    for _ in range(amount):
                        item = self.create_item(name)
                        pool.append(item)
                if "1-4: Hunting For Truth" in self.playable_stories:
                    amount = data.story14
                    for _ in range(amount):
                        item = self.create_item(name)
                        pool.append(item)
                if "1-5: Lurking In The Shadows" in self.playable_stories:
                    amount = data.story15
                    for _ in range(amount):
                        item = self.create_item(name)
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
        print(starting_story)
        #self.excluded_items[playable_character_to_item[starting_story]] = item_table[playable_character_to_item[starting_story]]
        self.multiworld.push_precollected(self.create_item(playable_character_to_item[starting_story]))

    def create_and_assign_event_items(self) -> None:
        for location in self.multiworld.get_locations(self.player):
            if location.address == EventId:
                item = Item(location.name, ItemClassification.progression, EventId, self.player)
                location.place_locked_item(item)

    def completion_rule(self, state: CollectionState):
        if self.options.last_chapter.value == 1:
            if "1-1: Falling Into Chaos" in self.playable_stories:
                if not state.has("Story 1-1 Completion", self.player):
                    return False
            if "1-2: Rising To The Challenge" in self.playable_stories:
                if not state.has("Story 1-2 Completion", self.player):
                    return False
            if "1-3: Unleashing The Beast" in self.playable_stories:
                if not state.has("Story 1-3 Completion", self.player):
                    return False
            if "1-4: Hunting For Truth" in self.playable_stories:
                if not state.has("Story 1-4 Completion", self.player):
                    return False
            if "1-5: Lurking In The Shadows" in self.playable_stories:
                if not state.has("Story 1-5 Completion", self.player):
                    return False
        return True

    def set_classifications(self, name: str) -> Item:
        data = item_table[name]
        item = Item(name, data.classification, data.code, self.player)

        return item