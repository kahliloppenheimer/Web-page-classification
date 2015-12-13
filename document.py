from bs4 import BeautifulSoup
from subprocess import call
from urllib.request import urlopen


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

class Document(object):
    """A document to represent featurized HTML"""

    max_display_data = 10 # limit for data abbreviation

    def __init__(self, url, label=None, source=None):
        self.url = url
        self.label = label
        self.source = source

    def __repr__(self):
        return ("<%s: %s>" % (self.label, self.abbrev()) if self.label else
                "%s" % self.abbrev())

    def abbrev(self):
        return (self.data if len(self.data) < self.max_display_data else
                self.data[0:self.max_display_data] + "...")

    def features(self):
        """A list of features that characterize this document."""
        return self.data

class StrippedText(Document):
    """An HTML document with the text stripped right from the page"""

    def features(self):
        html = urlopen(doc['url'], timeout = 5).read()
        return cleanHtml(html)

class luhn(Document):
    def features(self, length = '20%'):
        return call([ 'sumy', 'luhn', '--url=' + self.url, '--length=' + length]).replace('\n',' ')

#class SummarizedPage(Document):
