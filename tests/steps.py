from np_scout import NPScoutModel
from pytest_bdd import given, parsers, when


@given("the NPScout model", target_fixture="predictor")
def np_scout_model():
    return NPScoutModel()


@when(
    parsers.parse("the model generates predictions for the molecule representations"),
    target_fixture="predictions",
)
def predictions(representations, predictor, input_type):
    return predictor.predict(
        representations,
        input_type=input_type,
        output_format="record_list",
    )