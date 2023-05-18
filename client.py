import os

import questionary
from Code.EDecimals import *

mainMenu = [
    {
    'type': 'list',
    'name': 'Main Menu',
    'message': '------ Welcome to the Simulation project. ------\nWhat would you like to do?',
    'choices': [
        'Get basic information on e decimals',
        'Information on the pseudo-randomness of e decimals',
        'Generation of uniform distribution with e decimals',
        'Exit'
    ],
    'use_arrow_keys': True
    }
]

testMenu = [
    {
    'type': 'list',
    'name': 'Test Menu',
    'message': 'Which test do you want to use ?',
    'choices': [
        'Chi-Squared test',
        'Poker Test',
    ],
    'use_arrow_keys': True
    }
]

generatorMenu = [
    {
    'type': 'list',
    'name': 'Generator Menu',
    'message': 'Do you want to generate and test or compare with Python ?',
    'choices': [
        'Generate and Test',
        'Compare',
    ],
    'use_arrow_keys': True
    }
]

confirmMenu = [
    {
    'type': 'confirm',
    'name': 'Continue',
    'message': 'Do you want to continue?',
    'default': True
    }
]

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    answer1 = questionary.prompt(mainMenu)
    if answer1.get("Main Menu") == 'Get basic information on e decimals':
        EDecimals.displayInformation(e)

    elif answer1.get("Main Menu") == 'Information on the pseudo-randomness of e decimals':
        answer2 = questionary.prompt(testMenu)
        if answer2.get("Test Menu") == 'Chi-Squared test':
            obs, exp = EDecimals.chiSquaredTest(e, e.decimals)
            EDecimals.plotChiSquared(e, obs, exp)


        elif answer2.get("Test Menu") == 'Poker Test':
            obs, exp = EDecimals.pokerTest(e, e.decimals, 10, 5)
            EDecimals.plotPoker(e, obs, exp)

    elif answer1.get("Main Menu") == 'Generation of uniform distribution with e decimals':
        answer3 = questionary.prompt(generatorMenu)
        if answer3.get("Generator Menu") == 'Generate and Test':
            """
            print("----- Basic Generator -----")
            BFreq = EDecimals.basicGenerator(e, 2000000)
            print("Chi-Squared Test :")
            EDecimals.chiSquaredTest(e, BFreq)
            print("Poker Test validated by the Chi-Squared Test:")
            EDecimals.pokerTest(e, BFreq, 10, 5)
            """
            print("----- LCG Generator -----")
            LCGfrequencies = EDecimals.linearCongruentialGenerator(e, 2000000)
            print("Chi-Squared Test :")
            obs, exp = EDecimals.chiSquaredTest(e, LCGfrequencies)
            EDecimals.plotChiSquared(e, obs, exp, gen=True)
            print("Poker Test validated by the Chi-Squared Test:")
            obs, exp = EDecimals.pokerTest(e, LCGfrequencies, 10, 5)
            EDecimals.plotPoker(e, obs, exp)


        elif answer3.get("Generator Menu") == 'Compare':
            LCGfrequencies = EDecimals.linearCongruentialGenerator(e, 2000000)
            obsLCG, expLCG = EDecimals.chiSquaredTest(e, LCGfrequencies)
            obsLCGPoker, expLCGPoker = EDecimals.pokerTest(e, LCGfrequencies, 10, 5)

            python = EDecimals.compareWithPython(e, 2000000)
            print("Chi-Squared Test :")
            obs, exp = EDecimals.chiSquaredTest(e, python)
            EDecimals.plotChiSquared(e, obs, exp, obsLCG, gen=True)
            print("Poker Test validated by the Chi-Squared Test:")
            obs, exp = EDecimals.pokerTest(e, python, 10, 5)
            EDecimals.plotPoker(e, obs, exp, obsLCGPoker)

    elif answer1.get("Main Menu") == 'Exit':
        print("Goodbye !")
        return 0

if __name__ == '__main__':
    import sys
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(sys.argv) == 2:
        e = EDecimals(sys.argv[1])
        decimals = e.decimals
    else :
        print("Please choose a file to exploit by giving it as argument")
        sys.exit(1)
    a = 1
    while a != 0:
        a = main()
        if a != 0:
            answer = questionary.prompt(confirmMenu)
            if not answer.get("Continue"):
                a = 0