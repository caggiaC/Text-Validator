import sys

validationSets = []

def validateText(targetText, verbose=False):
    allowed = []
    for char in targetText:
        allowed.append(compareToSets(char))
    return all(allowed)

def validateFile(targetPath, verbose=False):
    allowed = []
    try:
        with open(targetPath, "r") as f:
            for line in f:
                for char in line:
                    allowed.append(compareToSets(char))
        return all(allowed)
    except:
        print('Error opening file.')
        return False


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
    if validateText(input('Enter text to be scanned: ')):
        print('No illegal characters found.')
    else:
        print('Text contains illegal characters.')

if __name__ == '__main__':
    main()
