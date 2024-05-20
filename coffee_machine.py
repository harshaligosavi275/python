from coffee_machine_database import menu

# -------------------------------------------------------------------------------------------------------------------------------
report = {
       "water":500,
       "milk":250,
       "coffee":500,
       "money":0
}
# -------------------------------------------------------------------------------------------------------------------------
def check_resources(coffee_chosen):
    
        if(menu[coffee_chosen]["Ingredients"]["water"] <= report["water"]):
             if(menu[coffee_chosen]["Ingredients"]["milk"] <= report["milk"]):
                 if(menu[coffee_chosen]["Ingredients"]["coffee"] <= report["coffee"]):
                       return True
                 else:
                     print("Sorry 🥺 there is not enough  🥔🥔")
                     return False
             else:
                 print("Sorry 🥺 there is not enough  🥛")
                 return False
        else:
            print("Sorry 🥺 there is not enough  💧")
            return False     
        
# -----------------------------------------------------------------------------------------------------------------------
change = 0
total = 0
def get_coffee(coffee_chosen):
    
    print("\nPlease Insert Coins....💲💲")
    five_coin = int(input("How many 5rs Coin?: "))
    ten_coin = int(input("How many 10rs Coin?: "))
    twenty_coin = int(input("How many 20rs Coin?: "))
    
    total = five_coin*5 + ten_coin*10 + twenty_coin*20
    
    if(menu[coffee_chosen]["cost"] == total):
        total=total+report["money"]
        print(f"\nHere is your ☕ {coffee_chosen} ☕.....Enjoy!😃 😃")
        
    elif(menu[coffee_chosen]["cost"] > total):
        return "\nSorry that's not enough money❌. Money refunded.💰 💸  💰 💸"
    else:
        change = total - menu[coffee_chosen]["cost"]
        total = (report["money"]-change)+total
        print(f"\nHere is your Rs{change} in change.\nHere is your ☕ {coffee_chosen} ☕.....Enjoy!😃 😃")
    
    # report updated
    report["money"]=total
    report["water"] = report["water"]-menu[coffee_chosen]["Ingredients"]["water"]
    report["milk"] = report["milk"]-menu[coffee_chosen]["Ingredients"]["milk"]
    report["coffee"] = report["coffee"]-menu[coffee_chosen]["Ingredients"]["coffee"]

# --------------------------------------------------------------------------------------------------------------

on = True
while(on):
    print("\n\t\t\tWELCOME, FRIEND.....\n")
    choice = input("What would you like to have? 👉 (latte/espresso/cappuccino)☕ :- ") 
    if(choice == "report"):
        
        print(f'\t\t\tWater = {report["water"]}ml\n\t\t\tMilk = {report["milk"]}ml\n\t\t\tCoffee = {report["coffee"]}g\n\t\t\tMoney = Rs.{report["money"]}') 
          
    elif(choice == "latte" or choice=="espresso" or choice=="cappuccino"):
       print(menu[choice])
       is_resource_available =  check_resources(choice)  
       if(is_resource_available):
           print(get_coffee(choice))
       else:
           continue          
    elif(choice == "off"):
         print("Thank You!!")
         on=False
    
