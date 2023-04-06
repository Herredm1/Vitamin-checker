from datetime import date
import shelve
import pprint
import os

selectionDict = {
    1: 'Check Vitamin Status',
    2: 'Input Vitamin Status',
    3: 'Exit Program'
}

userDict = {
    'Protien': '',
    'Vitamins': '',
    'Creatine': ''
}

def didYouTake(item:str, choice:int, userDict:dict):
    today = date.today()
    while True:
        subChoice = input(f'Did you take your {item} (y/n)?: ').lower()
        if subChoice == 'y':
            userDict.update({item:str(today)})
            with shelve.open('userData') as db:
                db[item] = userDict[item]
            
            choice += 0.1
            break
        elif choice == 'n':
            input(f"Go take your {item}")
    
    return item, choice, userDict
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
                userDict['Protien'] = db['Protien']
                userDict['Vitamins'] = db['Vitamins']
                userDict['Creatine'] = db['Creatine']
                
            for k,v in userDict.items():
                print(f"{k}: {v}")
            
            input("Return to main menu.....")
            choice =0
        else:
            pprint.pprint(userDict)
            choice = 0
            input("Return to main menu.....")
        
    while choice == 2:
        choice = 2.1
        while choice == 2.1:
            os.system('cls')
            item = 'Protien'
            item, choice, userDict = didYouTake(item=item, choice=choice, userDict=userDict) 
            
        while choice == 2.2:
            os.system('cls')
            item = 'Vitamins'
            item, choice, userDict = didYouTake(item=item, choice=choice, userDict=userDict) 
            
        while choice == 2.3000000000000003:
            os.system('cls')
            item = 'Creatine'
            item, choice, userDict = didYouTake(item=item, choice=choice, userDict=userDict)
            choice = 0 
            
        while choice == 3:
            exit()
        
    if choice not in [1,2,3]:
        input("Please choose a valid option....")
        choice = 0
        continue
