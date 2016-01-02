import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    oldRabbitPop = CURRENTRABBITPOP
    for idx in range(oldRabbitPop):
        reproduceProb = 1.0 - float(CURRENTRABBITPOP)/MAXRABBITPOP
        if (random.random() < reproduceProb):
            CURRENTRABBITPOP += 1

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    oldFoxPop = CURRENTFOXPOP
    for idx in range(oldFoxPop):
        huntProb = float(CURRENTRABBITPOP) / MAXRABBITPOP
        if (random.random() < huntProb):
            if (CURRENTRABBITPOP > 10):
                CURRENTRABBITPOP -= 1
            if (random.random() < 0.333):
                CURRENTFOXPOP += 1
        else:
            if (random.random() < 0.9):
                if (CURRENTFOXPOP > 10):
                    CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbitPops = []
    foxPops = []
    for idx in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPops.append(CURRENTRABBITPOP)
        foxPops.append(CURRENTFOXPOP)
    return (rabbitPops, foxPops)

def plotStuff():
    rabbitPops, foxPops = runSimulation(200)
    steps = [n for n in range(1, 201)]
    pylab.plot(steps, rabbitPops)
    pylab.plot(steps, foxPops)
    pylab.title('Fox vs. Rabbit')
    pylab.legend(('Rabbit Pop', 'Fox Pop'))
    pylab.xlabel('Step')
    pylab.ylabel('Population')
    pylab.show()

def plotLineFit():
    rabbitPops, foxPops = runSimulation(200)
    steps = [n for n in range(1, 201)]
    coeff = pylab.polyfit(range(len(rabbitPops)), rabbitPops, 2)
    pylab.plot(pylab.polyval(coeff, range(len(rabbitPops))))
    coeff = pylab.polyfit(range(len(foxPops)), foxPops, 2)
    pylab.plot(pylab.polyval(coeff, range(len(foxPops))))
    pylab.title('Fox vs. Rabbit')
    pylab.legend(('Rabbit Pop', 'Fox Pop'))
    pylab.xlabel('Step')
    pylab.ylabel('Population')
    pylab.show()

#plotStuff()
plotLineFit()
