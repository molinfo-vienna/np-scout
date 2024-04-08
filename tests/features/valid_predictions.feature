@np_scout
Feature: Valid predictions

  Scenario Outline: Predictions are valid
    Given a random seed set to <seed>
    And the input type is '<input_type>'
    And a list of <num_molecules> random molecules, where <num_none> entries are None
    And the representations of the molecules
    And the NPScout model

    When the model generates predictions for the molecule representations
    And The subset of the result where the input was not None is considered

    Then the result should be a pandas DataFrame
    And The result should contain the columns:
            probability
            similarity_map
    And the value in column 'probability' should be between 0 and 1
    And the value in column 'similarity_map' should be a png image


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
