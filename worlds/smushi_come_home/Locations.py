from typing import NamedTuple, Optional
from BaseClasses import Location


class SmushiLocation(Location):
    game = "Smushi Come Home"


class SmushiLocationData(NamedTuple):
    region: str
    address: int


garden_of_spring_locations = {
    # Mycena Entry
    "Map Pickup (Garden of Spring)": SmushiLocationData("Garden of Spring", 1),
    "Mycology Journal": SmushiLocationData("Garden of Spring", 2),
    "Tool of Writing": SmushiLocationData("Garden of Spring", 3),
    "Yellow Flower Shrine": SmushiLocationData("Garden pf Spring", 4),
    "Restore all Flower Shrines": SmushiLocationData("Garden of Spring", 5),
    "Placeholder for the onion guy": SmushiLocationData("Garden of Spring", 6),

    # Anemone Woods
    "Blue Flower Shrine": SmushiLocationData("Garden of Spring", 7),
    "Band of Elasticity": SmushiLocationData("Garden of Spring", 8),
    "Strawberry Shooting Minigame": SmushiLocationData("Garden of Spring", 9),
    "Forest Wisp in Bird Fountain": SmushiLocationData("Garden of Spring", 10),

    # Crystal Caves
    "Blueberry from Crystal Caves": SmushiLocationData("Garden of Spring", 11),

    # Bolete Beach
    "Blade of Power": SmushiLocationData("Garden of Spring", 12),
    "Pink Flower Shrine": SmushiLocationData("Garden of Spring", 13),

    # Myrtle Pools
    "Ancient Relic 1": SmushiLocationData("Garden of Spring", 14),
    "Ancient Relic 2": SmushiLocationData("Garden of Spring", 15),
    "Return the Ancient Relics": SmushiLocationData("Garden of Spring", 16),
    "Blueberry from Chillin": SmushiLocationData("Garden of Spring", 17),
    "Forest Wisp on Stump": SmushiLocationData("Garden of Spring", 18),
}

journal_checks = {

}

crystal_sanity_checks = {
    
}
