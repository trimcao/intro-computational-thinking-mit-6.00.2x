"""
Lecture 5 Problems
Date: November 2015
"""
import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    balls = [1, 2, 1, 2, 1, 2] # 1 is red, 2 is green
    failures = 0
    for dummy_idx in range(numTrials):
        balls_trial = list(balls)
        random.shuffle(balls_trial)
        balls_drawn = []
        for idx in range(3):
            balls_drawn.append(balls_trial.pop())
            #ball = random.choice(balls_trial)
            #balls_drawn.append(ball)
            #balls_trial.remove(ball)
        first_ball = balls_drawn[0]
        for each_ball in balls_drawn:
            if (first_ball != each_ball):
                failures += 1
                break
    successes = numTrials - failures            
    return float(successes) / numTrials

print noReplacementSimulation(100000)
