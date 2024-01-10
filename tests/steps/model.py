from np_scout import NPScoutModel
from pytest_bdd import given, parsers


@given("the NPScout model", target_fixture="model")
def model():
    return NPScoutModel()


@given(parsers.parse("the input type is '{input_type}'"), target_fixture="input_type")
def input_type(input_type):
    return input_type
