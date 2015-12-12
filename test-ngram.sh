#!/bin/bash

# Imports both description and full page of the passed size as n-gram
# then evaluates each

(cd mallet && bin/mallet import-dir --input ../raw/dmoz5c.data/desc/* --output input/ngram/gram-d-${1}.mallet --remove-stopwords --gram-sizes ${1})
(cd mallet && bin/mallet import-dir --input ../raw/dmoz5c.data/html/* --output input/ngram/gram-p-${1}.mallet --remove-stopwords --gram-sizes ${1})

(cd mallet && bin/mallet train-classifier --input input/ngram/gram-d-${1}.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ngram/gram-d-${1}.out)
(cd mallet && bin/mallet train-classifier --input input/ngram/gram-p-${1}.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ngram/gram-p-${1}.out)
