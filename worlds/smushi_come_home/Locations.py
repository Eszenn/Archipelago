from typing import NamedTuple, Optional, Callable
from BaseClasses import Location, CollectionState


class SmushiLocation(Location):
    game = "Smushi Come Home"


class SmushiLocationData(NamedTuple):
    region: str
    address: int


garden_of_spring_locations = {
    # Mycena Entry
    "Garden of Spring Map": SmushiLocationData("Garden of Spring", 1),
    "Mycology Journal": SmushiLocationData("Garden of Spring", 2),
    "Tool of Writing": SmushiLocationData("Garden of Spring", 3),
    "Yellow Flower Shrine": SmushiLocationData("Garden pf Spring", 4),
    "Orange Flower Shrine": SmushiLocationData("Garden of Spring", 5),
    "Restore all Flower Shrines": SmushiLocationData("Garden of Spring", 6),
    "SHO Augmenter": SmushiLocationData("Garden of Spring", 7),

    # Anemone Woods
    "Blue Flower Shrine": SmushiLocationData("Garden of Spring", 8),
    "Band of Elasticity": SmushiLocationData("Garden of Spring", 9),
    "Strawberry Shooting Minigame Reward": SmushiLocationData("Garden of Spring", 10),
    "Forest Wisp in Bird Fountain": SmushiLocationData("Garden of Spring", 11),

    # Crystal Caves
    "Blueberry from Crystal Caves": SmushiLocationData("Garden of Spring", 12),

    # Bolete Beach
    "Blade of Power": SmushiLocationData("Garden of Spring", 13),
    "Pink Flower Shrine": SmushiLocationData("Garden of Spring", 14),

    # Myrtle Pools
    "Ancient Relic 1": SmushiLocationData("Garden of Spring", 15),
    "Ancient Relic 2": SmushiLocationData("Garden of Spring", 16),
    "Return the Ancient Relics": SmushiLocationData("Garden of Spring", 17),
    "Blueberry from Chillin": SmushiLocationData("Garden of Spring", 18),
    "Forest Wisp on Stump": SmushiLocationData("Garden of Spring", 19),
}

forest_of_fall_locations = {
    # Waxcap Falls
    "Forest of Fall Map": SmushiLocationData("Forest of Fall", 20),
    "Sturdy Hooks": SmushiLocationData("Forest of Fall", 21),
    "Nectar Minigame Reward 1": SmushiLocationData("Forest of Fall", 22),
    "Nectar Minigame Reward 2": SmushiLocationData("Forest of Fall", 23),
    "Sparkle Augmenter": SmushiLocationData("Forest of Fall", 24),

    # Restless Stream
    "Forest Wisp on Green Vase": SmushiLocationData("Forest of Fall", 25),
    "Acorn Hole": SmushiLocationData("Forest of Fall", 26),

    # Cryptic Caverns
    "Container of Light": SmushiLocationData("Forest of Fall", 27),
    "Headlamp": SmushiLocationData("Forest of Fall", 28),
    "Rescue the Green Lover": SmushiLocationData("Forest of Fall", 29),
    "Rescue the Purple Lover": SmushiLocationData("Forest of Fall", 30),
    "Cryptic Caverns Explosive Powder": SmushiLocationData("Forest of Fall", 31),
    "Clubhouse Explosive Powder": SmushiLocationData("Forest of Fall", 32),

    # Maple Sanctuary
    "Fire Starter Kit": SmushiLocationData("Forest of Fall", 33),
    "Light the Incense in Maple Sanctuary": SmushiLocationData("Forest of Fall", 34),
    "Gliding Minigame Reward": SmushiLocationData("Forest of Fall", 35),
    "Obstacle Course Reward 1": SmushiLocationData("Forest of Fall", 36),
    "Obstacle Course Reward 2": SmushiLocationData("Forest of Fall", 37),
    "Forest Wisp in Garden Shed": SmushiLocationData("Forest of Fall", 38),
}

lake_of_bloom_locations = {
    # Twin Beach
    "Lake of Bloom Map": SmushiLocationData("Lake of Bloom", 39),

    # Divers Locus
    "Essence of Water": SmushiLocationData("Lake of Bloom", 40),
    "Diving Minigame Reward": SmushiLocationData("Lake of Bloom", 41),

    # Hidden Lotus
    "Old String from Gourmand": SmushiLocationData("Lake of Bloom", 42),

    # Indigo Island
    "Cococo's Shop Item 1": SmushiLocationData("Lake of Bloom", 43),
    "Cococo's Shop Item 2": SmushiLocationData("Lake of Bloom", 44),
    "Secret Opener": SmushiLocationData("Lake of Bloom", 45),

    # Sacred Holm
    "Sacred Orb": SmushiLocationData("Lake of Bloom", 46),
}

journal_checks = {

}

crystal_sanity_checks = {
    
}

location_data_table = {
    **garden_of_spring_locations,
    **forest_of_fall_locations,
    **lake_of_bloom_locations,
    **journal_checks,
    **crystal_sanity_checks
}
