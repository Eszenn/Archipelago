from typing import List, Mapping, Any, Dict

from worlds.AutoWorld import World, WebWorld
from BaseClasses import MultiWorld, Tutorial, ItemClassification, Region

from .Items import SmushiItem, filler_items, crystal_rocks, item_data_table
from .Locations import SmushiLocation, location_data_table
from .Options import SmushiOptions
from .Rules import set_common_rules


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
    web = SmushiWebWorld()
    options = SmushiOptions
    options_dataclass = SmushiOptions

    item_name_to_id = {name: data.code for name, data in item_data_table.items()}
    location_name_to_id = {name: data.address for name, data in location_data_table.items()}

    def generate_early(self) -> None:
        pass

    def create_regions(self) -> None:
        from .Regions import region_data_table
        excluded_regions = []

        # if self.options.goal == 0:
        #    excluded_regions += "Grove of Life"

        for region_name in region_data_table.keys():
            # if region_name in excluded_regions:
            #     continue

            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in region_data_table.items():
            if region_name in excluded_regions:
                continue

            region = self.get_region(region_name)
            for region_exit in region_data.exits:
                if region_exit in excluded_regions:
                    continue
                connecting_region = self.get_region(region_exit)
                region.connect(connecting_region)

            region.add_locations({location_name: self.location_name_to_id[location_name]
                                  for location_name, location_data in location_data_table.items()
                                  if location_data.region == region_name}, SmushiLocation)

        # if self.options.goal.value == 0:
        #     goal_region = self.get_region("Lake of Bloom")
        # else:
        #     goal_region = self.get_region("Grove of Life")

        goal_region = self.get_region("Lake of Bloom")

        goal_location = SmushiLocation(self.player, "Return Home", None, goal_region)
        goal_location.place_locked_item(SmushiItem("Victory", ItemClassification.progression, None, self.player))
        goal_location.access_rule = lambda state: (((state.has("Rusty Hooks", self.player) and state.has("Leaf", self.player))
                                                    or state.has("Tools of the Explorer", self.player))
                                                   and state.has_all(["Sturdy Hooks", "Fire Starter Kit",
                                                                      "Old String", "Sacred Orb"], self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        goal_region.locations.append(goal_location)

    def create_item(self, name: str) -> "SmushiItem":
        data = item_data_table[name]
        return SmushiItem(name, data.classification, data.code, self.player)

    def create_items(self) -> None:
        excluded_items = []
        smushi_item_pool = []

        for name in filler_items.keys():
            excluded_items.append(name)

        if self.options.split_tools.value:
            excluded_items += ["Tools of the Explorer"]

        else:
            excluded_items += ["Leaf", "Rusty Hooks"]

        for name, data in item_data_table.items():
            if name not in excluded_items:
                for i in range(data.amount):
                    item = self.create_item(name)
                    smushi_item_pool.append(item)

        self.multiworld.itempool += smushi_item_pool

    def set_rules(self) -> None:
        set_common_rules(self, self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        pass
