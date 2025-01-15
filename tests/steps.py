from pytest_bdd import parsers, when

from np_scout import NPScoutModel


@when(
    parsers.parse(
        "the NPScout model generates predictions for the molecule representations"
    ),
    target_fixture="predictions",
)
def predictions(representations):
    model = NPScoutModel()
    return model.predict(
        representations,
        output_format="record_list",
    )
