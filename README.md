
# Vitamin and Protein Intake Tracker
This Python program allows the user to track their vitamin and protein intake. It makes use of the date, shelve, pprint, and os modules.

## Dictionary Definitions
The program defines two dictionaries:
 * selectionDict 
 * userDict.

## selectionDict
selectionDict contains options for the user to choose from. The keys are integers, and the values are strings representing the options.

``` python
selectionDict = {
    1: 'Check Vitamin Status',
    2: 'Input Vitamin Status',
    3: 'Exit Program'
}
```
## userDict

userDict contains the user's vitamin and protein intake. The keys are strings representing the items, and the values are strings representing the dates the items were taken.

``` python
userDict = {
    'Protien': '',
    'Vitamins': '',
    'Creatine': ''
}
```

## Function Definitions
The program defines a function didYouTake that prompts the user if they have taken a certain item, and if they have, updates the userDict with the current date. It also stores the userDict in a shelve database.

``` python
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
```

## Main Program
The program runs in a while loop that presents the user with the options from selectionDict and prompts the user to select an option.

``` python
num = 1
choice = 0
while choice == 0:
    print('                 What would you like to do?')
    
    for i in selectionDict.values():
        print(f"{num:>20}.{i}")
        num += 1
    
    num = 1
    choice = int(input('Selection: '))
```

If the user selects "Check Vitamin Status", it retrieves the user's intake from the database and prints it.

``` python

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
```

If the user selects "Input Vitamin Status", it prompts the user to enter whether they have taken each item and updates the userDict.

``` python

while choice == 2:
    choice = 2.1
    while choice == 2.1:
        os.system('cls')
        item = 'Protien'
        item, choice, userDict = didYouTake(item=item, choice=choice, userDict=userDict) 
            
    while choice == 2.2:
        os.system('cls')
        item
```