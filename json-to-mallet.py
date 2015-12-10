# Command line args
# 1) input JSON file name
# 2) output text file name
# 3) field of JSON to use as features
import sys
import json
import os

# Prints out the given json object to the given output stream
# with the features as obj[feature_field]. Returns True if
# conversion from JSON to mallet input was succesful, false otherwise
def printObj(out, obj, feature_field):
    name = obj['url']
    label = obj['topic'].split('/')
    # Weird cases where there is no label like top/*
    if(len(label) < 2):
        return False
    label = label[1]
    features = obj[feature_field]
    if (name and label and features):
        out.write(name + '\t' + label + '\t' + features + '\n')
        return True
    else:
        return False

input = sys.argv[1]
output = sys.argv[2]
feature_field = sys.argv[3]

sCount = 0
total = 0

if (os.path.isdir(input)):
    with open(output, 'w') as out:
        for fName in os.listdir(input):
            with open(os.path.join(input, fName)) as f:
                for l in f:
                    total += 1
                    obj = json.loads(l)
                    if(printObj(out, obj, feature_field)):
                        sCount += 1

else:
    with open(output, 'w') as out:
        with open(input) as f:
            for l in f:
                total += 1
                print(total)
                obj = json.loads(l)
                if(printObj(out, obj, feature_field)):
                    sCount += 1

print(100 * float(sCount) / total)
