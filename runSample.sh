#!/bin/bash
(cd mallet && bin/mallet import-dir --input ../raw/dmoz${1}c.data/desc/* --output input/sample/sample-d-${1}.mallet --remove-stopwords)
(cd mallet && bin/mallet import-dir --input ../raw/dmoz${1}c.data/html/* --output input/sample/sample-p-${1}.mallet --remove-stopwords)

(cd mallet && bin/mallet train-classifier --input input/sample/sample-d-${1}.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/sample/sample-d-${1}.out)
(cd mallet && bin/mallet train-classifier --input input/sample/sample-p-${1}.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/sample/sample-p-${1}.out)
