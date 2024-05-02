#a program to define the functions and classes of the online car store.
import csv #import the csv module
import random #import the random module

# create a class car
class car:
    #a function to view the car store status
    def view_status(self):

        with open('data.csv','r') as data1: #open the csv file in read mode
            items = data1.readlines() #read all the data in the csv files and stores it in a list
            print('Current car store Status:\n')

            for item in items: #loop through the items in the list
                print(item)

    # a function to add a car to the store
    def add_car(self):

        with open('data.csv','r') as data3: #open the file in read-mode
            cars = csv.reader(data3) #use csv reader to read file
            car1,prices,quantity = [],[],[] #to store the different data in the csv file in another lists
            for x,y,z in cars: #loop through items in the cars
                car1.append(x) #add cars  to the car1 list
                prices.append(y) #add prices to the prices list
                quantity.append(z) #add quantity to the quantity list

            new_car = input('\nEnter a new car: ').strip().lower() #user enters a new car
            new_price = input('Enter a price per car: ').strip() #user enters a new price

            if new_car in car1:  #check if the new car is in list of cars
                if new_price in prices: #check if new price is in list of prices
                    print('This Car already exists, Kindly update the quantity')

            else: #if new car is not in the var1 list.
                new_quantity = input('Enter a quantity: ').strip() #user enter quantity

                while new_quantity.isnumeric() is False: #if quantity is not a numeric value
                    new_quantity = input('Enter a numeric value: ').strip()#user has to enter a numeric value
                    #continues looping still user enters a numeric value

                with open('data.csv', 'a') as data2: #open the file in the append mode
                    data2.write(f'{new_car},{new_price},{new_quantity}\n') #write these variables to the file
                print(f'\nA new car {new_car} has been added to the store successfully.\n')

    #a function to remove a car from the store
    def remove_car(self):

        with open('data.csv','r') as data3: #open the file in read-mode
            cars = csv.reader(data3) #use csv reader to read file
            car1, prices, quantity = [],[],[] #to store different data in the csv files in an empty lists
            for x,y,z in cars: #loop through items in the cars
                car1.append(x) #add cars to car1 list
                prices.append(y) #adds prices to the prices list
                quantity.append(z) #adds quantity to the quantity list
            print('\nHere are the available cars:')

            for car_item in car1: #loop through the cars in car1
                if 'cars' not in car_item: #exclude the word cars
                    print(car_item) #print the remaining cars

            #user enter the car the use to remove
            item = input('\nEnter the car you will like to remove: ').lower().strip() #convert it to lowercase and remove whitespaces
            while item not in car1: #if the item is not amonng the cars in the list
                item = input('Enter the available cars: ').lower().strip() #user will enter the available car
                #continue looping still user enter the available cars
            index1 = car1.index(item) #get the index of the car the user enters
            Save = int(quantity[index1]) #get the index of the quantity the user enters
            #ask the user if they will remove a specific quantity or not

            question = input('Will you like to remove a specific quantity? (Y or N) ').lower().strip()
            while question not in  ['y','n']: #if the user doesn't enters y or n
               question = input('Please Enter either Y or N: ').strip().lower()
                #continue looping still the user enters y or n

            if question == 'y': #if user enters y
                print(f'{Save} {item} cars are available')
                #user enters the quantity the want to remove
                remove_quantity = input('Enter the quantity you want to remove: ').strip()
                while remove_quantity.isnumeric() is False: #if the remove quantity is not a number
                    remove_quantity = input('Enter a numeric value: ').strip() #removes all the white spaces
                #continue looping still user enters a numeric value
                result = Save - int(remove_quantity) #original quantity - removed quantity

                #if result is 0, remove everything
                if result == 0:
                    car1.pop(index1) #remove the index of the car the user entered
                    prices.pop(index1) #remove the prices of the car the user entered
                    quantity.pop(index1) #remove the quantity of the car the user entered
                    #no car the user entered are avialble now
                    print(f'\nno {item} cars are available now.')

                elif result <0:
                    #if result if less than 0
                    #user has to enter a number lesser than the origianl quantity(save) in the remove quantity
                    remove_quantity = input(f'Only {Save} {item} car(s) available.\nEnter a number lesser than {Save + 1}: ').strip()
                    #if the user enters an alphabet or number lesser than the original quantity(save)
                    while not remove_quantity.isdigit() or Save < int(remove_quantity):
                        remove_quantity = input(f'Enter a numeric value lesser than {Save + 1} :').strip()
                        #continues loop still user enters a lesser number
                    result = Save - int(remove_quantity) #origianl quantity - removed quantity
                    quantity[index1] = result #result put in the index of the car user enters, quantity section
                    #the remaing quantity of the car the user entered are available now.
                    print(f'\n{result} {item} car(s) are available now.')

                else: #if result >0
                    quantity[index1] = result #result put in the index of the car user enters, quantity section
                    print(f'\n{result} {item} car(s) are available now.')

                #after check all the conditions for result
                with open('data.csv', 'w') as data4: #open the csv file in write mode
                    for i in range(len(car1)): #loop through the range of the len of the car1
                        #write the 1st index for car1,prices, quantity, then move to the second index still you are done
                        data4.write(f'{car1[i]},{prices[i]},{quantity[i]}\n') #write these variables to the file
                #the remove quantity of the car the user entered has been removed successfully
                print(f'\n{remove_quantity} {item} car(s) has been removed from the store successfully\n')

            elif question == 'n': #if user enters n, remove everything
                car1.pop(index1) #remove the index of the car the user entered
                prices.pop(index1) #remove the price of the car the user entered
                quantity.pop(index1) #remove the quantity of the car the user entered

                with open('data.csv', 'w') as data4: #open the file in write mode
                    for i in range(len(car1)): #loop through the range of the len of the car1
                        # write the 1st index for car1,prices, quantity, then move to the second index still you are done
                        data4.write(f'{car1[i]},{prices[i]},{quantity[i]}\n')  #write these variables to the file
                #the car the user entered has been removed sucessfully
                print(f'\n{item} car(s) has been removed from the store successfully\n')
                print(f'No {item} cars are available now') #the car the user enetered is not available

            else:
                print('Please either Y or N \n')

    #a function to update the prices and quantity
    def update(self):

        with open('data.csv','r') as data3: #open the file in read-mode
            cars = csv.reader(data3) #use csv reader to read file
            car1, prices, quantity = [],[],[] #to store the different variables in another lists

            for x,y,z in cars: #loop through ittems in the cars
                car1.append(x) #add cars to car1 list
                prices.append(y) #add prices to prices list
                quantity.append(z) #add quantity to quantity list
            print('Here are the available Cars:')

            for car_item in car1: #loop through the cars in car1
                if 'cars' not in car_item: #remove the first index car
                    print(car_item) #print the remaining cars

            #user enters the car they will like to update
            car = input('\nEnter the car you will like to update: ').lower().strip()
            while car not in car1: #if the user car is not amng the cars in the list car1
                #user have to enter the available cars
                car = input('Enter the available Cars: ').lower().strip()
                #continue loop still user enters the available cars
            index2 = car1.index(car) #get the index of the car the user enters
            #print the original quantity of the user input car, and the original price
            print(f'{quantity[index2]} {car} cars available, {prices[index2]} per car')

            #user will enter the quantity the want to update to
            quantity1 = input('Enter the quantity you will like to update to: ').strip() #remove all whitespaces
            while quantity1.isnumeric() is False: #when the quantity is not a numeric value
                quantity1 = input('Enter a numeric value: ') #user has to enters a numeric value
                #continue looping still user enters a numeric value
            #user enters the price the want to update to
            price = input('Enter the price per car you want to update: ').strip() #remove all the whitespaces
            quantity[index2] = quantity1 #the quantity of the car the user wants to update to is replaced in the original quantity
            prices[index2] = price #the price the user wants to update to is replaced in the original price

        with open('data.csv','w') as data4: #open the filein the write mode
           for i in range(len(car1)): #loop through the range of the len of the car in the list car1
               # write the 1st index for car1,prices, quantity, then move to the second index still you are done
               data4.write(f'{car1[i]},{prices[i]},{quantity[i]}\n') #write these variable to the file
        print(f'\n{car} car has been updated successfully\n') #the car the user enetered has been updated successfully

    #a function to login
    def login1(self):
        with open('login.csv','r') as info1: #open the login csv file in read mode
            info2 = csv.reader(info1) #use the csv reader to read the file
            users, passwords = [],[] #create an empty list to store the user names and passwords
            for x,y in info2: #loop through the data in the login.csv file
                users.append(x) #add username to list users
                passwords.append(y) #add the passwords to the list 
            user_login = input('Enter your username: ').strip()
            password_login = input('Enter you password: ').strip()
            while user_login not in users:
                user_login = input('Incorrect user name: ')
            while password_login not in passwords:
                password_login = input('Incorrect Password: ')
            print('\nLogin Successful.')

    def register1(self):
        user_name = input('Enter a user name: ')
        password = input('Enter a password: ')
        while len(password) < 8 or not any(char.isdigit() for char in password):
            password = input('Paasword must be more than 7 characters and must have at least one numeric value: ')
        with open('login.csv','r+') as info3:
            x = csv.reader(info3)
            names = []
            for name, passwords in x:
                names.append(name)
            while  user_name in names:
                user_name = input('This user name already exists. Enter another user name: ')
            info3.write(f'\n{user_name},{password}')
        print('\nYou have Successfully created an account.')

