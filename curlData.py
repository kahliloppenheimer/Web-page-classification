import json
import sys
import os
import urllib2
from bs4 import BeautifulSoup
import socket

def getNumLines(file_name):
    count = 0
    with open(file_name) as f:
        for l in f:
            count += 1
    return count

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

input = sys.argv[1]
output_dir = sys.argv[2]

numLines = getNumLines(input)
numErrors = 0

with open (input) as f:
    for i, line in enumerate(f):
        if ((i + 1) % 50 < .00001):
            print 100 * float(i + 1) / numLines, '% done', 'nErrors:', numErrors, '(', 100 * float(numErrors) / i, ')%'
        # First call to loads removes escape characters but does not turn
        # into dict for strange reason
        doc = json.loads(line)
        if (type(doc) == type(u'foo')):
            doc = json.loads(doc)
        try:
            html = unicode(urllib2.urlopen(doc['url'], timeout = 5).read(), errors='ignore')
            doc['html'] = cleanHtml(html)
            printObj(os.path.join(output_dir, 'desc'), doc, 'd:Description')
            printObj(os.path.join(output_dir, 'html'), doc, 'html')
            print 'line', i + 1, '(', 100 * float(i) / numLines, '%)'
        except socket.timeout, e:
            numErrors += 1
            print 'URL timeout:', doc['url']
        except urllib2.URLError, e:
            numErrors += 1
            print 'URL timeout:', doc['url']
        except urllib2.HTTPError, e:
            numErrors += 1
            print 'SKIPPED (HTTPError):', doc['url']
        except Exception as e:
            numErrors += 1
            print e
