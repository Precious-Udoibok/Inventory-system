#a program for an online car store
from inventory import car,another_operation #import the module inventory, import the class car and another operation

print('\nWelcome to Preshy online Car Store!\n')
info = input('Will you like to create a new account or login:\n1. Login\n2. Create a new Account\n\n')
while not info.isdigit() or int(info) not in range(1,3):
    info = input('Enter either 1 or 2: ')
int_info = int(info)
if int_info == 1:
    car.login1('self')
elif int_info == 2:
    car.register1('self')

#operations to be performed in the store
try: #this try block is inside the csv file is empty so that the program won,t crash or break.
    print('\nSelect the operations you will like to perform below:')
    operations = input('''
        1. Add a new car to the store
        2. Remove a car from the store
        3. Update the car prices and quantity
        4. View the current car store status\n
    ''') #user enters any of the operations above

    #if the operation is not a number or the integer of the operation is not 1,2,3 or 4
    while not operations.isdigit() or int(operations) not in range(1,5):
        operations = input('\nEnter the operations above:\n')
        #user has to enter the operation above

    #when the user enters the operations above
    #the integer of the operation is store in a variable choice
    choice = int(operations)

    #check for the following conditions
    if choice == 4: #if user enters 4
        car.view_status('self') #view the car status
        another_operation.operation('self') #perform another operation

    #1.add a car to the store
    elif choice == 1: #if user enters 1
        #calling the class car and the function add car
        car.add_car('self') #add car to the store
        #calling the class another operation and the function operation
        another_operation.operation('self') #perform another operation

    #2.Remove a car from the store
    elif choice == 2: #if the user enters 2
        car.remove_car('self') #remove a car from the store
        another_operation.operation('self') #perform aother operation

    #3.update a car in the store
    elif choice == 3: #if the user enters 3
        car.update('self') #update a car from the store
        another_operation.operation('self') #perform another operation

except UnboundLocalError: #except an exception, if the csv file is empty, or any other thing
    print('Opps! the is a little problem\nwe apologize for any inconvenience caused. please try again later.')