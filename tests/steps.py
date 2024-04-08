from np_scout import NPScoutModel
from pytest_bdd import given


@given("the NPScout model", target_fixture="model")
def np_scout_model():
    return NPScoutModel()
