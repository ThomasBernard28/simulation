import sys
import re
import numpy as np
import scipy.stats as stats

from matplotlib import pyplot as plt


class EDecimals:
    def __init__(self, file):
        self.file = file
        self.decimals = self.initialize()

    def initialize(self):
        try:
            with open(self.file, "r") as f:
                e = f.read()
                # delete all \n from the e string
                new_e = re.sub(r'\n', '', e)
                # First two characters are 2. and they are not decimals
                decimals = [int(i) for i in new_e[2:]]
                return decimals
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)

    def displayInformation(self):
        eLabels, eFreq = np.unique(self.decimals, return_counts=True)
        print("Voici les différentes valeurs présentes dans les décimales de e : " + str(eLabels))
        print("Voici le nombre de fois où chaque valeur est présente : " + str(eFreq))
        print("Voici le graphique de répartition des décimales de e : ")
        plt.figure()
        plt.bar(eLabels, eFreq)
        plt.title("Distribution des décimales de e")
        plt.savefig("eDecimalsDistribution.png")
        plt.show()

    def chiSquaredTest(self):
        '''Test if the decimals of e are uniformly distributed'''
        observedFrequencies = np.zeros(10)
        for digit in self.decimals:
            observedFrequencies[digit] += 1
        expectedFrequencies = np.full(10, len(self.decimals) / 10)

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