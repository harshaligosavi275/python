menu = {
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffee":80
}
# Greet
print("Welcome to our restaurant, Here's the Menu:")
# Menu list
print(f"Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

price = 0
orderNow = "yes"
while orderNow =="yes":
    order = input("Enter item that you want to order = ")
    if order in menu:
          print(f'Order of {order} has been added.')
          price = price + menu[order]
        #   orderNow = input("Do you want to order anything else?(yes/no)") 
           
    else:
          print(f'Sorry order is not available.') 
        #   orderNow = input("Do you want to order anything else? (yes/no)")
    orderNow = input("Do you want to order anything else?(yes/no)")
    
print(f"The total price to pay is {price}")
print("Thank You!")
