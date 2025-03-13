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
    # "Magic Conch": SmushiItemData(11, ItemClassification.progression),
    # "Tool of Smashing": SmushiItemData(12, ItemClassification.progression)
}

task_items = {
    "Blueberry": SmushiItemData(13, ItemClassification.progression, 2),
    "Explosive Powder": SmushiItemData(14, ItemClassification.progression, 2),
    "Secret Password": SmushiItemData(15, ItemClassification.progression),
    "Tool of Writing": SmushiItemData(16, ItemClassification.progression),
    "Band of Elasticity": SmushiItemData(17, ItemClassification.progression),
    "Ancient Relic": SmushiItemData(18, ItemClassification.progression, 2),
    "Container of Light": SmushiItemData(19, ItemClassification.progression),
    "Old String": SmushiItemData(20, ItemClassification.progression),
    "Sacred Orb": SmushiItemData(21, ItemClassification.progression),
    "Secret Opener": SmushiItemData(22, ItemClassification.progression),
    # "Sacred Streamer": SmushiItemData(23, ItemClassification.progression, 4),
}

upgrades = {
    "Spore of Energy": SmushiItemData(24, ItemClassification.progression, 7),
    "Essence of Wind": SmushiItemData(25, ItemClassification.useful, 5),
    # "Super Spore": SmushiItemData(26, ItemClassification.useful),
    "Super Essence": SmushiItemData(27, ItemClassification.useful),
}

augmenters = {
    "Purple Augmenter": SmushiItemData(28),
    "Strawberry Augmenter": SmushiItemData(29),
    "Flower Augmenter": SmushiItemData(30),
    "Secret Augmenter": SmushiItemData(31),
    "Verdant Augmenter": SmushiItemData(32),
    "Pelagic Augmenter": SmushiItemData(33),
    "Honey Augmenter": SmushiItemData(34),
    "Sparkle Augmenter": SmushiItemData(35),
    "Clavaria Augmenter": SmushiItemData(36),
    "Ink Augmenter": SmushiItemData(37),
    # "Sharp Augmenter": SmushiItemData(38),
    # "Precious Augmenter": SmushiItemData(39),
    # "Rainbow Augmenter": SmushiItemData(40),
    # "Veiled Augmenter": SmushiItemData(41),
    # "Sacred Augmenter": SmushiItemData(42),
}

crystal_rewards = {
    "Green Crystal x20": SmushiItemData(43),
    "Green Crystal x30": SmushiItemData(44),
}

crystal_rocks = {
    "Green Crystal x3": SmushiItemData(45, ),  # Some amount of these
    "Green Crystal x4": SmushiItemData(46, ),  # Some amount of these
    "Green Crystal x6": SmushiItemData(47, ),  # Some amount of these
    "Purple Crystal x4": SmushiItemData(48)
}

filler_items = {
    "Green Crystal": SmushiItemData(49),
    "Purple Crystal": SmushiItemData(50)
}

item_data_table = {
    **equipment,
    **task_items,
    **upgrades,
    **augmenters,
    **crystal_rewards,
    # **crystal_rocks,
    **filler_items
}
