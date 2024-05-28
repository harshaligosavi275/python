from Car_operations import *


print("🚗 🚗 🚗 🚗 🚗 🚗  Car Management System  🚗 🚗 🚗 🚗 🚗 🚗")
continueLoop=True
while(continueLoop):
      print('Enter 1 for add car details\nEnter 2 for update car details\nEnter 3 for remove car details\nEnter 4 for get all car details\nEnter 5 for Exit')
      select_option = int(input("Select option from above 📃: "))
      
      match select_option:
             case 1:
                   # add car details
               id = input("Enter car id: ")
               name = input("Enter car name: ")
               color = input("Enter car color: ")
               brand = input("Enter brand of car: ")
               fuel_type = input("Enter fuel type of car: ")
               price = int(input("Enter price of car: "))
               insert(id,name,color,brand,fuel_type,price)
               print("🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗")
             case 2:
                 # update car details
                id = int(input("Enter Car Id that you want to update: "))
                update(id)
                print("🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗")
             case 3:
                 # remove car details
                id = int(input("Enter Car Id that you want to delete: "))
                remove(id)
                print("🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗")
             case 4:
                 # get all car details
                getAllDetails()
                print("🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗")
             case 5:
                  print("Thank You!")
                  print("🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗")
                  continueLoop = False
        

