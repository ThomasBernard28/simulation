from PyInquirer import prompt, Separator
from tabulate import tabulate

from code.EDecimals import *

mainMenu = [
    {
        'type': 'list',
        'name': 'Main Menu',
        'message': 'Welcome to the Simulation project.\nWhat would you like to do?',
        'choices': [
            'Get basic information on e decimals',
            'Information on the pseudo-randomness of e decimals',
            'Generation of uniform distribution with e decimals',
            'Exit'
        ]
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

leaveMenu = [
    {
        'type': 'confirm',
        'name': 'Leave',
        'message': 'Do you want to leave?',
        'default': True
    }
]


def main():
    answer1 = prompt(mainMenu)

    if answer1.get("Main Menu") == 'Get basic information on e decimals':
        # TODO
        print("TODO")

    elif answer1.get("Main Menu") == 'Information on the pseudo-randomness of e decimals':
        # TODO
        print("TODO")

    elif answer1.get("Main Menu") == 'Generation of uniform distribution with e decimals':
        # TODO
        print("TODO")

    elif answer1.get("Main Menu") == 'Exit':
        answer2 = prompt(leaveMenu)
        if answer2.get("yes"):
            return 0
        else:
            return 1


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        e = EDecimals(sys.argv[1])
        decimals = e.decimals
    else:
        print("Please choose a file to exploit by giving it as argument")
        sys.exit(1)
    a = 1
    while a != 0:
        a = main()
        if a != 0:
            answer = prompt(confirmMenu)
            if not answer.get("Continue"):
                a = 0
