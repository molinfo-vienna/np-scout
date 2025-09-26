# NP-Scout

## Installation

```sh
conda env create -f environment.yml
conda activate np_scout

curl -sS https://gist.githubusercontent.com/shirte/e1734e51dbc72984b2d918a71b68c25b/raw/ae4afece11980f5d7da9e7668a651abe349c357a/rdkit_installation_fix.sh | bash -s np_scout

pip install .
```

## About NP-Scout

NP-Scout is a free web service for the:

* Identification of natural products in large molecular libraries
* Quantification of natural product-likeness of small molecules
* Visualization of atoms and areas in small molecules characteristic to natural products or synthetic molecules (based on similarity maps)

NP-Scout utilizes random forest classifiers trained on data sets consisting of more than 265k natural products and synthetic molecules ([doi: 10.3390/biom9020043](https://www.mdpi.com/2218-273X/9/2/43)).

## Usage

Molecular structures can be loaded either by directly drawing a molecule with the JSME Molecular editor [1], by pasting a SMILES into the field “Enter SMILES”, or by uploading a text file containing a list of SMILES. NP-Scout runs a thorough data preparation protocol to standardize the input. Therefore, chemical structures do not need to be preprocessed by the user with respect to hydrogen annotation, aromatization, protonation, tautomerism and stereochemistry. Salts are also recognized, and the minor components removed prior to calculations. 

[1] Bienfait, B.; Ertl, P. JSME: a free molecule editor in JavaScript. J. Cheminform. 2013, 5, 24. 
 
## Example upload file

Lists of SMILES should be formatted as shown in the following examples: 
1. One SMILES per row with no additional data 
<br /> ```C=C1C(=O)OC2C1CCC1(C)OC13CC=C(C)C23```
<br /> ```CC12C=CC(=O)NC1CCC1C2CCC2(C)C(C(=O)Nc3cc(C(F)(F)F)ccc3C(F)(F)F)CCC12```

2. One SMILES per row with additional data 
<br /> ```C=C1C(=O)OC2C1CCC1(C)OC13CC=C(C)C23 arglabin```
<br /> ```CC12C=CC(=O)NC1CCC1C2CCC2(C)C(C(=O)Nc3cc(C(F)(F)F)ccc3C(F)(F)F)CCC12 dutaseride```

The following separators may be used: *" "* (space character) or *"\t"* (tab). 

## Running the calculations

Calculations are started by clicking the *"Submit"* button. A new web page will load that reports on the progress of calculations and displays a web link that allows users to return and inspect the results once all calculations have been completed. 

## Analyzing the results

The results page displays a table that presents the predictions for the query molecules.

* Column *"Name"* reports the input.
* Column *"Input SMILES"* reports the input SMILES with or without the name of a molecule.
* Column *"Filtered SMILES"* reports the filtered SMILES.
* Column *"Error/Warning"* reports any errors or warnings.
* Column *"NP class probability"* reports the predicted probability of the molecule being a natural product.
* Column *"Similarity maps"* shows a visualization of similarity maps. Green highlights mark atom contributing to the classification of a molecule as natural products, whereas orange highlights mark atoms contributing to the classification of a molecule as synthetic molecules. Note that similarity maps are not calculated for molecules with a molecular weight below 150 Da or above 1500 Da.

The results in *.csv* format can be downloaded for further use. The *.csv* file contains all the information from the table of results except for the similarity maps.


## Contribute

```
conda env create -f environment.yml
conda activate np_scout
pip install -e .[dev,test]
ptw
```

## Contributors

* Ya Chen
* Steffen Hirte
* Axinya Tokareva