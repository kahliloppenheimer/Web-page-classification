# python curlData.py input_file output_dir num_lines document_type
from urllib.request import urlopen
import document
import json
import sys
import os
import socket
import numpy as np
import codecs

# Possible labels for dmoz dataset
LABELS = ['Arts', 'Computers', 'Health', 'News', 'Recreation', 'Regional', 'Shopping', 'Sports', 'World', 'Business', 'Games', 'Home', 'Reference', 'Science', 'Society']

# Returns set of n line #s randomly selected from the file
def getRandLineNums(file, n):
    totalLines = np.arange(getNumLines(input))
    linesToPull = np.random.choice(totalLines, n, False)
    return set(linesToPull)

# Returns the # of lines of the given file
def getNumLines(file_name):
    count = 0
    with open(file_name) as f:
        for l in f:
            count += 1
    return count

# Prints out the given json object to the output directory
# with the features as obj[feature_field], file name as obj['url'],
# and subdirectory (label) as obj['topic']. Returns True if
# conversion from JSON to mallet input was succesful, false otherwise
def printObj(dir, obj, feature_field):
    # Since we're going to use these as file names, we can't have slashes
    name = obj['url'].replace('/', '')
    label = obj['topic'].split('/')
    # Weird cases where there is no label like top/*
    if(len(label) < 2 or label[1] not in LABELS):
        return False
    label = label[1]
    features = obj[feature_field]
    instance_path = os.path.join(dir, label)
    if (name and label and features):
        if not os.path.isdir(instance_path):
            os.makedirs(instance_path)
        with open(os.path.join(instance_path, name), 'w') as f:
            f.write(features)
        return True
    else:
        return False

# Input JSON file
input = sys.argv[1]
numLines = getNumLines(input)
numErrors = 0
# Output directory with input for mallet
output_dir = sys.argv[2]
# Number of lines from JSON to randomly sample (defaults to all lines)
n = int(sys.argv[3]) if len(sys.argv) > 3 else numLines
# Type of document to parse HTML as (defaults to StrippedText)
document_type = eval('document.' + sys.argv[4].replace('-', '').capitalize()) if len(sys.argv) > 4 else document.StrippedText
lineNums = getRandLineNums(input, n)
currLine = 0

with open (input) as f:
    for i, line in enumerate(f):
        if (i in lineNums):
            currLine += 1
            if ((currLine) % 50 == 0):
                print(100 * float(currLine) / n, '% done', 'nErrors:', numErrors, '(', 100 * float(numErrors) / currLine, ')%')
            doc = json.loads(line)
            if (type(doc) == type(u'foo')):
                doc = json.loads(doc)
            try:
                doc['html'] = document_type(doc['url']).features()
                printObj(os.path.join(output_dir, 'desc'), doc, 'd:Description')
                printObj(os.path.join(output_dir, 'html'), doc, 'html')
                print ('line', currLine, '(', 100 * float(currLine) / n, '%)')
            except Exception as e:
                numErrors += 1
                raise (e)
