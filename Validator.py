import sys

validationSets = []

def validate(targetText, verbose=False):
    allowed = []
    for char in targetText:
        allowed.append(compareToSets(char))
    return all(allowed)


def compareToSets(char, verbose=False):
    charInSet = []
    for setElement in validationSets:
        if char in setElement:
            charInSet.append(True)
        else:
            charInSet.append(False)
    return any(charInSet)
            

def init(verbose=False):
    try:
        with open("allowedCharSets.txt", "r") as f:
            for line in f:
                validationSets.append(line)
    except:
        sys.stderr.write('Error encountered when attempting to read \'allowedCharSets.txt\'. File may be missing.')
        exit()

def main(verbose=False):
    init(verbose)
    if validate(input('Enter text to be scanned: ')):
        print('No illegal characters found.')
    else:
        print('Text contains illegal characters.')

if __name__ == '__main__':
    main()
