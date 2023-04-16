import re
import numpy as np
import scipy.stats as stats


def initialize(file):
    with open(file, "r") as f:
        e = f.read()
        # delete all \n from the e string
        new_e = re.sub(r'\n', '', e)
        # First two characters are 2. and they are not decimals
        decimals = [int(i) for i in new_e[2:]]
        chiSquaredTest(decimals)

def chiSquaredTest(data):
    '''Test if the decimals of e are uniformly distributed'''
    observedFrequencies = np.zeros(10)
    for digit in data:
        observedFrequencies[digit] += 1
    expectedFrequencies = np.full(10, len(data) / 10)

    chiSquared, pValue = stats.chisquare(observedFrequencies, expectedFrequencies)
    alpha = 0.05

    if pValue > alpha:
        print("\nWe can't reject the null hypothesis\n")
        print("The decimals of e are uniformly distributed and so are random \n\n"
              "The p-value is : " + str(pValue) + " and the alpha is : " + str(alpha) + "\n\n"
              "As the p-value is greater than the alpha, we can't reject the null hypothesis\n\n"
              "The expected frequencies are : " + str(expectedFrequencies) + "\n\n"
              "The observed frequencies are : " + str(observedFrequencies))


    else:
        print("We reject the null hypothesis")
        print("The decimals of e are not uniformly distributed and so are not random")


# With a 2M data set and 10 intervals, the expected value is 200000
# But we observed : [199093, 200171, 199471, 200361, 199923, 200285, 200395, 199789, 200098, 200414]

def kolmogrovSmirnovTest(decimals):
    '''Generate a uniform distribution with the len of decimals'''

    uniformDistribution = np.random.uniform(0, 1, len(decimals))

    '''Perform the Kolmogrov-Smirnov test'''
    D, pValue = stats.kstest(decimals, uniformDistribution)

    print(f"Kolmogrov-Smirnov test : D = {D} and p-value = {pValue}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        initialize(sys.argv[1])
    else:
        print("Please choose a file to exploit by giving it as argument")
        sys.exit(1)
