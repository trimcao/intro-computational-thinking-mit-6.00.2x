import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def countVowels(word):
    numVowels = 0
    for letter in word:
        if (letter == 'a') or (letter == 'i') or (letter == 'o') or (letter == 'e') or (letter == 'u'):
            numVowels += 1
    return numVowels

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    # calculate the proportion of vowels in each word:
    proportion = []
    for word in wordList:
        proportion.append(countVowels(word) / float(len(word)))

    # plot the histogram
    pylab.hist(proportion, numBins)
    pylab.title('Fraction of Vowels in Words')
    pylab.xlabel('Fraction of Vowels')
    pylab.ylabel('Number of Words')
    pylab.show()
     

if __name__ == '__main__':
    wordList = loadWords()
    #print wordList
    plotVowelProportionHistogram(wordList)

    
