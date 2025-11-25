characters_per_story = {
    1: ["Apolonia"], #Glades
    2: ["Stan"],
    3: ["Hina"],
    4: ["Lan"],
    5: ["Sibyl"],

    7: ["Apolonia", "Stan"], #Oasis
    8: ["Hina", "Sibyl"]
}

stories_per_chapter = {
    1: [1, 2, 3, 4, 5],
    2: [7, 8],
}

story_to_chapter = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    7: 2,
    8: 2,
}

previous_stories = {
    1: [1],
    2: [2],
    3: [3],
    4: [4],
    5: [5],

    7: [7, 2, 1],
    8: [8, 5, 3]
}

playable_character_to_item = {
    1: "Character - Playable Apolonia",
    2: "Character - Playable Stan",
    3: "Character - Playable Hina",
    4: "Character - Playable Lan",
    5: "Character - Playable Sibyl"
}

first_chapter_stories = {
    1: "1-1: Falling Into Chaos",
    2: "1-2: Rising To The Challenge",
    3: "1-3: Unleashing The Beast",
    4: "1-4: Hunting For Truth",
    5: "1-5: Lurking In The Shadows"
}

first_chapter_playable_stories = {
    "1-1: Falling Into Chaos": 1,
    "1-2: Rising To The Challenge": 2,
    "1-3: Unleashing The Beast": 3,
    "1-4: Hunting For Truth": 4,
    "1-5: Lurking In The Shadows": 5
}