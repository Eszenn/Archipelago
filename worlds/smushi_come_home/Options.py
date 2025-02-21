from Options import Toggle, DefaultOnToggle, Range, Choice, PerGameCommonOptions
from dataclasses import dataclass

class Goal(Choice):
    """
    When your world should be considered completed.
    Go Home:
    Heart of the Forest: Requires going back home, then returning to restore the Heart of the Forest
    """
    display_name = "Goal"
    option_go_home = 0
    option_heart_of_the_forest = 1
    default = 0


class SplitExplorerTools(Toggle):
    """
    If enabled, the explorer tools will be split into the Leaf and Rusty Hook
    """
    display_name = "Split Explorer Tools"


class CrystalSanity(Toggle):
    """
    If enabled, Green and Purple Crystal Rocks will be added to locations, and the corresponding amount of Green and
    Purple Crystals will be added to the item pool
    """
    display_name = "Crystal Sanity"


class MushroomSanity(Toggle):
    """
    If enabled, mushroom journal entries will be added to locations, and the Mycology Journal will be added to the item
    pool
    """
    display_name = "Mushroom Sanity"


@dataclass
class SmushiOptions(PerGameCommonOptions):
    goal: Goal
    split_tools: SplitExplorerTools
    crystal_sanity: CrystalSanity
    mushroom_sanity: MushroomSanity

