from typing import Optional, NamedTuple
from BaseClasses import Item, ItemClassification


class SmushiItem(Item):
    game = "Smushi Come Home"


class SmushiItemData(NamedTuple):
    code: int
    classification: Optional[ItemClassification] = ItemClassification.filler
    amount: Optional[int] = 1


equipment = {
    "Tools of the Explorer": SmushiItemData(1, ItemClassification.progression),
    "Leaf": SmushiItemData(2, ItemClassification.progression),
    "Rusty Hooks": SmushiItemData(3, ItemClassification.progression),
    "Sturdy Hooks": SmushiItemData(4, ItemClassification.progression),
    "Tool of Mining": SmushiItemData(5, ItemClassification.progression),
    "Mycology Journal": SmushiItemData(6, ItemClassification.useful),
    "Blade of Power": SmushiItemData(7, ItemClassification.progression),
    "Fire Starter Kit": SmushiItemData(8, ItemClassification.progression),
    "Headlamp": SmushiItemData(9, ItemClassification.progression),
    "Essence of Water": SmushiItemData(10, ItemClassification.progression),
    "Magic Conch": SmushiItemData(11, ItemClassification.progression),
    "Tool of Smashing": SmushiItemData(12, ItemClassification.progression)
}

task_items = {
    "Blueberry": SmushiItemData(13, ItemClassification.progression, 2),
    "Explosive Powder": SmushiItemData(14, ItemClassification.progression, 2),
    "Secret Password": SmushiItemData(15, ItemClassification.progression),
    "Tool of Writing": SmushiItemData(16, ItemClassification.progression),
    "Band of Elasticity": SmushiItemData(17, ItemClassification.progression),
    "Ancient Relic": SmushiItemData(18, ItemClassification.progression, 2),
    "Old String": SmushiItemData(19, ItemClassification.progression),
    "Sacred Orb": SmushiItemData(20, ItemClassification.progression),
    "Secret Opener": SmushiItemData(21, ItemClassification.progression),
    "Sacred Streamer": SmushiItemData(22, ItemClassification.progression, 4),
}

upgrades = {
    "Spore of Energy": SmushiItemData(23, ItemClassification.progression, 7),
    "Essence of Wind": SmushiItemData(24, ItemClassification.useful, 5),
    "Super Spore": SmushiItemData(25, ItemClassification.useful),
    "Super Essence": SmushiItemData(26, ItemClassification.useful),
}

augmenters = {
    "Purple Augmenter": SmushiItemData(27),
    "Strawberry Augmenter": SmushiItemData(28),
    "Flower Augmenter": SmushiItemData(29),
    "Secret Augmenter": SmushiItemData(30),
    "Verdant Augmenter": SmushiItemData(31),
    "Pelagic Augmenter": SmushiItemData(32),
    "Honey Augmenter": SmushiItemData(33),
    "Sparkle Augmenter": SmushiItemData(34),
    "Clavaria Augmenter": SmushiItemData(35),
    "Ink Augmenter": SmushiItemData(36),
    "Sharp Augmenter": SmushiItemData(37),
    "Precious Augmenter": SmushiItemData(38),
    "Rainbow Augmenter": SmushiItemData(39),
    "Veiled Augmenter": SmushiItemData(40),
    "Sacred Augmenter": SmushiItemData(41),
}

crystals = {
    "Green Crystal x3": SmushiItemData(42, ),  # Some amount of these
    "Green Crystal x4": SmushiItemData(43, ),  # Some amount of these
    "Green Crystal x6": SmushiItemData(44, ),  # Some amount of these
    "Purple Crystal x4": SmushiItemData(45, )  # Some amount of these
}

filler_items = {
    "Green Crystal": SmushiItemData(),
    "Purple Crystal": SmushiItemData()
}

item_data_table = {
    **equipment,
    **task_items,
    **upgrades,
    **augmenters
}
