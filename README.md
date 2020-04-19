# DL-CRISPR_offtarget_prediction
TriplexFPP is a program for off-target activity prediction in CRISPR/Cas9 system. 

## SYSTEM REQUIREMENTS

### Hardware requirements
TriplexFPP requires only a standard computer with enough RAM to support the in-memory operations.

### Software requirements

#### OS Requirements

TriplexFPP has been tested on the following systems:

* macOS (10.14.6)
* Windows10

 with tensorflow 1 (>=1.12)

#### Python Dependencies

Based on python3.  
Python modules:  
```
numpy  
pandas  
csv  
tensorflow 
keras
```

## EXPLANATION
This repository contains five folders and one docx file.

### Supplementary Table.docx:
the supplementary materials for [1].

### data folder:
Contains the data in [1].

### code folder:
Contains the python codes.  
```
dlcrispr_util.py -- functions will be used.  
DL_CRISPR.ipynb -- user interface.  
```
### model folder:
This folder contains the models. The models are from one of the 5-fold cross-fold validation.

### input_example folder:
This folder contains example input files. These example files are from one of 5-fold cross-fold validation positive test data, which are consistent with the model folder above.

### output_files folder:
The output result files will be put into this folder.


## USAGE:
  
Download the github repository, open DL_CRISPR.ipynb in code file, change data path:  
```
datapath = '.../...'
```
to where this respository dwonloaded,
change input file path and name
```
inputfile = '.csv' 
```
to where input file is, refer to the example input file for the format.
change output file name
```
outputname = '.csv'
```
to the output file name, the output file will be at the datapath/output.

* To run DL-CRISPR off-target prediction:
  - open DL_CRISPR.ipynb
  - change corresponding data path and file names
  - run
 
the default name is the demo, it takes about 20s to run.

More details can be found from [1]

## REFERANCE
[1] 
## CONTACT
If you have any inqueries, please contact YU007@e.ntu.edu.sg
