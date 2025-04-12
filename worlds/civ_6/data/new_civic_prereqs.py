from typing import List

from ..ItemData import CivicPrereqData


new_civic_prereqs: List[CivicPrereqData] = [
    {"Civic": "CIVIC_AP_ANCIENT_01", "PrereqCivic": "CIVIC_AP_ANCIENT_00"},
    {"Civic": "CIVIC_AP_ANCIENT_02", "PrereqCivic": "CIVIC_AP_ANCIENT_00"},
    {"Civic": "CIVIC_AP_ANCIENT_03", "PrereqCivic": "CIVIC_AP_ANCIENT_01"},
    {"Civic": "CIVIC_AP_ANCIENT_04", "PrereqCivic": "CIVIC_AP_ANCIENT_01"},
    {"Civic": "CIVIC_AP_ANCIENT_05", "PrereqCivic": "CIVIC_AP_ANCIENT_02"},
    {"Civic": "CIVIC_AP_ANCIENT_06", "PrereqCivic": "CIVIC_AP_ANCIENT_02"},
    {"Civic": "CIVIC_AP_CLASSICAL_07", "PrereqCivic": "CIVIC_AP_ANCIENT_04"},
    {"Civic": "CIVIC_AP_CLASSICAL_08", "PrereqCivic": "CIVIC_AP_ANCIENT_04"},
    {"Civic": "CIVIC_AP_CLASSICAL_08", "PrereqCivic": "CIVIC_AP_ANCIENT_05"},
    {"Civic": "CIVIC_AP_CLASSICAL_09", "PrereqCivic": "CIVIC_AP_ANCIENT_05"},
    {"Civic": "CIVIC_AP_CLASSICAL_10", "PrereqCivic": "CIVIC_AP_ANCIENT_03"},
    {"Civic": "CIVIC_AP_CLASSICAL_10", "PrereqCivic": "CIVIC_AP_CLASSICAL_07"},
    {"Civic": "CIVIC_AP_CLASSICAL_11", "PrereqCivic": "CIVIC_AP_CLASSICAL_07"},
    {"Civic": "CIVIC_AP_CLASSICAL_11", "PrereqCivic": "CIVIC_AP_CLASSICAL_08"},
    {"Civic": "CIVIC_AP_CLASSICAL_12", "PrereqCivic": "CIVIC_AP_CLASSICAL_08"},
    {"Civic": "CIVIC_AP_CLASSICAL_12", "PrereqCivic": "CIVIC_AP_CLASSICAL_09"},
    {"Civic": "CIVIC_AP_CLASSICAL_13", "PrereqCivic": "CIVIC_AP_CLASSICAL_09"},
    {"Civic": "CIVIC_AP_CLASSICAL_13", "PrereqCivic": "CIVIC_AP_ANCIENT_06"},
    {"Civic": "CIVIC_AP_MEDIEVAL_14", "PrereqCivic": "CIVIC_AP_CLASSICAL_11"},
    {"Civic": "CIVIC_AP_MEDIEVAL_15", "PrereqCivic": "CIVIC_AP_CLASSICAL_11"},
    {"Civic": "CIVIC_AP_MEDIEVAL_16", "PrereqCivic": "CIVIC_AP_CLASSICAL_11"},
    {"Civic": "CIVIC_AP_MEDIEVAL_16", "PrereqCivic": "CIVIC_AP_CLASSICAL_12"},
    {"Civic": "CIVIC_AP_MEDIEVAL_17", "PrereqCivic": "CIVIC_AP_CLASSICAL_10"},
    {"Civic": "CIVIC_AP_MEDIEVAL_17", "PrereqCivic": "CIVIC_AP_MEDIEVAL_15"},
    {"Civic": "CIVIC_AP_MEDIEVAL_18", "PrereqCivic": "CIVIC_AP_MEDIEVAL_15"},
    {"Civic": "CIVIC_AP_MEDIEVAL_19", "PrereqCivic": "CIVIC_AP_MEDIEVAL_15"},
    {"Civic": "CIVIC_AP_MEDIEVAL_19", "PrereqCivic": "CIVIC_AP_MEDIEVAL_16"},
    {"Civic": "CIVIC_AP_MEDIEVAL_20", "PrereqCivic": "CIVIC_AP_MEDIEVAL_16"},
    {"Civic": "CIVIC_AP_MEDIEVAL_20", "PrereqCivic": "CIVIC_AP_CLASSICAL_13"},
    {"Civic": "CIVIC_AP_RENAISSANCE_21", "PrereqCivic": "CIVIC_AP_MEDIEVAL_17"},
    {"Civic": "CIVIC_AP_RENAISSANCE_21", "PrereqCivic": "CIVIC_AP_MEDIEVAL_18"},
    {"Civic": "CIVIC_AP_RENAISSANCE_22", "PrereqCivic": "CIVIC_AP_MEDIEVAL_18"},
    {"Civic": "CIVIC_AP_RENAISSANCE_22", "PrereqCivic": "CIVIC_AP_MEDIEVAL_19"},
    {"Civic": "CIVIC_AP_RENAISSANCE_23", "PrereqCivic": "CIVIC_AP_MEDIEVAL_19"},
    {"Civic": "CIVIC_AP_RENAISSANCE_24", "PrereqCivic": "CIVIC_AP_MEDIEVAL_19"},
    {"Civic": "CIVIC_AP_RENAISSANCE_24", "PrereqCivic": "CIVIC_AP_MEDIEVAL_20"},
    {"Civic": "CIVIC_AP_RENAISSANCE_25", "PrereqCivic": "CIVIC_AP_RENAISSANCE_22"},
    {"Civic": "CIVIC_AP_RENAISSANCE_26", "PrereqCivic": "CIVIC_AP_RENAISSANCE_22"},
    {"Civic": "CIVIC_AP_RENAISSANCE_26", "PrereqCivic": "CIVIC_AP_RENAISSANCE_23"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_27", "PrereqCivic": "CIVIC_AP_RENAISSANCE_25"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_28", "PrereqCivic": "CIVIC_AP_RENAISSANCE_25"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_29", "PrereqCivic": "CIVIC_AP_RENAISSANCE_26"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_30", "PrereqCivic": "CIVIC_AP_RENAISSANCE_26"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_31", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_27"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_32", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_29"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_33", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_28"},
    {"Civic": "CIVIC_AP_INDUSTRIAL_33", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_29"},
    {"Civic": "CIVIC_AP_MODERN_34", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_31"},
    {"Civic": "CIVIC_AP_MODERN_37", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_31"},
    {"Civic": "CIVIC_AP_MODERN_37", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_33"},
    {"Civic": "CIVIC_AP_MODERN_35", "PrereqCivic": "CIVIC_AP_MODERN_37"},
    {"Civic": "CIVIC_AP_MODERN_38", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_33"},
    {"Civic": "CIVIC_AP_MODERN_39", "PrereqCivic": "CIVIC_AP_MODERN_37"},
    {"Civic": "CIVIC_AP_MODERN_39", "PrereqCivic": "CIVIC_AP_MODERN_38"},
    {"Civic": "CIVIC_AP_MODERN_36", "PrereqCivic": "CIVIC_AP_MODERN_39"},
    {"Civic": "CIVIC_AP_MODERN_40", "PrereqCivic": "CIVIC_AP_MODERN_39"},
    {"Civic": "CIVIC_AP_MODERN_41", "PrereqCivic": "CIVIC_AP_MODERN_39"},
    {"Civic": "CIVIC_AP_MODERN_42", "PrereqCivic": "CIVIC_AP_MODERN_39"},
    {"Civic": "CIVIC_AP_ATOMIC_43", "PrereqCivic": "CIVIC_AP_MODERN_39"},
    {"Civic": "CIVIC_AP_ATOMIC_44", "PrereqCivic": "CIVIC_AP_MODERN_39"},
    {"Civic": "CIVIC_AP_ATOMIC_45", "PrereqCivic": "CIVIC_AP_MODERN_34"},
    {"Civic": "CIVIC_AP_ATOMIC_46", "PrereqCivic": "CIVIC_AP_ATOMIC_43"},
    {"Civic": "CIVIC_AP_ATOMIC_47", "PrereqCivic": "CIVIC_AP_ATOMIC_43"},
    {"Civic": "CIVIC_AP_INFORMATION_48", "PrereqCivic": "CIVIC_AP_ATOMIC_46"},
    {"Civic": "CIVIC_AP_INFORMATION_48", "PrereqCivic": "CIVIC_AP_ATOMIC_47"},
    {"Civic": "CIVIC_AP_INFORMATION_49", "PrereqCivic": "CIVIC_AP_ATOMIC_47"},
    {"Civic": "CIVIC_AP_INFORMATION_49", "PrereqCivic": "CIVIC_AP_ATOMIC_44"},
    {"Civic": "CIVIC_AP_FUTURE_50", "PrereqCivic": "CIVIC_AP_INFORMATION_48"},
    {"Civic": "CIVIC_AP_FUTURE_50", "PrereqCivic": "CIVIC_AP_INFORMATION_49"},
    {"Civic": "CIVIC_AP_MODERN_38", "PrereqCivic": "CIVIC_AP_INDUSTRIAL_32"},
    {"Civic": "CIVIC_AP_INFORMATION_51", "PrereqCivic": "CIVIC_AP_ATOMIC_45"},
    {"Civic": "CIVIC_AP_INFORMATION_51", "PrereqCivic": "CIVIC_AP_ATOMIC_46"},
    {"Civic": "CIVIC_AP_INFORMATION_52", "PrereqCivic": "CIVIC_AP_INFORMATION_48"},
    {"Civic": "CIVIC_AP_INFORMATION_52", "PrereqCivic": "CIVIC_AP_INFORMATION_49"},
    {"Civic": "CIVIC_AP_INFORMATION_53", "PrereqCivic": "CIVIC_AP_INFORMATION_48"},
    {"Civic": "CIVIC_AP_INFORMATION_53", "PrereqCivic": "CIVIC_AP_INFORMATION_49"},
    {"Civic": "CIVIC_AP_INFORMATION_54", "PrereqCivic": "CIVIC_AP_INFORMATION_48"},
    {"Civic": "CIVIC_AP_INFORMATION_54", "PrereqCivic": "CIVIC_AP_INFORMATION_49"},
    {"Civic": "CIVIC_AP_INFORMATION_55", "PrereqCivic": "CIVIC_AP_INFORMATION_51"},
    {"Civic": "CIVIC_AP_INFORMATION_55", "PrereqCivic": "CIVIC_AP_INFORMATION_48"},
    {"Civic": "CIVIC_AP_FUTURE_56", "PrereqCivic": "CIVIC_AP_FUTURE_50"},
    {"Civic": "CIVIC_AP_FUTURE_57", "PrereqCivic": "CIVIC_AP_FUTURE_50"},
    {"Civic": "CIVIC_AP_FUTURE_58", "PrereqCivic": "CIVIC_AP_FUTURE_50"},
    {"Civic": "CIVIC_AP_FUTURE_59", "PrereqCivic": "CIVIC_AP_FUTURE_50"},
    {"Civic": "CIVIC_AP_FUTURE_60", "PrereqCivic": "CIVIC_AP_FUTURE_50"},
]
