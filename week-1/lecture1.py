"""
Code for quizzes in lecture 1
"""
import pylab

def load_file(name):
    high = []
    low = []
    inLine = open(name, 'r')
    for line in inLine:
        fields = line[:-1].split(' ')
        if (len(fields) != 3 or not fields[0].isdigit()):
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))

    return (high, low)

def producePlot(lowTemps, highTemps):
    diffTemps = []
    for idx in range(len(lowTemps)):
        diffTemps.append(highTemps[idx] - lowTemps[idx])
    pylab.plot(range(1, 32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

high, low = load_file('julyTemps.txt')
producePlot(low, high) 
