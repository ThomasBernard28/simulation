import sys
import re
from collections import Counter

import numpy as np
from scipy.stats import chi2
from scipy.stats import ksone

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
        plt.xlabel("Décimales")
        plt.ylabel("Fréquences")
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

        plt.figure()
        plt.bar(np.arange(10) - 0.2, observedFrequencies, width=0.4, color="red", label="Observed frequencies")
        plt.bar(np.arange(10) + 0.2, expectedFrequencies, width=0.4, color="blue",label="Expected frequencies")
        plt.title("Comparison between observed and expected frequencies")
        plt.xlabel("Digits")
        plt.ylabel("Frequencies")
        plt.legend(loc="lower right")
        plt.savefig("eDecimalsChi2.png")
        plt.show()

    def stirlingNbr(self, r, k):
        """
        Compute the Stirling number of the second kind. The formula is given in the course.
        """
        if k == 0 or k > r:
            return 0
        elif k == 1 or k == r:
            return 1
        else:
            return self.stirlingNbr(r - 1, k - 1) + k * self.stirlingNbr(r - 1, k)

    def pokerProb(self, r, k, d):
        """
        Compute the probability of having r different values in a packet of size k
        where each value can be between 0 and d-1. Here d = 10 because we are working
        with decimals. The formula is given in the course. I use np.prod to compute
        the product of all the values between d and d-r+1
        """
        if r > d:
            raise ValueError("r must be lower than d")

        return self.stirlingNbr(k, r) * np.prod([d-i for i in range(r)]) /(d ** k)

    def evaluatePokerHand(self, packet, nbrOfDifferentValues):
        """
        We will count the number of different values in a packet and increment the
        corresponding value in nbrOfDifferentValues
        """
        # We use a set to count the number of different values in a packet
        s = set()
        for value in packet:
            s.add(value)
        nbrOfDifferentValues[len(s)-1] += 1

    def pokerTest(self, nbrOfIntervals, sizeOfPacket):

        # We split the decimals into packets of size sizeOfPacket
        packets = [self.decimals[i:i+sizeOfPacket] for i in range(0, len(self.decimals), sizeOfPacket)]

        # Once we've done that we can compute the number of different values in each packet
        nbrOfDifferentValues = [0] * 5
        for packet in packets:
            self.evaluatePokerHand(packet, nbrOfDifferentValues)

        # We compute the expected number of different values in a packet
        expectedNbrOfDifferentValues = [0] * 5
        # We compute the expected probability of having r sets of different
        # values in a packet. Ex : if the packet is 55555, we have 1 set
        expectedProbability = [0] * 5
        for i in range(5):
            expectedProbability[i] = self.pokerProb(i+1, sizeOfPacket, 10)

        # We have 2M decimals so we have 2M/sizeOfPacket packets i.e we have
        # 400k packets. So now we can compute the expected number of sets
        # of different values in a packet
        for i in range(5):
            expectedNbrOfDifferentValues[i] = int(400000 * expectedProbability[i])

        absoluteError = [abs(nbrOfDifferentValues[i] - expectedNbrOfDifferentValues[i]) for i in range(5)]
        percentageError = [absoluteError[i] / expectedNbrOfDifferentValues[i] for i in range(5)]

        print(f"Observed number of different values in a packet : {nbrOfDifferentValues}")
        print(f"Expected number of different values in a packet : {expectedNbrOfDifferentValues}")
        print(f"Absolute error : {absoluteError}")


        xline = np.arange(1, 6)
        plt.title(f"Comparaison des fréquences observées et \nthéoriques pour des paquets de taille {sizeOfPacket}")
        plt.xlabel("Nombre de valeurs différentes par paquet")
        plt.ylabel("Fréquences")
        plt.bar(xline - 0.2, nbrOfDifferentValues, width=0.4, color="red", label="Fréquences observées")
        plt.bar(xline + 0.2, expectedNbrOfDifferentValues, width=0.4, color="blue", label="Fréquences théoriques")
        plt.legend()
        plt.show()
        plt.savefig(f"eDecimalsPoker{sizeOfPacket}.png")



        # Then we split each packet into intervals of size nbrOfIntervals