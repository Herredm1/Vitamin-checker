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
        userDict = db
        
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


print(userDict)
def didYouTake(userDict:dict):
    today = date.today()
    supplementList = 0
    while supplementList != len(userDict):
        for k in userDict.keys():
            while True:
                supplement = input(f'Did you take your {k} today (y/n): ').lower()
                if supplement == 'y':
                    userDict.update({k:today})
                    supplementList += 1
                    break
                elif supplement == 'n':
                    input(f'Go take your {k} right now!....')
                    continue
                
        return userDict
num = 1
choice = 0
while choice == 0:
    print('                 What would you like to do?')
    
    for i in selectionDict.values():
        print(f"{num:>20}.{i}")
        num += 1
    
    num = 1
    choice = int(input('Selection: '))
    
    while choice == 1:
        os.system('cls')
        if os.path.exists('userData.dat'):
            with shelve.open('userData') as db:
                userDict = db
                
            for k,v in userDict.items():
                print(f"{k}: {v}")
            
            input("Return to main menu.....")
            choice =0
        else:
            pprint.pprint(userDict)
            choice = 0
            input("Return to main menu.....")
        
    while choice == 2:
        userDict = didYouTake(userDict=userDict)
        with shelve.open('supplement') as db:
            db = userDict
            
        while choice == 3:
            exit()
        
    if choice not in [1,2,3]:
        input("Please choose a valid option....")
        choice = 0
        continue