# A list of driving tips for the user when they are done with the operations
Driving_tips = [
'No drinking while driving.','Always use your seat belt.', 'Everything in life is somewhere else,and you get there in a car.',
'Take care of your car in the garage,and the car will take care of you on the road.','The cars we drive says alot about us.',
'Drive slow and enjoy the scenery, drive fast and join the scenery.','Normal speed meets every need',
'Sometimes the best therapy is a long drive and music.','Keep calm and drive safely.',
'Driving is not my hobby it\'s my feelings!','we aren\'t addicted to oil, but our cars are!','Driving is love!'
            ]

# A class to perform another operation
#inheritng the Class car
class another_operation(car):
    def operation(self): # a function to perform another operation

        continue1 = True #define a variable to contain the boolean True

        #Do while loop
        #while the user keep entering yes, it will keep running
        while continue1: #While True
            #ask the user if they will like to perform another operation
            input1 = input('\nWill you like to perform another operation? Yes or No:\n').strip().lower() #conver to lowercase and remove white spaces

            # if the user enters yes
            if input1 == 'yes':

                #the try to avoid the program from breaking if the is an exception
                try:
                    #user enters any of the operations the will like to perform
                    operation = input('\nEnter any of the operations you will like to perform below:\n\n'
                                          '1. Add a new car to the store\n'
                                          '2. Remove a car from the store\n'
                                          '3. Update the car prices and quantity\n'
                                          '4. View the current car store status\n\n').strip()

                    #when the operation is not a number or the interger of the operation is not in the numbers 1,2,3,4
                    while not operation.isdigit() or int(operation) not in range(1, 5):
                        #continue looping still user enters the above operations
                        operation = input('\nEnter the operations above:\n')

                        #when the user enters the above operations
                    #the integer of the operation is store in the variable choice
                    choice = int(operation)
                    #check for the following conditions
                    if choice == 1: #if user enters 1
                        car.add_car('self') #perform the add car function

                    elif choice == 2: #if user enters 2
                        car.remove_car('self') #perform the remove car function

                    elif choice == 3: #if user enters 3
                        car.update('self') #perform the update car function

                    elif choice == 4: #if user enters 4
                        car.view_status('self') #perform the view car staus operation

                    else:
                        print('invalid inpput')

                except Exception:
                    print('Invalid input, Enter the correct value.')

            #when the user enters no
            elif input1 == 'no':
                #shuffle through the driving tips using random module
                random.shuffle(Driving_tips)
                for x in Driving_tips: #loop through the driving tips
                    pass
                #print any random tips from the driving tips..
                print(f'Hope we attended to your request effectively, any issues please contact us.\nAlways remember:\n{x} Have a nice day!')
                continue1 = False #ends the program completely, exist the program

            else: #if the user does not enter yes or no
                print('Invalid input please enter yes or no ')
                #go back to input 1 still user enters yes or no
















