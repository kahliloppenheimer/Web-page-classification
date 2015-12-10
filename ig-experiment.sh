#!/bin/bash
bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-1.mallet --prune-infogain 1
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-1.mallet --prune-infogain 1

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-2.mallet --prune-infogain 2
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-2.mallet --prune-infogain 2

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-4.mallet --prune-infogain 4
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-4.mallet --prune-infogain 4

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-8.mallet --prune-infogain 8
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-8.mallet --prune-infogain 8

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-16.mallet --prune-infogain 16
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-16.mallet --prune-infogain 16

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-32.mallet --prune-infogain 32
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-32.mallet --prune-infogain 32

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-64.mallet --prune-infogain 64
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-64.mallet --prune-infogain 64

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-128.mallet --prune-infogain 128
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-128.mallet --prune-infogain 128

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-256.mallet --prune-infogain 256
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-256.mallet --prune-infogain 256

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-512.mallet --prune-infogain 512
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-512.mallet --prune-infogain 512

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-1024.mallet --prune-infogain 1024
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-1024.mallet --prune-infogain 1024

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-2048.mallet --prune-infogain 2048
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-2048.mallet --prune-infogain 2048

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-4096.mallet --prune-infogain 4096
bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-4096.mallet --prune-infogain 4096

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-8192.mallet --prune-infogain 8192
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-8192.mallet --prune-infogain 8192

bin/mallet prune --input input/dmoz50p.mallet --output input/ig-p-16384.mallet --prune-infogain 16384
bin/mallet prune --input input/dmoz50d.mallet --output input/ig-d-16384.mallet --prune-infogain 16384

bin/mallet train-classifier --input input/ig-p-1.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-1.out
bin/mallet train-classifier --input input/ig-d-1.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-1.out

bin/mallet train-classifier --input input/ig-p-2.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-2.out
bin/mallet train-classifier --input input/ig-d-2.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-2.out

bin/mallet train-classifier --input input/ig-p-4.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-4.out
bin/mallet train-classifier --input input/ig-d-4.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-4.out

bin/mallet train-classifier --input input/ig-p-8.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-8.out
bin/mallet train-classifier --input input/ig-d-8.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-8.out

bin/mallet train-classifier --input input/ig-p-16.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-16.out
bin/mallet train-classifier --input input/ig-d-16.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-16.out

bin/mallet train-classifier --input input/ig-p-32.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-32.out
bin/mallet train-classifier --input input/ig-d-32.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-32.out

bin/mallet train-classifier --input input/ig-p-64.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-64.out
bin/mallet train-classifier --input input/ig-d-64.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-64.out

bin/mallet train-classifier --input input/ig-p-128.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-128.out
bin/mallet train-classifier --input input/ig-d-128.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-128.out

bin/mallet train-classifier --input input/ig-p-256.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-256.out
bin/mallet train-classifier --input input/ig-d-256.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-256.out

bin/mallet train-classifier --input input/ig-p-512.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-512.out
bin/mallet train-classifier --input input/ig-d-512.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-512.out

bin/mallet train-classifier --input input/ig-p-1024.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-1024.out
bin/mallet train-classifier --input input/ig-d-1024.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-1024.out

bin/mallet train-classifier --input input/ig-p-2048.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-2048.out
bin/mallet train-classifier --input input/ig-d-2048.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-2048.out

bin/mallet train-classifier --input input/ig-p-4096.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-4096.out
bin/mallet train-classifier --input input/ig-d-4096.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-4096.out

bin/mallet train-classifier --input input/ig-p-8192.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-8192.out
bin/mallet train-classifier --input input/ig-d-8192.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-8192.out

bin/mallet train-classifier --input input/ig-p-16384.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-p-16384.out
bin/mallet train-classifier --input input/ig-d-16384.mallet --cross-validation 10 --trainer NaiveBayes --trainer BalancedWinnow --trainer MaxEnt | tee output/ig-d-16384.out
