from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Choice, Range, Visibility, Option, OptionGroup, \
    PerGameCommonOptions
from typing import List, Any, Dict

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in ourascent_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class Last_Chapter(Range):
    """What is the most advanced chapter to include in the multiworld?
    The first chapter is Glades
    The second chapter is Oasis"""
    internal_name = "last_chapter"
    display_name = "Last Chapter"
    range_start = 1
    range_end = 2
    default = 1

class Story_Amount(Range):
    """How many stories in the latest indicated chapter are in the multiworld?
    Maximum for Glades: 6 (5 released)
    Maximum for Oasis: 4 (2 released)"""
    internal_name = "story_count"
    display_name = "Story Amount"
    range_start = 1
    range_end = 5
    default = 1

#class Goal(Range):
#    """How many stories must be completed in order to goal
#    Two and beyond is currently unimplemented."""
#    internal_name = "goal_count"
#    display_name = "Goal Amount"
#    range_start = 1
#    range_end = 5
#    default = 1

@dataclass
class OurAscentOptions(PerGameCommonOptions):
    last_chapter: Last_Chapter
    story_count: Story_Amount
#    goal_count: Goal

ourascent_groups: Dict[str, List[Any]] = {
    "Generic Options": [Last_Chapter, Story_Amount]
}