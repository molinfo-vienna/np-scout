from np_scout import NPScoutModel
from pytest_bdd import parsers, when


@when(
    parsers.parse(
        "the NPScout model generates predictions for the molecule representations"
    ),
    target_fixture="predictions",
)
def predictions(representations, input_type):
    model = NPScoutModel()
    return model.predict(
        representations,
        input_type=input_type,
        output_format="record_list",
    )
