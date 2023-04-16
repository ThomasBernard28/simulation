import questionary

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

confirmMenu = [
    {
    'type': 'confirm',
    'name': 'Continue',
    'message': 'Do you want to continue?',
    'default': True
    }
]

def main():
    answer1 = questionary.prompt(mainMenu)
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
        return 0


if __name__ == '__main__':
    a = 1
    a = main()
    if a != 0:
        answer = questionary.prompt(confirmMenu)
        if not answer.get("Continue"):
            a = 0