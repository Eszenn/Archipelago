from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import SmushiWorld


def set_common_rules(world: "SmushiWorld", player:int):
    # set_rule(world.get_location(""), lambda state: )

    # Entrances
    set_rule(world.get_entrance("Menu -> Garden of Spring"), lambda state: True)
    set_rule(world.get_entrance("Garden of Spring -> Forest of Fall"), lambda state: state.has("Blueberry", player, 2))
    set_rule(world.get_entrance("Forest of Fall -> Lake of Bloom"), lambda state: state.has("Explosive Powder", player, 2)
                                                                                  and state.has("Fire Starter Kit", player))
    # Mycena Entry
    set_rule(world.get_location("Mycology Journal"), lambda state: state.has("Tool of Writing", player))
    set_rule(world.get_location("Orange Flower Shrine"), lambda state: can_climb(player, state) and state.has("Blade of Power", player))
    set_rule(world.get_location("Restore all Flower Shrines"), lambda state: can_climb(player, state) and state.has("Blade of Power", player))
    set_rule(world.get_location("SHO Augmenter"), lambda state: can_climb(player, state) and state.has("Secret Opener", player))

    # Anemone Woods
    set_rule(world.get_location("Blue Flower Shrine"), lambda state: can_climb(player, state))
    set_rule(world.get_location("Strawberry Shooting Minigame Reward"), lambda state: can_climb(player, state) and can_glide(player, state) and state.has("Band of Elasticity", player))
    set_rule(world.get_location("Forest Wisp in Bird Fountain"), lambda state: can_climb(player, state) and can_glide(player, state))

    # Crystal Caves
    set_rule(world.get_location("Blueberry from Crystal Caves"), lambda state: can_climb(player, state) and can_glide(player, state))

    # Bolete Beach
    set_rule(world.get_location("Blade of Power"), lambda state: state.has("Mining Tool", player))
    set_rule(world.get_location("Pink Flower Shrine"), lambda state: can_climb(player, state) and state.has("Blade of Power", player))

    # Myrtle Pools
    set_rule(world.get_location("Ancient Relic 1"), lambda state: can_climb(player, state) and state.has("Mining Tool", player))
    set_rule(world.get_location("Ancient Relic 2"), lambda state: can_climb(player, state) and can_glide(player, state) and state.has("Mining Tool", player))
    set_rule(world.get_location("Return the Ancient Relics"), lambda state: state.has("Ancient Relic", player, 2))
    set_rule(world.get_location("Blueberry from Chillin"), lambda state: state.has("Mining Tool", player))  # Tentative requirement - needs verification
    set_rule(world.get_location("Forest Wisp on Stump"), lambda state: can_climb(player, state) and can_glide(player, state))

    # Waxcap Falls
    set_rule(world.get_location("Sturdy Hooks"), lambda state: can_climb(player, state) and state.has("Mining Tool", player))  # Tentative requirement - needs verification
    set_rule(world.get_location("Sparkle Augmenter"), lambda state: can_double_climb(player, state) and state.has("Essence of Water", player))

    # Restless Stream
    set_rule(world.get_location("Forest Wisp on Green Vase"), lambda state: can_climb(player, state) and can_glide(player, state))
    set_rule(world.get_location("Acorn Hole"), lambda state: can_climb(player, state) and state.has("Blade of Power", player))

    # Cryptic Caverns
    set_rule(world.get_location("Container of Light"), lambda state: can_climb(player, state) and can_glide(player, state))
    set_rule(world.get_location("Headlamp"), lambda state: can_climb(player, state) and state.has("Container of Light", player))
    set_rule(world.get_location("Rescue the Green Lover"), lambda state: can_climb(player, state) and can_glide(player, state) and state.has_all(["Headlamp", "Fire Starter Kit"], player))
    set_rule(world.get_location("Rescue the Purple Lover"), lambda state: can_climb(player, state) and can_glide(player, state) and state.has_all(["Headlamp", "Blade of Power", "Fire Starter Kit"], player))
    set_rule(world.get_location("Cryptic Caverns Explosive Powder"), lambda state: can_climb(player, state) and can_glide(player, state) and state.has("Headlamp", player))
    set_rule(world.get_location("Clubhouse Explosive Powder"), lambda state: can_climb(player, state) and state.has("Secret Password", player))

    # Maple Sanctuary
    set_rule(world.get_location("Fire Starter Kit"), lambda state: can_double_climb(player, state) and state.has("Mining Tool", player))
    set_rule(world.get_location("Light the Incense in Maple Sanctuary"), lambda state: can_double_climb(player, state) and can_glide(player, state) and state.has("Fire Starter Kit", player))
    set_rule(world.get_location("Forest Wisp in Garden Shed"), lambda state: can_double_climb(player, state) and can_glide(player, state))
    set_rule(world.get_location("Obstacle Course Reward 1"), lambda state: can_double_climb(player, state))
    set_rule(world.get_location("Obstacle Course Reward 2"), lambda state: can_double_climb(player, state))
    set_rule(world.get_location("Gliding Minigame Reward"), lambda state: can_double_climb(player, state) and can_glide(player, state))

    # Divers Locus
    set_rule(world.get_location("Essence of Water"), lambda state: state.has("Mining Tool", player))
    set_rule(world.get_location("Diving Minigame Reward"), lambda state: state.has_all(["Essence of Water", "Mining Tool"], player))

    # Hidden Lotus
    set_rule(world.get_location("Old String from Gourmand"), lambda state: can_double_climb(player, state) and can_glide(player, state) and state.has_all(["Headlamp", "Blade of Power", "Essence of Water"], player))

    # Indigo Island
    set_rule(world.get_location("Cococo's Shop Item 1"), lambda state: state.has("Mining Tool", player))
    set_rule(world.get_location("Cococo's Shop Item 2"), lambda state: state.has("Mining Tool", player))
    set_rule(world.get_location("Secret Opener"), lambda state: can_double_climb(player, state) and can_glide(player, state) and state.has_all(["Blade of Power", "Fire Starter Kit"], player))

    # Sacred Holm
    set_rule(world.get_location("Sacred Orb"), lambda state: can_double_climb(player, state) and can_glide(player, state) and state.has_all(["Blade of Power", "Fire Starter Kit", "Mining Tool"], player))


def can_climb(player: int, state: CollectionState) -> bool:
    return state.has_any(["Rusty Hooks", "Sturdy Hooks", "Tools of the Explorer"], player)


def can_double_climb(player: int, state: CollectionState) -> bool:
    return state.has_from_list(["Rusty Hooks", "Sturdy Hooks", "Tools of the Explorer"], player, 2)


def can_glide(player: int, state: CollectionState) -> bool:
    return state.has_any(["Leaf", "Tools of the Explorer"], player)
