# 6.00.2x Problem Set 4
# Name: Tri Minh Cao
# Email: trimcao@gmail.com
# Date: November 2015


import numpy
import random
import pylab
from ps3b import *


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, delayTime, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    
    viruses = []
    for dummy_idx in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    # initialize the virusPop to store the virus population over the timesteps
    totalSteps = delayTime + 150
    # we need the final virusPop after a trial
    finalPop = 0
    virusPop = []
    for idx in range(numTrials):
        print 'Trial: ', idx
        # initialize the patient named alvin
        alvin = TreatedPatient(viruses, maxPop)
        for step in range(delayTime):
            finalPop = alvin.update()
        # add the drug
        alvin.addPrescription('guttagonol')
        for step in range(150):
            finalPop = alvin.update()
        virusPop.append(finalPop) 
    print 'Prepare to plot...'
    # plot
    pylab.hist(virusPop)
    pylab.title('Virus Population Distribution with Delay = ' + str(delayTime)) 
    pylab.xlabel('Population')
    pylab.ylabel('Number of Occurences')
    pylab.show()


#resistances = {'guttagonol': False}
#simulationWithDrug(100, 1000, 0.1, 0.05, resistances, 0.005, 100)
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 10)

#
# PROBLEM 1
#        
def simulationDelayedTreatment(delayTime, numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    resistances = {'guttagonol': False, 'grimpex': False}
    simulationWithDrug(100, 1000, 0.1, 0.05, resistances, 0.005, delayTime, numTrials)

#simulationDelayedTreatment(150, 100)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(delayTime, numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    resistances = {'guttagonol': False, 'grimpex': False}
    simulationTwoDrugs(100, 1000, 0.1, 0.05, resistances, 0.005, delayTime, numTrials)


def simulationTwoDrugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, delayTime, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    
    viruses = []
    for dummy_idx in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    # initialize the virusPop to store the virus population over the timesteps
    totalSteps = delayTime + 150
    # we need the final virusPop after a trial
    finalPop = 0
    virusPop = []
    for idx in range(numTrials):
        print 'Trial: ', idx
        # initialize the patient named alvin
        alvin = TreatedPatient(viruses, maxPop)
        # first, run for 150 steps without any medication
        for step in range(150):
            finalPop = alvin.update()
        # add the drug
        alvin.addPrescription('guttagonol')
        for step in range(delayTime):
            finalPop = alvin.update()
        # final 150 steps
        alvin.addPrescription('grimpex')
        for step in range(150):
            finalPop = alvin.update()
        virusPop.append(finalPop) 
    print 'Prepare to plot...'
    # plot
    pylab.hist(virusPop)
    pylab.title('Virus Population Distribution with Delay of 2nd drug = ' + str(delayTime)) 
    pylab.xlabel('Population')
    pylab.ylabel('Number of Occurences')
    pylab.show()

simulationTwoDrugsDelayedTreatment(150, 100)
