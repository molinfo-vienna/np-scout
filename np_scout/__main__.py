from nerdd_module import auto_cli

from .np_scout_model import NPScoutModel


@auto_cli
def main():
    return NPScoutModel()
