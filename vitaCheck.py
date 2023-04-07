from datetime import date
import shelve
import pprint
import os

selectionDict = {
    1: 'Check supplement Status',
    2: 'Input supplement Status',
    3: 'Exit Program'
}

if os.path.exists('supplement.dat'):
    with shelve.open('supplement') as db:
        userDict = db['supplements']
        
else:
    supplement = 'blank'
    userDict = {
    
    }
    choice = ['y', 'n']
    while supplement != None:
        supplement = input('Add supplement (leave blank when finished): ').capitalize()
        if supplement == '':
            with shelve.open('supplement') as db:
                db['supplements'] = userDict

            break
        confirm = input(f"You want to add {supplement} to your list? (y/n): ").lower()
        while True:
            if confirm == 'y':
                userDict[supplement] = ''
                break
            elif confirm == 'n':
                break

def didYouTake(userDict:dict):
    today = str(date.today())
    for k in userDict.keys():
        while True:
            supplement = input(f'Did you take your {k} today (y/n): ').lower()
            if supplement == 'y':
                userDict.update({k:today})
                break
            while supplement == 'n':
                input(f'Go take your {k} right now!....')
                continue
            else:
                input('Please choose a valid input......')
                continue
    return userDict

choices = [0,1,2,3]
while True:
    try:
        print('                 What would you like to do?')
        
        for i in selectionDict.values():
            print(f"{num:>20}.{i}")
            num += 1
        
        num = 1
        choice = int(input('Selection: '))
        
        while choice == 1:
            os.system('cls')                
            for k,v in userDict.items():
                print(f"{k}: {v}")
            
            input("Return to main menu.....")
            os.system('cls')
            choice = 0

            
        while choice == 2:
            userDict = didYouTake(userDict=userDict)
            with shelve.open('supplement') as db:
                db['supplements'] = userDict
            choice = 0
            os.system('cls')
                
        while choice == 3:
            exit()
            
        if choice not in choices:
            input("Please choose a valid option....")
            os.system('cls')
            choice = 0
            continue
        
    except ValueError:
        input("Please choose a valid option....")
        os.system('cls')
        choice = 0
        continue