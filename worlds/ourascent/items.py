from typing import NamedTuple, Tuple, Dict, Optional
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
    "Equipment - Stan Progressive Sword": ItemData("EQUIPMENT", 7 + equipment_offset, ItemClassification.progression, 0, 10),
    "Equipment - Stan Progressive Snack": ItemData("EQUIPMENT", 8 + equipment_offset, ItemClassification.progression, 0, 7),
    "Equipment - Stan Progressive Shirt": ItemData("EQUIPMENT", 9 + equipment_offset, ItemClassification.progression, 0, 9),
    "Equipment - Stan Progressive Gloves": ItemData("EQUIPMENT", 10 + equipment_offset, ItemClassification.progression, 0, 9),
    "Equipment - Stan Progressive Belt": ItemData("EQUIPMENT", 11 + equipment_offset, ItemClassification.progression, 0, 9),
    "Equipment - Stan Progressive Pants": ItemData("EQUIPMENT", 12 + equipment_offset, ItemClassification.progression, 0, 9),
    "Equipment - Hina Progressive Right Weapon": ItemData("EQUIPMENT", 13 + equipment_offset, ItemClassification.progression, 0, 0, 10),
    "Equipment - Hina Progressive Snack": ItemData("EQUIPMENT", 14 + equipment_offset, ItemClassification.progression, 0, 0, 7),
    "Equipment - Hina Progressive Helmet": ItemData("EQUIPMENT", 15 + equipment_offset, ItemClassification.progression, 0, 0, 9),
    "Equipment - Hina Progressive Shirt": ItemData("EQUIPMENT", 16 + equipment_offset, ItemClassification.progression, 0, 0, 9),
    "Equipment - Hina Progressive Cloak": ItemData("EQUIPMENT", 17 + equipment_offset, ItemClassification.progression, 0, 0, 9),
    "Equipment - Hina Progressive Left Weapon": ItemData("EQUIPMENT", 18 + equipment_offset,ItemClassification.progression, 0, 0, 9),
    "Equipment - Lan Progressive Bow": ItemData("EQUIPMENT", 19 + equipment_offset, ItemClassification.progression, 0, 0, 0, 9),
    "Equipment - Lan Progressive Arrow": ItemData("EQUIPMENT", 20 + equipment_offset, ItemClassification.progression, 0, 0, 0, 9),
    "Equipment - Lan Progressive Hat": ItemData("EQUIPMENT", 21 + equipment_offset, ItemClassification.progression, 0, 0, 0, 9),
    "Equipment - Lan Progressive Belt": ItemData("EQUIPMENT", 22 + equipment_offset, ItemClassification.progression, 0, 0, 0, 10),
    "Equipment - Lan Progressive Cloak": ItemData("EQUIPMENT", 23 + equipment_offset, ItemClassification.progression, 0, 0, 0, 10),
    "Equipment - Lan Progressive Pants": ItemData("EQUIPMENT", 24 + equipment_offset, ItemClassification.progression, 0, 0, 0, 9),
    "Equipment - Sibyl Progressive Accessory": ItemData("EQUIPMENT", 25 + equipment_offset, ItemClassification.progression, 0, 0, 0, 0, 10),
    "Equipment - Sibyl Progressive Left Weapon": ItemData("EQUIPMENT", 26 + equipment_offset, ItemClassification.progression, 0, 0, 0, 0, 13),
    "Equipment - Sibyl Progressive Right Weapon": ItemData("EQUIPMENT", 27 + equipment_offset, ItemClassification.progression, 0, 0, 0, 0, 13),
    "Equipment - Sibyl Progressive Pouch": ItemData("EQUIPMENT", 28 + equipment_offset, ItemClassification.progression, 0, 0, 0, 0, 7),
    "Equipment - Sibyl Progressive Gloves": ItemData("EQUIPMENT", 29 + equipment_offset, ItemClassification.progression, 0, 0, 0, 0, 9),
    "Equipment - Sibyl Progressive Boots": ItemData("EQUIPMENT", 30 + equipment_offset, ItemClassification.progression, 0, 0, 0, 0, 9),

    #Glades
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
    "Accessory - Stan Tooth Amulet": ItemData("EQUIPMENT", 11 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Slim Band": ItemData("EQUIPMENT", 12 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Power Ring": ItemData("EQUIPMENT", 13 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Engraved Ring": ItemData("EQUIPMENT", 14 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Dagger Amulet": ItemData("EQUIPMENT", 15 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Empty Ring": ItemData("EQUIPMENT", 16 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Crown Ring": ItemData("EQUIPMENT", 17 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Double Band": ItemData("EQUIPMENT", 18 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Studded Band": ItemData("EQUIPMENT", 19 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Stan Jeweled Ring": ItemData("EQUIPMENT", 20 + accessory_offset, ItemClassification.useful, 0, 3),
    "Accessory - Hina Tooth Amulet": ItemData("EQUIPMENT", 21 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Dull Ring": ItemData("EQUIPMENT", 22 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Masked Amulet": ItemData("EQUIPMENT", 23 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Engraved Ring": ItemData("EQUIPMENT", 24 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Dagger Amulet": ItemData("EQUIPMENT", 25 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Blood Ring": ItemData("EQUIPMENT", 26 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Coin Amulet": ItemData("EQUIPMENT", 27 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Death Ring II": ItemData("EQUIPMENT", 28 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Studded Band": ItemData("EQUIPMENT", 29 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Hina Twilight Ring": ItemData("EQUIPMENT", 30 + accessory_offset, ItemClassification.useful, 0, 0, 3),
    "Accessory - Lan Chipped Earring": ItemData("EQUIPMENT", 31 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Slim Band": ItemData("EQUIPMENT", 32 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Creepy Amulet": ItemData("EQUIPMENT", 33 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Shield Amulet": ItemData("EQUIPMENT", 34 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Slim Double Band": ItemData("EQUIPMENT", 35 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Fancy Ring": ItemData("EQUIPMENT", 36 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Defeated Earring": ItemData("EQUIPMENT", 37 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Double Band": ItemData("EQUIPMENT", 38 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Death Ring II": ItemData("EQUIPMENT", 39 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Lan Enchanted Earring": ItemData("EQUIPMENT", 40 + accessory_offset, ItemClassification.useful, 0, 0, 0, 3),
    "Accessory - Sibyl Dull Ring": ItemData("EQUIPMENT", 41 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Masked Amulet": ItemData("EQUIPMENT", 42 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Power Ring": ItemData("EQUIPMENT", 43 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Creepy Amulet": ItemData("EQUIPMENT", 44 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Engraved Ring": ItemData("EQUIPMENT", 45 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Slim Double Band": ItemData("EQUIPMENT", 46 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Fancy Ring": ItemData("EQUIPMENT", 47 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Defeated Earring": ItemData("EQUIPMENT", 48 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Studded Band": ItemData("EQUIPMENT", 49 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Accessory - Sibyl Twilight Amulet": ItemData("EQUIPMENT", 50 + accessory_offset, ItemClassification.useful, 0, 0, 0, 0, 3),

    #Glades
    "Augment - Apolonia Weapon Mastery": ItemData("AUGMENT", 1 + augment_offset, ItemClassification.useful, 5),
    "Augment - Apolonia Magical Imbuement": ItemData("AUGMENT", 2 + augment_offset, ItemClassification.useful, 4),
    "Augment - Apolonia Mobility": ItemData("AUGMENT", 3 + augment_offset, ItemClassification.useful, 6),
    "Augment - Apolonia Holy Power": ItemData("AUGMENT", 4 + augment_offset, ItemClassification.useful, 3),
    "Augment - Stan Vitality Boost": ItemData("AUGMENT", 5 + augment_offset, ItemClassification.useful, 0, 3),
    "Augment - Stan Amplified Strength": ItemData("AUGMENT", 6 + augment_offset, ItemClassification.useful, 0, 3),
    "Augment - Stan Swift Steps": ItemData("AUGMENT", 7 + augment_offset, ItemClassification.useful, 0, 3),
    "Augment - Stan Defiant Guard": ItemData("AUGMENT", 8 + augment_offset, ItemClassification.useful, 0, 3),
	"Augment - Stan Fierce Onslaught": ItemData("AUGMENT", 9 + augment_offset, ItemClassification.useful, 0, 5),
    "Augment - Hina Mighty Monkey": ItemData("AUGMENT", 10 + augment_offset, ItemClassification.useful, 0, 0, 5),
    "Augment - Hina Sinister Serpent": ItemData("AUGMENT", 11 + augment_offset, ItemClassification.useful, 0, 0, 5),
    "Augment - Hina Tenacious Tiger": ItemData("AUGMENT", 12 + augment_offset, ItemClassification.useful, 0, 0, 5),
    "Augment - Hina Patient Panda": ItemData("AUGMENT", 13 + augment_offset, ItemClassification.useful, 0, 0, 5),
	"Augment - Hina Punch Training": ItemData("AUGMENT", 14 + augment_offset, ItemClassification.useful, 0, 0, 3),
	"Augment - Hina Form Training": ItemData("AUGMENT", 15 + augment_offset, ItemClassification.useful, 0, 0, 3),
	"Augment - Hina Speed Training": ItemData("AUGMENT", 16 + augment_offset, ItemClassification.useful, 0, 0, 3),
	"Augment - Hina Kick Training": ItemData("AUGMENT", 17 + augment_offset, ItemClassification.useful, 0, 0, 3),
    "Augment - Lan Lucky Shots": ItemData("AUGMENT", 18 + augment_offset, ItemClassification.useful, 0, 0, 0, 5),
    "Augment - Lan Relentless Fire": ItemData("AUGMENT", 19 + augment_offset, ItemClassification.useful, 0, 0, 0, 4),
    "Augment - Lan Hunter's Insight": ItemData("AUGMENT", 20 + augment_offset, ItemClassification.useful, 0, 0, 0, 2),
    "Augment - Lan Bloodthirsty Quiver": ItemData("AUGMENT", 21 + augment_offset, ItemClassification.useful, 0, 0, 0, 3),
	"Augment - Lan Killer Instinct": ItemData("AUGMENT", 22 + augment_offset, ItemClassification.useful, 0, 0, 0, 1),
    "Augment - Sibyl Silent Steps": ItemData("AUGMENT", 23 + augment_offset, ItemClassification.useful, 0, 0, 0, 0, 6),
    "Augment - Sibyl Dual Depredation": ItemData("AUGMENT", 24 + augment_offset, ItemClassification.useful, 0, 0, 0, 0, 4),
    "Augment - Sibyl Grounded Motion": ItemData("AUGMENT", 25 + augment_offset, ItemClassification.useful, 0, 0, 0, 0, 3),
    "Augment - Sibyl Stunning Distraction": ItemData("AUGMENT", 26 + augment_offset, ItemClassification.useful, 0, 0, 0, 0, 2),
	"Augment - Sibyl Ruinous Bleed": ItemData("AUGMENT", 27 + augment_offset, ItemClassification.useful, 0, 0, 0, 0, 7),

    #Glades
    "Story Completion - 1-1": ItemData("COMPLETION", None, ItemClassification.progression, 1),
    "Story Completion - 1-2": ItemData("COMPLETION", None, ItemClassification.progression, 0, 1),
    "Story Completion - 1-3": ItemData("COMPLETION", None, ItemClassification.progression, 0, 0, 1),
    "Story Completion - 1-4": ItemData("COMPLETION", None, ItemClassification.progression, 0, 0, 0, 1),
    "Story Completion - 1-5": ItemData("COMPLETION", None, ItemClassification.progression, 0, 0, 0, 0, 1)
}

item_name_to_id = {item: item_table[item].code for item in item_table}

filler_items: Tuple[str, ...] = (
    "Apolonia +1 Hesitation",
    "Stan +1 IQ",
    "Hina +1 Spirit",
    "Lan +1 Optimism",
    "Sibyl +1 Paranoia"
)