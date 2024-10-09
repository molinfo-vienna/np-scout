from nerdd_module.preprocessing import FilterByElement, FilterByWeight

from .canonicalize_tautomer import CanonicalizeTautomer
from .do_smiles_roundtrip import DoSmilesRoundtrip
from .neutralize_charges import NeutralizeCharges
from .strip_salts import StripSalts

__all__ = ["preprocessing_steps"]

preprocessing_steps=[
    DoSmilesRoundtrip(remove_stereo=False),
    StripSalts(),
    NeutralizeCharges(),
    FilterByWeight(
        min_weight=150,
        max_weight=1500,
        remove_invalid_molecules=True,
    ),
    FilterByElement(
        allowed_elements=[
            "H",
            "B",
            "C",
            "N",
            "O",
            "F",
            "Si",
            "P",
            "S",
            "Cl",
            "Se",
            "Br",
            "I",
        ],
        remove_invalid_molecules=True,
    ),
    CanonicalizeTautomer(
        remove_stereo=False,
        remove_invalid_molecules=True,
    ),
    DoSmilesRoundtrip(remove_stereo=False),
]
