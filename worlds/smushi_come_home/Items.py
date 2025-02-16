from typing import Optional, NamedTuple
from BaseClasses import Item, ItemClassification


class SmushiItem(Item):
    game = "Smushi Come Home"


class SmushiItemData(NamedTuple):
    code: int
    classification: Optional[ItemClassification] = ItemClassification.filler
    amount: Optional[int] = 1


equipment = {
    "Leaf": SmushiItemData(1, ItemClassification.progression),
    "Progressive Hooks": SmushiItemData(2, ItemClassification.progression, 2),
    "Tool of Mining": SmushiItemData(3, ItemClassification.progression),
    "Mycology Journal": SmushiItemData(4, ItemClassification.useful),
    "Blade of Power": SmushiItemData(5, ItemClassification.progression),
    "Fire Starter Kit": SmushiItemData(6, ItemClassification.progression),
    "Headlamp": SmushiItemData(7, ItemClassification.progression),
    "Essence of Water": SmushiItemData(8, ItemClassification.progression),
    "Magic Conch": SmushiItemData(9, ItemClassification.progression),
    "Tool of Smashing": SmushiItemData(10, ItemClassification.progression)
}

task_items = {
    "Blueberry": SmushiItemData(11, ItemClassification.progression, 2),
    "Explosive Powder": SmushiItemData(12, ItemClassification.progression, 2),
    "Secret Password": SmushiItemData(13, ItemClassification.progression),
    "Tool of Writing": SmushiItemData(14, ItemClassification.progression),
    "Band of Elasticity": SmushiItemData(15, ItemClassification.progression),
    "Ancient Relic": SmushiItemData(16, ItemClassification.progression, 2),
    "Old String": SmushiItemData(17, ItemClassification.progression),
    "Sacred Orb": SmushiItemData(18, ItemClassification.progression),
    "Secret Opener": SmushiItemData(19, ItemClassification.progression),
    "Sacred Streamer": SmushiItemData(20, ItemClassification.progression, 4),
}

upgrades = {
    "Spore of Energy": SmushiItemData(21, ItemClassification.progression, 7),
    "Essence of Wind": SmushiItemData(22, ItemClassification.useful, 5),
    "Super Spore": SmushiItemData(23, ItemClassification.useful),
    "Super Essence": SmushiItemData(24, ItemClassification.useful),
}

augmenters = {
    "Purple Augmenter": SmushiItemData(25),
    "Strawberry Augmenter": SmushiItemData(26),
    "Flower Augmenter": SmushiItemData(27),
    "Secret Augmenter": SmushiItemData(28),
    "Verdant Augmenter": SmushiItemData(29),
    "Pelagic Augmenter": SmushiItemData(30),
    "Honey Augmenter": SmushiItemData(31),
    "Sparkle Augmenter": SmushiItemData(32),
    "Clavaria Augmenter": SmushiItemData(33),
    "Ink Augmenter": SmushiItemData(34),
    "Sharp Augmenter": SmushiItemData(35),
    "Precious Augmenter": SmushiItemData(36),
    "Rainbow Augmenter": SmushiItemData(37),
    "Veiled Augmenter": SmushiItemData(38),
    "Sacred Augmenter": SmushiItemData(39),
}

filler_items = {
    "Green Crystal": SmushiItemData(),
    "Purple Crystal": SmushiItemData()
}
