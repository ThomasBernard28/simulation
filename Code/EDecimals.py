import sys
import re
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2

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

    def chiSquaredTest(self, df=None, pValues=[0.1, 0.05, 0.01, 0.001]):
        observedFrequencies = np.zeros(10)
        for digit in self.decimals:
            observedFrequencies[digit] += 1
        expectedFrequencies = np.zeros(10)
        for i in range(10):
            expectedFrequencies[i] = len(self.decimals) / 10
        Kr = np.sum((observedFrequencies - expectedFrequencies) ** 2 / expectedFrequencies)
        print("Here is the Kr value : " + str(Kr))

        if df is None:
            df = len(observedFrequencies) - 1
        else:
            df = df

        for p in pValues:
            if Kr <= chi2.ppf(q=1 - p, df=df):
                print(f"ACCEPT at {p : }% ; Kr = {Kr : ^6.5f} <= ChiSquared critical value = {chi2.ppf(q=1 - p, df=df) : ^7.5f} ; df = {df}")
            else:
                print(f"REJECT at {p : }% ; Kr = {Kr : ^6.5f} <= ChiSquared critical value = {chi2.ppf(q=1 - p, df=df) : ^7.5f} ; df = {df}")

        print("Each time the Kr value is lower than the ChiSquared critical value, we accept the null "
              "hypothesis\nWhich means that the decimals of e are uniformly distributed and so are random\n")

    def kolmogrovSmirnovTest(self):
        '''Generate a uniform distribution with the len of decimals'''

        uniformDistribution = np.random.uniform(0, 1, len(self.decimals))

        '''Perform the Kolmogrov-Smirnov test'''
        D, pValue = stats.kstest(self.decimals, uniformDistribution)

        print(f"Kolmogrov-Smirnov test : D = {D} and p-value = {pValue}")