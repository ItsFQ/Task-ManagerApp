'''
*Problem Description*

The aim of the program is to help the user manage their daily tasks and store these tasks in a simple 
and straightforward manner through the use of a text file. The use of the text file also 
allows for users to rerun the program, without losing the items on their Todo List from the previous run.

The program gives users the option of adding, displaying, editing, removing or clearing ToDo items 
through the use of item numbers that uniquely identify each item.

Functionalities:

- Add an Item Option:
Users will be able to input what item they would like to add to their Todo List.

- Show all Items Option:
Users will be able to view all their items on their Todo List.

- Edit an Item Option:
Users are able to enter in the item number they would like to edit, and their Todo List 
would be updated to reflect that change.

- Remove an Item Option:
Users are able to enter in the item number they would like to remove, and that item would be removed from 
their list.

- Clear Items Option:
Users can reset their Todo List by emptying it out.
'''

# To import all the needed modules for the program
import os.path,time, sys

# To check if saveItems.txt exsits in directory
if(os.path.isfile('saveItems.txt') == False):
    file = open('saveItems.txt','w') 
    file.close()
    
###################

# A function to create a cool typing effect for a passed in string
def typingPrint(text):
  for letter in text:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)

# A function to add a ToDo Item 
def addItem():
    
    # To get from the user and add an item to the itemsList
    todo = input('Enter an item: ') + '\n'
    itemsList.append(todo)
    
    # To update the txt file to reflect the new items added to the itemsList
    with open('saveItems.txt', 'w') as file:
        file.writelines(itemsList)
    
    typingPrint("\nThis item is being added to your list...")
    time.sleep(3)
    typingPrint("\nSuccefully added!\n")
        
# A function to Show All ToDo Items 
def showItems():
    
    # To check if the itemsList is empty
    if(not itemsList):
        print("There are no items in the ToDo List :( ")
    else:
        typingPrint('Here is your list:\n')
        time.sleep(1)
        
        # To print each item from the itemsList to the user
        for index, item in enumerate(itemsList):
            item =  item.title()
            item = item.strip("\n")
            print(f"{index+1}. {item}")

# A function to Edit a ToDo Item
def editItem():
    
    # A try and except to make sure the input is an integer
    try:
        # To check if the itemsList is empty
        if(not itemsList):
            print("There is nothing to edit...")
        
        else:
            editNum = int(input('Enter the number of the item to edit: '))
            
            # To check if the item number actually exsits 
            if(editNum <= len(itemsList) and editNum > 0):
            
                newItem = input('Please type the new item: ')
                
                # To replace the old item with the new one
                itemsList.__setitem__(editNum-1, newItem + '\n')
                
                
                # To update the txt file with the updated list
                with open('saveItems.txt', 'w') as file:
                    file.writelines(itemsList)
                    
                typingPrint(f"\nItem No. {editNum} is being edited...")
                time.sleep(3)
                typingPrint("\nSuccefully edited!\n")
                
            else:
                print('The item number entered is not valid!')
            
    except (ValueError):
        print('Not a valid input...')
        
# A Function to Remove a ToDo Item
def removeItem():
    
    # Try and except to catch if the input is an integer
    try:
        # To check if the itemsList is empty
        if(not itemsList):
            print("There is nothing to mark as complete or remove...")
        
        else:
            removeNum = int(input('Enter the number of the item to remove/mark as complete: '))
            
            # To check if the item number really exsits 
            if(removeNum <= len(itemsList) and removeNum > 0):
                
                # To remove an item from the list
                itemsList.pop(removeNum-1)
                
                # To update the txt file to reflect the updated list.
                with open('saveItems.txt', 'w') as file:
                    file.writelines(itemsList)
                
                typingPrint(f"\nItem No. {removeNum} is being removed...")
                time.sleep(3)
                typingPrint("\nSuccefully removed!\n")
                
            else:
                print('The item number entered is not valid!')
            
    except ValueError:
        print('Not a valid input...')

# A Function to Clear Items
def clearItems():
    
    # To check if the file is already empty
    if(os.path.getsize('saveItems.txt') == 0):
        print("\nThe list is already empty.")
        time.sleep(2)
    else:
        # To overwrite the current file and make it empty
        open("saveItems.txt", "w").close()
        
        
        typingPrint("The list is being cleared...")
        time.sleep(3)
        typingPrint("\nSuccefully cleared!\n")

#############################

userInput = ""

while True:
    
    # To make sure the itemsList matches the text file before an action
    with open('saveItems.txt', 'r') as file:
        itemsList = file.readlines()
    
    # Intro; To ask user what action to do
    print("")
    print("\u001b[34;1m" + '=============')
    print('What action would you like to do?\n')
    print('1. 📝 Add an item\n2. 👀 Show all items\n3. 🔍 Edit an item \n4. ❌ Remove or mark a task as complete\n5. 📄 Clear List\n6. 🚪 Exit')
    print( '=============\n')
    userInput = (input('Enter your choice by number: ')).strip()
    
    
    # To call the add item function
    if(userInput == '1'):
        print("")
        addItem()
        
    # To call the show items function
    elif(userInput == '2'):
        print("")
        showItems()
        time.sleep(2)
            
    # To call the edit items function
    elif(userInput == '3'):
        print("")
        editItem()
        time.sleep(2)
    
    # To call the remove item function
    elif(userInput == '4'):
        print("")
        removeItem()
        time.sleep(2)
    
    # To call the clear items function
    elif(userInput == '5'):
        clearItems()
    
    # To exit the program
    elif(userInput == '6'):
        break
    
    # Invalid Input Case
    else:
        print('You have entered an invalid input!')

# Ending Message
print('\u001b[32;1mBye! 😊')




            


