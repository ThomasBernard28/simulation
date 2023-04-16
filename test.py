import questionary

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
        ],
        'use_arrow_keys': True
    }
]


answer = questionary.prompt(mainMenu)

print('You chose: ', answer.get('Main Menu'))
