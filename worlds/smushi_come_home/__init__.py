from typing import List, Mapping, Any, Dict

from worlds.AutoWorld import World, WebWorld
from BaseClasses import MultiWorld, Tutorial, ItemClassification, Region

from .Items import SmushiItem, item_data_table
from .Options import SmushiOptions


class SmushiWebWorld(WebWorld):
    theme = "grassFlowers"

    setup_en = Tutorial(
        tutorial_name="Setup Guide",
        description="A guide to setting up Smushi Come Home",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["Eszenn"]
    )
    tutorials = [setup_en]


class SmushiWorld(World):
    """Smushi description goes here"""

    game = "Smushi Come Home"
    web = SmushiWebWorld
    options = SmushiOptions
    options_dataclass = SmushiOptions

    item_name_to_id = {name: data.code for name, data in item_data_table.items()}
    # location_name_to_id = {name: data.address for name, data in location_data_table.items()}

    def generate_early(self) -> None:
        pass

    def create_regions(self) -> None:
        pass

    def create_item(self, name: str) -> "SmushiItem":
        data = item_data_table[name]
        return SmushiItem(name, data.classification, data.code, self.player)

    def create_items(self) -> None:
        pass

    def set_rules(self) -> None:
        pass

    def fill_slot_data(self) -> Mapping[str, Any]:
        pass
