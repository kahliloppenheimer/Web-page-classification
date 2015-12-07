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

input = sys.argv[1]
output_dir = sys.argv[2]

numLines = getNumLines(input)
numErrors = 0

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open (input) as f:
    for i, line in enumerate(f):
        next_file = os.path.join(output_dir, 'd' + str(i) + '.json')
        with open(next_file, 'w') as out:
            if ((i + 1) % 50 < .00001):
                print 100 * float(i + 1) / numLines, '% done', 'nErrors:', numErrors, '(', 100 * float(numErrors) / i, ')%'
            # First call to loads removes escape characters but does not turn
            # into dict for strange reason
            doc = json.loads(line)
            if (type(doc) == type(u'foo')):
                doc = json.loads(doc)
            try:
                html = unicode(urllib2.urlopen(doc['url'], timeout = 5).read(), errors='ignore')
                origLength = len(html)
                cleaned = cleanHtml(html)
                doc['html'] = cleaned
                json.dump(doc, out)
                out.write('\n')
                print 'line', i + 1, 'html length:', len(html), 'stripped length:', len(cleaned)
            except socket.timeout, e:
                numErrors += 1
                print 'URL timeout:', doc['url']
            except urllib2.URLError, e:
                numErrors += 1
                print 'URL timeout:', doc['url']
            except urllib2.HTTPError, e:
                numErrors += 1
                print 'SKIPPED (HTTPError):', doc['url']
            # except Exception as e:
                # raise e
                # numErrors += 1
                # doc['html'] = 'ERROR'
                # print 'other error'
