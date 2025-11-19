from typing import NamedTuple, Tuple, Dict, Optional, List
from BaseClasses import ItemClassification, Item

class ItemData(NamedTuple):
    category: str
    code: Optional[int]
    classification: ItemClassification
    story11: Optional[int] = 0
    story12: Optional[int] = 0
    story13: Optional[int] = 0
    story14: Optional[int] = 0
    story15: Optional[int] = 0
    story16: Optional[int] = 0
    story21: Optional[int] = 0
    story22: Optional[int] = 0

class OurAscentItem(Item):
    game = "Our Ascent"

character_offset = 1
equipment_offset = 11
accessory_offset = 101
augment_offset = 1001
completion_offset = 10001

item_table: Dict[str, ItemData] = {
    "Character - Playable Apolonia": ItemData("CHARACTER", 1 + character_offset, ItemClassification.progression, 1, 0, 0, 0, 0, 0, 1),
    "Character - Playable Stan": ItemData("CHARACTER", 2 + character_offset, ItemClassification.progression, 0, 1, 0, 0, 0, 0, 1),
    "Character - Playable Hina": ItemData("CHARACTER", 3 + character_offset, ItemClassification.progression, 0, 0, 1, 0, 0, 0, 0, 1),
    "Character - Playable Lan": ItemData("CHARACTER", 4 + character_offset, ItemClassification.progression, 0, 0, 0, 1),
    "Character - Playable Sibyl": ItemData("CHARACTER", 5 + character_offset, ItemClassification.progression, 0, 0, 0, 0, 1, 0, 0, 1),

    "Equipment - Apolonia Progressive Sword": ItemData("EQUIPMENT", 1 + equipment_offset, ItemClassification.progression, 10),
    "Equipment - Apolonia Progressive Shield": ItemData("EQUIPMENT", 2 + equipment_offset, ItemClassification.progression, 7),
    "Equipment - Apolonia Progressive Helmet": ItemData("EQUIPMENT", 3 + equipment_offset, ItemClassification.progression, 9),
    "Equipment - Apolonia Progressive Breastplate": ItemData("EQUIPMENT", 4 + equipment_offset, ItemClassification.progression, 9),
    "Equipment - Apolonia Progressive Gloves": ItemData("EQUIPMENT", 5 + equipment_offset, ItemClassification.progression, 9),
    "Equipment - Apolonia Progressive Boots": ItemData("EQUIPMENT", 6 + equipment_offset, ItemClassification.progression, 9),

    "Accessory - Apolonia Dull Ring": ItemData("EQUIPMENT", 1 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Chipped Earring": ItemData("EQUIPMENT", 2 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Death Ring I": ItemData("EQUIPMENT", 3 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Shield Amulet": ItemData("EQUIPMENT", 4 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Slim Double Band": ItemData("EQUIPMENT", 5 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Fancy Ring": ItemData("EQUIPMENT", 6 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Recovery Ring": ItemData("EQUIPMENT", 7 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Coin Amulet": ItemData("EQUIPMENT", 8 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Death Ring II": ItemData("EQUIPMENT", 9 + accessory_offset, ItemClassification.useful, 3),
    "Accessory - Apolonia Enchanted Ring": ItemData("EQUIPMENT", 10 + accessory_offset, ItemClassification.useful, 3),

    "Augment - Apolonia Weapon Mastery": ItemData("AUGMENT", 1 + augment_offset, ItemClassification.useful, 5),
    "Augment - Apolonia Magical Imbuement": ItemData("AUGMENT", 2 + augment_offset, ItemClassification.useful, 4),
    "Augment - Apolonia Mobility": ItemData("AUGMENT", 3 + augment_offset, ItemClassification.useful, 6),
    "Augment - Apolonia Holy Power": ItemData("AUGMENT", 4 + augment_offset, ItemClassification.useful, 3),

    "Story Completion - 1-1": ItemData("COMPLETION", None, ItemClassification.progression, 1)
}

item_name_to_id = {item: item_table[item].code for item in item_table}

def is_character(item_name: str) -> bool:
    item_id = item_name_to_id[item_name]
    return 2 <= item_id <= 6


filler_items: Tuple[str, ...] = (
    "Apolonia +1 Hesitation",
    "Stan +1 IQ",
    "Hina +1 Spirit",
    "Lan +1 Optimism",
    "Sibyl +1 Paranoia"
)