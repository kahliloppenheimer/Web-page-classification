#!/bin/bash
# Takes summary algorithm as input (i.e. luhn, edmundson, etc.)
python prepData.py ../old/dmoz10.json raw/summary/${1} ${1}
(cd mallet && bin/mallet import-dir --remove-stopwords --input ../raw/summary/${1}/html --output input/summary/${1}.mallet)
(cd mallet && bin/mallet train-classifier --input input/summary/${1}.mallet --cross-validation 10 | tee output/summary/${1}.out)
