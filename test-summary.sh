#!/bin/bash
# Takes summary algorithm as input (i.e. luhn, edmundson, etc.)
python prepData.py ../old/dmoz10.json raw/summary/${1} 100% ${1}
