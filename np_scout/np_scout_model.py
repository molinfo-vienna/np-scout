import base64
import sys
from io import BytesIO
from typing import List

import matplotlib as mpl
import numpy as np
from joblib import load
from rdkit.Chem import AllChem, Mol, MolToSmiles
from rdkit.Chem.Draw import SimilarityMaps

mpl.use("Agg")


import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from nerdd_module import SimpleModel

from .preprocessing import preprocessing_steps

if sys.version_info < (3, 9):
    from importlib_resources import files
else:
    from importlib.resources import files

import warnings

# avoid warnings in old versions of numpy
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

__all__ = ["NPScoutModel"]

# load ml models
# build with n_jobs=1
clfMaccs = load(files("np_scout").joinpath("models").joinpath("clf_maccs.pkl.gz"))
clfMorgan = load(files("np_scout").joinpath("models").joinpath("clf_morgan2.pkl.gz"))

# build with n_jobs=4
clfMaccs4 = load(files("np_scout").joinpath("models").joinpath("clf_maccs_4.pkl.gz"))
clfMorgan4 = load(files("np_scout").joinpath("models").joinpath("clf_morgan2_4.pkl.gz"))


def get_similarity_map(model, mol, fSize, colorMap, cL):
    """
    Builds a similarity map for the NPScout model

    :param args: model: model for which the sim map should be build, mol: rdkit molecule, colorMap: colorMap of NpscoutCalculator, fSize: figure size of NpscoutCalculator, cL: contuor lines of the NpscoutCalculator
    :return: binary sting of map
    """
    try:
        predict = lambda fp: model.predict_proba([fp])[0][1]
        fig, _ = SimilarityMaps.GetSimilarityMapForModel(
            mol,
            lambda m, id: SimilarityMaps.GetMorganFingerprint(
                m, id, radius=2, nBits=1024
            ),
            predict,
            size=fSize,  # width == height
            colorMap=colorMap,
            contourLines=cL,
            sigma=None,  # don't change this! CS: why?
            step=0.01,
        )
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format="png", bbox_inches="tight")
        encoded = base64.b64encode(tmpfile.getvalue())
        image = '<img src="data:image/png;base64,{}">'.format(encoded.decode("utf-8"))
        image_resize = image[:-1] + ' width = "200" height="200" />'
        plt.close(fig)
        return image_resize
    except ZeroDivisionError:
        print(
            MolToSmiles(mol),
            "This mol was printed because the similarity map raises an ZeroDivisionError. If someone can find out why would be great, cheers ;)",
        )
        return None


def predict(
    mols: List[Mol],
    contour_lines: bool = False,
    quality: str = "low",
) -> List[dict]:
    similarity_map_size = (150, 150) if quality == "low" else (300, 300)

    # calculate features

    # calculate descriptors and probabilities
    maccs = [AllChem.GetMACCSKeysFingerprint(mol) for mol in mols]
    # maccs = Parallel(n_jobs=4, backend="threading")(
    #     delayed(AllChem.GetMACCSKeysFingerprint)(mol) for mol in mols
    # )

    if len(mols) > 0:
        # avoid mypy complaining about round_ not being an attribute of np

        probabilities = np.round_(  # type: ignore
            clfMaccs.predict_proba(maccs)[:, 1], decimals=2, out=None
        )
    else:
        probabilities = []

    # build similarity maps
    color_map = LinearSegmentedColormap.from_list(
        "PiWG", ["#FFB029", "#FFFFFF", "#39DB6A"], N=255
    )

    similarity_maps = [
        get_similarity_map(
            clfMorgan,
            mol,
            similarity_map_size,
            color_map,
            (10 if contour_lines else 0),
        )
        for mol in mols
    ]

    return [
        {"probability": prob, "similarity_ap": sim_map}
        for prob, sim_map in zip(probabilities, similarity_maps)
    ]


class NPScoutModel(SimpleModel):
    def __init__(self):
        super().__init__(
            preprocessing_steps=preprocessing_steps,
        )

    def _predict_mols(
        self,
        mols: List[Mol],
        contour_lines: bool = False,
        quality: str = "low",
    ) -> List[dict]:
        assert quality in ["low", "high"]

        return predict(mols, contour_lines, quality)
