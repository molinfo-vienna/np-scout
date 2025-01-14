@np_scout
Feature: Valid predictions

  Scenario Outline: Predictions are valid
    Given a random seed set to <seed>
    And a list of <num_molecules> random molecules, where <num_none> entries are None
    And the representations of the molecules in <input_type> format

    When the NPScout model generates predictions for the molecule representations
    And the subset of the result where the input was not None is considered

    # TODO: add similarity_map
    Then the result should contain the columns:
            probability
    And the value in column 'probability' should be between 0 and 1


  Examples:
  | seed | num_molecules | num_none | input_type |
  | 1    | 10            | 0        | smiles     |
  | 2    | 10            | 1        | smiles     |
  | 3    | 10            | 2        | smiles     |
  | 4    | 10            | 10       | smiles     |
  | 1    | 10            | 0        | smiles     |
  | 2    | 10            | 1        | smiles     |
  | 3    | 10            | 2        | smiles     |
  | 4    | 10            | 10       | smiles     |
