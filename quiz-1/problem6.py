import random
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)
    
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if (title != None):
        pylab.title(title)
    pylab.show()
    
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    total_longest_run = 0
    longest_runs = []
    for dummy_idx in range(numTrials):
        rolls = []
        for dummy_idx2 in range(numRolls):
            rolls.append(die.roll())
        print rolls
        longest = longestRun(rolls)
        longest_runs.append(longest)
        total_longest_run += longest
    # call histogram
    #makeHistogram(longest_runs, 10, 'Longest Runs', "Number of Occurances", "Quiz")
    return float(total_longest_run) / numTrials
    
def longestRun(rolls):
    longest = 1
    count = 1
    currentVal = -1
    while(len(rolls) > 0):
        nextVal = rolls.pop()
        if (nextVal == currentVal):
            count += 1
        else:
            if (count > longest):
                longest = count            
            count = 1
            currentVal = nextVal
    if (count > longest):
        longest = count
    return longest

# test longestRun
#rolls = [5, 4, 4, 5, 5, 2, 5]
#rolls = [1,4, 3]
#print longestRun(rolls)

#print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
print getAverage(Die([1]), 10, 1)
    
    
    
    
    
    
    
