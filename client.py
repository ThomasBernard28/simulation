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
        'Kolmogorov-Smirnov test',
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
            EDecimals.chiSquaredTest(e)
        elif answer2.get("Test Menu") == 'Kolmogorov-Smirnov test':
            print("TODO")

    elif answer1.get("Main Menu") == 'Generation of uniform distribution with e decimals':
        # TODO
        print("TODO")

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