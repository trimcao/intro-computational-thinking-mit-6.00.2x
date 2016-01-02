
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    if (len(L) == 0):
        return float('NaN')
    else:
        mean = 0
        sum = 0
        for each in L:
            sum += len(each)
        mean = sum / float(len(L))
        stdDev = 0
        for each in L:
            stdDev += (len(each) - mean)**2
        stdDev = (stdDev / float(len(L))) ** 0.5
        return stdDev
        
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)
    

