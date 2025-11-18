from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class OurAscentWebWorld(WebWorld):
    game = "Our Ascent"
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide for setting up Our Ascent for Archipelago",
        "English",
        "setup_en.md",
        "setup/en",
        ["Azuri Caelum"]
    )

    tutorials = [setup_en]