from typing import Optional, List, NamedTuple


class SmushiRegionData(NamedTuple):
    exits: Optional[List[str]] = None


region_data_table = {
    "Menu": SmushiRegionData(["Garden of Spring"]),
    "Garden of Spring": SmushiRegionData(["Menu", "Forest of Fall"]),
    "Forest of Fall": SmushiRegionData(["Garden of Spring", "Lake of Bloom"]),
    "Lake of Bloom": SmushiRegionData(["Forest of Fall"]),  # add exit to Grove of Life when that's implemented
    # "Grove of Life": SmushiRegionData(["Lake of Bloom"])
}
