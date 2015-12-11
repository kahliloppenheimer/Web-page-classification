# python curlData.py input_file output_dir num_lines
from __future__ import print_function
from bs4 import BeautifulSoup
import json
import sys
import os
import urllib2
import socket
import numpy as np
import codecs

# Setup unicode encoding to work
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

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

# Parses all scripts/CSS/html tags out of html
# Taken from http://stackoverflow.com/questions/22799990/beatifulsoup4-get-text-still-has-javascript
def cleanHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = ' '.join(chunk for chunk in chunks if chunk)
    return text


# Prints out the given json object to the output directory
# with the features as obj[feature_field], file name as obj['url'],
# and subdirectory (label) as obj['topic']. Returns True if
# conversion from JSON to mallet input was succesful, false otherwise
def printObj(dir, obj, feature_field):
    # Since we're going to use these as file names, we can't have slashes
    name = obj['url'].replace('/', '')
    label = obj['topic'].split('/')
    # Weird cases where there is no label like top/*
    if(len(label) < 2):
        return False
    label = label[1]
    features = obj[feature_field]
    instance_path = os.path.join(dir, label)
    if (name and label and features):
        if not os.path.isdir(instance_path):
            os.makedirs(instance_path)
        with open(os.path.join(instance_path, name), 'w') as f:
            f.write(features.encode('utf8'))
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
                html = unicode(urllib2.urlopen(doc['url'], timeout = 5).read(), errors='ignore')
                doc['html'] = cleanHtml(html)
                printObj(os.path.join(output_dir, 'desc'), doc, 'd:Description')
                printObj(os.path.join(output_dir, 'html'), doc, 'html')
                print ('line', currLine, '(', 100 * float(currLine) / n, '%)')
            except Exception as e:
                numErrors += 1
                print (e)
