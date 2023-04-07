import datetime
import shelve
import os
import sys

selectionDict = {
    1: 'Check supplement Status',
    2: 'Input supplement Status',
    3: 'Exit Program'
}

if os.path.exists('supplement.dat'):
    with shelve.open('supplement') as db:
        user_dict = db['supplements']
else:
    user_dict = {}
    choice = ['y', 'n']
    while True:
        supplement = input('Add supplement (leave blank when finished): ').capitalize()
        if supplement == '':
            with shelve.open('supplement') as db:
                db['supplements'] = user_dict

            break
        confirm = input(f"You want to add {supplement} to your list? (y/n): ").lower()
        while True:
            if confirm == 'y':
                user_dict[supplement] = ''
                break
            elif confirm == 'n':
                break

def did_you_take(supplement_dict:dict):
    """_summary_

    Args:
        user_dict (dict): _description_

    Returns:
        _type_: _description_
    """
    today = str(datetime.date.today())
    for key in user_dict.keys():
        while True:
            supplement_add = input(f'Did you take your {key} today (y/n): ').lower()
            if supplement_add == 'y':
                supplement_dict.update({key:today})
                break
            elif supplement_add == 'n':
                input(f'Go take your {key} right now!....')
                continue
            else:
                input('Please choose a valid input......')
                continue
    return user_dict

choices = [0,1,2,3]
num = 1
while True:
    try:
        print('What would you like to do?')
        for i in selectionDict.values():
            print(f"{num:>20}.{i}")
            num += 1
        num = 1
        choice = int(input('Selection: '))
    except ValueError:
        input("Please choose a valid option....")
        os.system('cls')
        continue
    if choice == 1:
        os.system('cls')                
        for k,v in user_dict.items():
            print(f"{k}: {v}")  
        input("Return to main menu.....")
        os.system('cls')
    elif choice == 2:
        user_dict = did_you_take(supplement_dict=user_dict)
        with shelve.open('supplement') as db:
            db['supplements'] = user_dict
        os.system('cls')
    elif choice == 3:
        sys.exit()      
    elif choice not in choices:
        input("Please choose a valid option....")
        os.system('cls')
        continue