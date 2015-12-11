# Samples lines randomly from a given file
#
# use:
# python sample-lines.py input_file output_file num_lines
from __future__ import print_function
import numpy as np
import codecs

# Setup unicode encoding to work
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

line_seps = [u'0x000A', u'0x000B', u'0x000C', u'0x000D', u'0x001C', u'0x001D', u'0x001E', u'0x0085', u'0x2028', u'0x2029']

# Returns the number of lines of a given file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Returns set of n line #s randomly selected from the file
def getRandLineNums(file, n):
    totalLines = np.arange(file_len(input))
    linesToPull = np.random.choice(totalLines, n, False)
    return set(linesToPull)

# Grab command line args (input, output, size)
input = sys.argv[1]
output = sys.argv[2]
n = sys.argv[3] if sys.argv.length > 3 else file_len(input)

# Pull out SAMPLE_SIZE random lines from the input file and print to putput file
lineNums = getRandLineNums(input, n)
with open(output, 'w') as output:
    with open(input) as input:
        for i, l in enumerate(input):
            if i in lineNums:
                # l = l.decode('unicode-escape')
                # Handles weird occasional unicode newlines that are created in parsing
                new = ''.join(l.splitlines()) + '\n'
                output.write(new)
